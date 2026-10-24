"""Write paper/numbers.tex: every number the paper quotes, generated from results/analysis (no hand copying).

Use in LaTeX as \\N{key}; an unknown key prints a bold ??key so it cannot pass unnoticed. Keys:
  <study>/<contrast>/{rd,lo,hi,p,pmc,ra,rb,ka,na,kb,nb,tost,holm}  pooled over all models; rd/lo/hi/ra/rb in percentage
                                                                    points; p = CMH p; pmc = McNemar p (paired)
  <study>/cell/<condition>/{acc,rep,n,k}                            pooled over all models (%, count)
  <study>/{valid,missing,keys,models,informative}                   data summary
  econ/<pi>/<ratio>/{catches,precision,breakeven}                   detector economics
  study3/... and pareto/... as listed below

    python scripts/make_macros.py
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / "results" / "analysis"


def pct(x, signed=False):
    if x is None:
        return "--"
    v = 100 * x
    s = f"{v:+.1f}" if signed else f"{v:.1f}"
    return s.replace("-", "$-$") if signed or v < 0 else s


def pfmt(p):
    if p is None:
        return "--"
    if p < 0.001:
        return "< 0.001"
    return "= " + (f"{p:.3f}" if p < 0.1 else f"{p:.2f}")


def main():
    n = json.loads((A / "numbers.json").read_text(encoding="utf-8"))
    out = {}
    for study in ("study1", "study2", "study2b", "study4", "para"):
        if study not in n:
            continue
        s = n[study]
        out[f"{study}/valid"] = f"{s['n_valid_trials']:,}"
        out[f"{study}/missing"] = str(s["n_missing_error"])
        out[f"{study}/keys"] = f"{s['n_trial_keys']:,}"
        out[f"{study}/models"] = str(s["n_models_with_data"])
        out[f"{study}/informative"] = str(len(s["informative_models"]))
        out[f"{study}/roster"] = str(len(s["roster_models"]))
        for cid, d in s["hypotheses"].items():
            a = d["all"]
            k = f"{study}/{cid}"
            out[k + "/rd"] = pct(a["rd_mh"], True)
            out[k + "/lo"], out[k + "/hi"] = (pct(x, True) for x in a["ci95_boot"])
            out[k + "/p"] = pfmt(a["cmh_p"])
            out[k + "/ra"], out[k + "/rb"] = pct(a["rate_a"]), pct(a["rate_b"])
            for x in ("ka", "na", "kb", "nb"):
                out[f"{k}/{x}"] = str(a[{"ka": "k_a", "na": "n_a", "kb": "k_b", "nb": "n_b"}[x]])
            if a.get("paired"):
                out[k + "/pmc"] = pfmt(a["paired"].get("mcnemar_p"))
            if "tost_equivalent" in a:
                out[k + "/tost"] = "equivalent" if a["tost_equivalent"] else "not shown equivalent"
                out[k + "/lo90"], out[k + "/hi90"] = (pct(x, True) for x in a["ci90_boot"])
    for study, d in n.get("holm_families", {}).items():
        for cid, v in d.items():
            out[f"{study}/{cid}/holm"] = pfmt(v["holm_p"])

    # pooled cell rates
    agg = defaultdict(lambda: [0, 0, 0])
    with open(A / "tables" / "cell_counts.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["model"] == "POOLED":  # the table also carries pooled rows; sum the per-model rows only
                continue
            c = agg[(r["study"], r["condition"])]
            c[0] += int(r["n"]); c[1] += int(r["accept"]); c[2] += int(r["report"])
    out["total/decisions"] = f"{sum(n[k]['n_valid_trials'] for k in ('study1', 'study2', 'study2b', 'study4', 'para') if k in n):,}"
    for (study, cond), (nn, ka, kr) in agg.items():
        if nn:
            out[f"{study}/cell/{cond}/acc"] = pct(ka / nn)
            out[f"{study}/cell/{cond}/rep"] = pct(kr / nn)
            out[f"{study}/cell/{cond}/n"] = str(nn)
            out[f"{study}/cell/{cond}/k"] = str(ka)
            out[f"{study}/cell/{cond}/nonacc"] = pct(1 - ka / nn)

    # base-wording Study 2 contrast restricted to the models run in the paraphrases
    para_models = set(n.get("para", {}).get("models", []))
    per = defaultdict(lambda: [0, 0])
    with open(A / "tables" / "cell_counts.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["study"] == "study2" and r["model"] in para_models:
                per[r["condition"]][0] += int(r["accept"]); per[r["condition"]][1] += int(r["n"])
    if per["n_sting50"][1] and per["n_audit50"][1]:
        d = per["n_sting50"][0] / per["n_sting50"][1] - per["n_audit50"][0] / per["n_audit50"][1]
        out["para/base/sting_audit"] = pct(d, True)
        out["para/base/reportfree"] = pct(per["n_reportfree"][0] / per["n_reportfree"][1])
    out["para/models"] = str(len(para_models))

    for row in n.get("detector_economics", {}).get("rows", []):
        k = f"econ/{row['plant_rate']:g}/{row['benign_ratio']:g}"
        out[k + "/catches"] = f"{row['catches']:.1f}"
        out[k + "/precision"] = pct(row["precision"])
        out[k + "/breakeven"] = f"{row['breakeven_ratio']:.2f}"
        out[k + "/genuine"] = f"{row['genuine_reports']:,.0f}"

    for key in ("study2b", "study2"):
        for r in n.get("pareto", {}).get(key, {}).get("pooled", []):
            out[f"pareto/{key}/{r['rule']}/safety"] = f"{r['safety']:.2f}" if r["safety"] is not None else "--"
            out[f"pareto/{key}/{r['rule']}/useful"] = f"{r['usefulness']:.2f}" if r["usefulness"] is not None else "--"

    s3 = n.get("study3", {})
    summ = s3.get("summary", {})
    out["study3/keys"] = str(summ.get("n_trial_keys", "--"))
    out["study3/both"] = str(summ.get("n_both_plays_observed", "--"))
    for pop in ("all", "informative"):
        pooled = (summ.get("pooled") or {}).get(pop) or {}
        for cond, d in (pooled.get("by_condition") or {}).items():
            out[f"study3/{pop}/F/{cond}"] = pct(d.get("F"), True)
            out[f"study3/{pop}/F/{cond}/n"] = str(d.get("n"))
            if d.get("boot_ci95"):
                out[f"study3/{pop}/F/{cond}/lo"], out[f"study3/{pop}/F/{cond}/hi"] = (pct(x, True) for x in d["boot_ci95"])
        for cond, d in (pooled.get("did") or {}).items():
            q = d.get("pooled") or {}
            out[f"study3/{pop}/did/{cond}"] = pct(q.get("estimate"), True)
            out[f"study3/{pop}/did/{cond}/models"] = str(q.get("n_models"))
            out[f"study3/{pop}/did/{cond}/pos"] = str(q.get("models_pos"))
            out[f"study3/{pop}/did/{cond}/neg"] = str(q.get("models_neg"))
            if q.get("boot_ci95"):
                out[f"study3/{pop}/did/{cond}/lo"], out[f"study3/{pop}/did/{cond}/hi"] = (pct(x, True) for x in q["boot_ci95"])
            if q.get("boot_ci90"):
                out[f"study3/{pop}/did/{cond}/lo90"], out[f"study3/{pop}/did/{cond}/hi90"] = (pct(x, True) for x in q["boot_ci90"])
    out["study3/informative"] = str(len(summ.get("informative_models", []) or []))

    lines = ["% Generated by scripts/make_macros.py from results/analysis. Do not edit by hand.",
             r"\makeatletter",
             r"\newcommand{\N}[1]{\ifcsname wp@#1\endcsname\csname wp@#1\endcsname\else\textbf{??#1}\fi}"]
    for k in sorted(out):
        lines.append(r"\expandafter\def\csname wp@" + k + r"\endcsname{" + out[k] + "}")
    lines.append(r"\makeatother")
    (ROOT / "paper" / "numbers.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(out)} macros -> paper/numbers.tex")


if __name__ == "__main__":
    main()
