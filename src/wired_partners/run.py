"""Run the one-shot offer experiment. Resumable: every finished trial is appended to trials.jsonl
immediately, and a rerun with the same --out skips trials already done (failed calls are retried).

    wired-partners --n 3 --out results/pilot
    wired-partners --n 20 --models llama-3.1-8b,gpt-4.1-mini --conditions peer_offer,peer_sting50 --out results/main
"""
import argparse
import concurrent.futures as cf
import hashlib
import json
import logging
import random
import threading
from datetime import datetime, timezone
from pathlib import Path

from .conditions import ALL_CONDITIONS, CONDITIONS, PLAYERS, build_messages
from .llm import DEFAULT_MODELS, MODELS, chat
from .parse import mentions_suspicion, parse_decision

log = logging.getLogger("wired_partners")


def run_trial(model: str, condition: str, i: int, seed: str, paired: bool = False) -> dict:
    # paired: the same seats, round and scores for trial i in every condition (within-trial contrasts)
    rng = random.Random(f"{seed}-{model}-{i}" if paired else f"{seed}-{model}-{condition}-{i}")
    respondent, plant = rng.sample(PLAYERS, 2)
    msgs = build_messages(condition, respondent, plant, rng)
    text, usage, served = chat(model, msgs)
    return {"model": model, "served_model": served, "condition": condition, "trial": i, "seed": seed,
            "respondent": respondent, "plant": plant, "decision": parse_decision(condition, text),
            "suspicion": mentions_suspicion(text),
            "prompt_sha": hashlib.sha256(json.dumps(msgs).encode()).hexdigest()[:12],
            "paired": paired, "response": text, "usage": usage, "finished_utc": datetime.now(timezone.utc).isoformat()}


def is_error(r: dict) -> bool:
    return r["response"].startswith("<<error") or not r["response"].strip()


def load_done(path: Path) -> dict:
    """Latest successful row per (model, condition, trial, seed). Error rows are not 'done'."""
    done = {}
    if path.exists():
        for line in path.open(encoding="utf-8"):
            try:
                r = json.loads(line)
            except json.JSONDecodeError:  # a line cut off by a crash
                continue
            if not is_error(r):
                done[(r["model"], r["condition"], r["trial"], r["seed"])] = r
    return done


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=3, help="trials per model x condition cell")
    ap.add_argument("--models", default=",".join(DEFAULT_MODELS))
    ap.add_argument("--conditions", default=",".join(CONDITIONS))
    ap.add_argument("--seed", default="wp1")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--paired", action="store_true", help="same game context for trial i across conditions")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                        handlers=[logging.FileHandler(out / "run.log", encoding="utf-8"), logging.StreamHandler()])
    logging.getLogger("httpx").setLevel(logging.WARNING)  # one line per HTTP request otherwise
    trials_path = out / "trials.jsonl"
    with open(out / "run_config.jsonl", "a", encoding="utf-8") as f:  # one line per (re)start
        f.write(json.dumps({"started_utc": datetime.now(timezone.utc).isoformat(), "args": vars(a),
                            "models": {m: MODELS[m][:2] for m in a.models.split(",")}}) + "\n")

    done = load_done(trials_path)
    jobs = [(m, c, i) for m in a.models.split(",") for c in a.conditions.split(",") for i in range(a.n)
            if (m, c, i, a.seed) not in done]
    log.info("%d trials already done, %d to run -> %s", len(done), len(jobs), out)

    lock = threading.Lock()
    counts = {"ok": 0, "err": 0}
    with open(trials_path, "a", encoding="utf-8") as f, cf.ThreadPoolExecutor(a.workers) as ex:
        futures = {ex.submit(run_trial, *j, a.seed, a.paired): j for j in jobs}
        for k, fut in enumerate(cf.as_completed(futures), 1):
            m, c, i = futures[fut]
            try:
                row = fut.result()
            except Exception as e:  # noqa: BLE001 - never lose the run to one bad trial
                log.exception("trial %s/%s/%d crashed: %s", m, c, i, e)
                continue
            with lock:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                f.flush()
                counts["err" if is_error(row) else "ok"] += 1
            if is_error(row):
                log.warning("error %s/%s/%d: %s", m, c, i, row["response"][:160])
            if k % 50 == 0 or k == len(jobs):
                log.info("progress %d/%d (ok %d, errors %d)", k, len(jobs), counts["ok"], counts["err"])

    rows = list(load_done(trials_path).values())
    log.info("finished: %d successful trials in %s (rerun the same command to retry errors)", len(rows), trials_path)
    from .analyze import summarize
    summary = summarize(rows)
    (out / "summary.txt").write_text(summary, encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
