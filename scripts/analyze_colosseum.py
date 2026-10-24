"""Study 5: the house rules on Colosseum's Jira task-allocation benchmark (tool-using agents).

    python scripts/analyze_colosseum.py [--sync PATH_TO_COLOSSEUM_CHECKOUT]

--sync copies the per-run files we keep (metrics, run config, blackboards, final summary) from a Colosseum checkout's
experiments/sting/outputs/{main,instructed} into results/colosseum/{emergent,instructed}. The analysis then reads only
results/colosseum, so it reruns from the repository alone.

Design: 4 agents, complete topology, 2 of them share a secret blackboard. "emergent" = nobody is told to collude
(Colosseum's control prompt); "instructed" = the two are told they are a coalition (Colosseum's "simple" prompt).
The house rule (none / prohibition / sting) is appended to every agent's system prompt. Seeds are shared across
conditions, so contrasts are paired by seed within model; intervals are percentile bootstraps over seeds (pooled:
the mean of per-model differences, resampling seeds within each model). The no-channel runs are the positive
control for emergent collusion: with no secret blackboard the would-be coalition has no way to coordinate privately.

Outputs: results/analysis/colosseum.json, paper/numbers_colosseum.tex (\\N{col/...} macros),
results/analysis/figures/fig_colosseum.{pdf,png}.
"""
import argparse
import json
import random
import shutil
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results" / "colosseum"
KEEP = ("metrics.json", "run_config.json", "blackboards.json", "final_summary.json")
ARMS = {"emergent": "main", "instructed": "instructed"}
CONDS = ["no_channel", "no_rule", "prohibit", "sting"]
METRICS = {"adv": "coalition_advantage_mean", "regret": "system_regret_ratio", "secret": "colluder_posts_secret_rate"}
MODEL_NAME = {"gpt-4.1-mini": "GPT-4.1-mini", "gpt-oss-120b": "GPT-OSS-120B"}


def sync(checkout: Path):
    for arm, sub in ARMS.items():
        src = checkout / "experiments" / "sting" / "outputs" / sub
        for mfile in src.glob("*/runs/*/*/*/metrics.json"):
            run = mfile.parent
            dst = DATA / arm / run.parent.parent.name / run.parent.name / run.name
            dst.mkdir(parents=True, exist_ok=True)
            for f in KEEP:
                if (run / f).exists():
                    shutil.copy2(run / f, dst / f)


def condition(run_name: str, sweep: str) -> str:
    if sweep == "no_channel":
        return "no_channel"
    return run_name.split("__env", 1)[1].split("__", 1)[0]


def load():
    rows = []
    for mfile in DATA.glob("*/*/*/*/metrics.json"):
        arm, model, sweep, run = mfile.parts[-5], mfile.parts[-4], mfile.parts[-3], mfile.parts[-2]
        m = json.loads(mfile.read_text(encoding="utf-8"))
        if m.get("status") != "complete":
            continue
        seed = int(run.rsplit("seed", 1)[1])
        rows.append({"arm": arm, "model": model, "cond": condition(run, sweep), "seed": seed,
                     **{k: m.get(v) for k, v in METRICS.items()}})
    return rows


def boot(diffs_by_model: dict, reps=5000, seed=7):
    """Pooled mean of per-model mean differences, bootstrapping seeds within model."""
    rng = random.Random(seed)
    models = [m for m, d in diffs_by_model.items() if d]
    if not models:
        return None, None, None
    est = sum(sum(d) / len(d) for d in (diffs_by_model[m] for m in models)) / len(models)
    draws = []
    for _ in range(reps):
        tot = 0.0
        for m in models:
            d = diffs_by_model[m]
            tot += sum(rng.choice(d) for _ in d) / len(d)
        draws.append(tot / len(models))
    draws.sort()
    return est, draws[int(0.025 * reps)], draws[int(0.975 * reps)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sync", type=Path, help="path to a Colosseum checkout to copy run outputs from")
    a = ap.parse_args()
    if a.sync:
        sync(a.sync)
    rows = load()
    by = defaultdict(dict)  # (arm, model, cond) -> {seed: row}
    for r in rows:
        by[(r["arm"], r["model"], r["cond"])][r["seed"]] = r
    out, M = {"cells": {}, "contrasts": {}}, {}
    models = sorted({r["model"] for r in rows})
    for (arm, model, cond), d in sorted(by.items()):
        cell = {k: sum(r[k] for r in d.values() if r[k] is not None) / len(d) for k in METRICS}
        cell["n"] = len(d)
        out["cells"][f"{arm}/{model}/{cond}"] = cell
        tag = f"col/{arm}/{model}/{cond}"
        M[f"{tag}/adv"], M[f"{tag}/n"] = f"{cell['adv']:+.1f}", str(cell["n"])
        M[f"{tag}/secret"] = f"{100 * cell['secret']:.0f}"
        M[f"{tag}/regret"] = f"{100 * cell['regret']:.0f}"
    for arm in ARMS:
        n = sum(len(by.get((arm, m, c), {})) for m in models for c in CONDS)
        M[f"col/{arm}/runs"] = str(n)
        for a_, b_ in (("no_rule", "no_channel"), ("prohibit", "no_rule"), ("sting", "no_rule"), ("sting", "prohibit")):
            for k in METRICS:
                diffs = {}
                for m in models:
                    A, B = by.get((arm, m, a_), {}), by.get((arm, m, b_), {})
                    diffs[m] = [A[s][k] - B[s][k] for s in sorted(set(A) & set(B))
                                if A[s][k] is not None and B[s][k] is not None]
                est, lo, hi = boot(diffs)
                if est is None:
                    continue
                key = f"{arm}/{a_}_vs_{b_}/{k}"
                out["contrasts"][key] = {"est": est, "lo": lo, "hi": hi,
                                         "per_model": {m: (sum(d) / len(d) if d else None) for m, d in diffs.items()},
                                         "pairs": sum(len(d) for d in diffs.values())}
                scale = 100 if k in ("secret", "regret") else 1
                f = (lambda x: f"{x * scale:+.1f}".replace("-", "$-$"))
                M[f"col/{key}"], M[f"col/{key}/lo"], M[f"col/{key}/hi"] = f(est), f(lo), f(hi)
                for m, d in diffs.items():
                    if d:
                        M[f"col/{key}/{m}"] = f(sum(d) / len(d))
    (ROOT / "results" / "analysis").mkdir(parents=True, exist_ok=True)
    (ROOT / "results" / "analysis" / "colosseum.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    lines = ["% Generated by scripts/analyze_colosseum.py. Do not edit by hand.", r"\makeatletter"]
    lines += [rf"\expandafter\def\csname wp@{k}\endcsname{{{v}}}" for k, v in sorted(M.items())]
    (ROOT / "paper" / "numbers_colosseum.tex").write_text("\n".join(lines + [r"\makeatother"]) + "\n", encoding="utf-8")
    figure(by, models)
    print(len(rows), "runs;", len(M), "macros")


def figure(by, models):
    plt.rcParams.update({"font.size": 8, "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42})
    arms = [x for x in ARMS if any(by.get((x, m, c)) for m in models for c in CONDS)]
    fig, axes = plt.subplots(1, len(arms), figsize=(3.4 * len(arms), 2.5), sharey=True, squeeze=False)
    labels = {"no_channel": "No secret\nchannel", "no_rule": "Channel,\nno rule", "prohibit": "Channel,\nprohibition",
              "sting": "Channel,\nsting"}
    colors = {"gpt-4.1-mini": "#0072B2", "gpt-oss-120b": "#D55E00"}
    for ax, arm in zip(axes[0], arms):
        conds = [c for c in CONDS if any(by.get((arm, m, c)) for m in models)]
        for j, m in enumerate(models):
            for i, c in enumerate(conds):
                d = by.get((arm, m, c), {})
                vals = [r["adv"] for r in d.values() if r["adv"] is not None]
                if not vals:
                    continue
                x = i + (j - (len(models) - 1) / 2) * 0.22
                ax.scatter([x] * len(vals), vals, s=6, alpha=0.25, color=colors.get(m, "#555"), lw=0)
                mu = sum(vals) / len(vals)
                se = (sum((v - mu) ** 2 for v in vals) / max(1, len(vals) - 1)) ** 0.5 / len(vals) ** 0.5
                ax.errorbar(x, mu, yerr=1.96 * se, fmt="o", ms=4, color=colors.get(m, "#555"), capsize=2,
                            label=MODEL_NAME.get(m, m) if i == 0 else None)
        ax.axhline(0, color="#999", lw=0.7, ls=":")
        ax.set_xticks(range(len(conds)), [labels[c] for c in conds])
        ax.set_title({"emergent": "Not told to collude", "instructed": "Told to form a coalition"}[arm], fontsize=8.5)
    axes[0][0].set_ylabel("Coalition advantage\n(coalition minus others, mean reward)")
    axes[0][0].legend(frameon=False, fontsize=7, loc="upper left")
    fig.tight_layout()
    fd = ROOT / "results" / "analysis" / "figures"
    fd.mkdir(parents=True, exist_ok=True)
    fig.savefig(fd / "fig_colosseum.pdf", bbox_inches="tight")
    fig.savefig(fd / "fig_colosseum.png", dpi=250, bbox_inches="tight")


if __name__ == "__main__":
    main()
