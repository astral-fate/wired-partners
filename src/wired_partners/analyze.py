"""Summaries with Wilson 95% intervals.

    wp-analyze results/pilot/trials.jsonl
"""
import argparse
import json
import math
from collections import defaultdict


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def reparse(rows: list[dict]) -> list[dict]:
    """Re-derive every decision from the raw reply with the current parser."""
    from .parse import parse_decision
    return [{**r, "decision": parse_decision(r["condition"], r["response"])} for r in rows]


def summarize(rows: list[dict]) -> str:
    rows = reparse(rows)
    cells = defaultdict(list)
    for r in rows:
        cells[(r["model"], r["condition"])].append(r)
    lines = [f"{'model':14} {'condition':18} {'n':>3}  {'accept [95% CI]':>20}  {'decline':>7} {'report':>6} "
             f"{'unparsed':>8} {'errors':>6} {'suspicion':>9}"]
    for (m, c), cell in sorted(cells.items()):
        n = len(cell)
        cnt = lambda d: sum(r["decision"] == d for r in cell)
        acc = cnt("ACCEPT")
        lo, hi = wilson(acc, n)
        errs = cnt("ERROR") + cnt("SAFETY_REFUSAL")
        lines.append(f"{m:14} {c:18} {n:3}  {acc / n:5.2f} [{lo:.2f}, {hi:.2f}]  "
                     f"{(cnt('DECLINE') + cnt('REFUSE')) / n:7.2f} {cnt('REPORT') / n:6.2f} "
                     f"{cnt('UNPARSED') / n:8.2f} {errs:6} {sum(r['suspicion'] for r in cell) / n:9.2f}")
    toks = sum((r.get("usage") or {}).get("total_tokens", 0) for r in rows)
    lines.append(f"\ncalls: {len(rows)}   total tokens: {toks}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("trials", nargs="+")
    a = ap.parse_args()
    rows = [json.loads(line) for p in a.trials for line in open(p, encoding="utf-8")]
    print(summarize(rows))


if __name__ == "__main__":
    main()
