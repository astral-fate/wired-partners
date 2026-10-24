"""Statistics for the Wired Partners analysis.

Binomial intervals, risk differences (independent and paired), Mantel-Haenszel pooling across
models, a bootstrap over models, Holm correction and TOST equivalence. Pure functions over counts,
plus the loader that dedupes trial logs and re-derives every decision with the current parser.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
from scipy import stats as sps

Z95 = 1.959963984540054

# ---------------------------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------------------------
NONACCEPT_CODES = ("DECLINE", "REFUSE", "REPORT", "SAFETY_REFUSAL", "UNPARSED")


def is_error_response(response: str) -> bool:
    t = (response or "").strip()
    return not t or t.startswith("<<error")  # an empty reply never answered: a failed call


def load_trials(path: str | Path) -> tuple[list[dict], dict]:
    """Read a trials.jsonl that may still be appended to.

    Returns (records, meta). One record per (model, condition, trial, seed): the last non-error row
    if any exists, otherwise the last error row (coded ERROR, outcome missing). The decision is always
    re-derived from the raw reply with ``parse.parse_decision``.
    """
    from .parse import parse_decision

    path = Path(path)
    meta = {"path": str(path), "raw_lines": 0, "bad_lines": 0, "error_attempts": 0}
    last_ok: dict[tuple, dict] = {}
    last_err: dict[tuple, dict] = {}
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                meta["raw_lines"] += 1
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:  # a line still being written
                    meta["bad_lines"] += 1
                    continue
                key = (r["model"], r["condition"], r["trial"], r["seed"])
                if is_error_response(r.get("response", "")):
                    meta["error_attempts"] += 1
                    last_err[key] = r
                else:
                    last_ok[key] = r
    out = []
    for key in sorted(set(last_ok) | set(last_err), key=lambda k: tuple(map(str, k))):
        r = last_ok.get(key) or last_err[key]
        dec = parse_decision(r["condition"], r.get("response", ""))
        out.append({"model": r["model"], "condition": r["condition"], "trial": r["trial"], "seed": r["seed"],
                    "served_model": r.get("served_model"), "decision": dec,
                    "accept": None if dec == "ERROR" else int(dec == "ACCEPT"),
                    "report": None if dec == "ERROR" else int(dec == "REPORT"),
                    "nonaccept": None if dec == "ERROR" else int(dec != "ACCEPT")})
    meta["unique_keys"] = len(out)
    return out, meta


# ---------------------------------------------------------------------------------------------
# Single proportions and independent two-sample risk differences
# ---------------------------------------------------------------------------------------------
def wilson(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    """Wilson score interval for k/n."""
    if n == 0:
        return (math.nan, math.nan)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def newcombe_rd_ci(k1: int, n1: int, k2: int, n2: int, z: float = Z95) -> tuple[float, float]:
    """Newcombe (1998, method 10) hybrid-score CI for p1 - p2, independent samples."""
    if n1 == 0 or n2 == 0:
        return (math.nan, math.nan)
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson(k1, n1, z)
    l2, u2 = wilson(k2, n2, z)
    d = p1 - p2
    return (d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2))


def fisher_p(k1: int, n1: int, k2: int, n2: int) -> float:
    """Two-sided Fisher exact test of k1/n1 vs k2/n2."""
    if n1 == 0 or n2 == 0:
        return math.nan
    return float(sps.fisher_exact([[k1, n1 - k1], [k2, n2 - k2]], alternative="two-sided")[1])


def holm(pvals: Sequence[float]) -> list[float]:
    """Holm step-down adjusted p-values; NaNs are left out of the family and returned as NaN."""
    idx = [i for i, p in enumerate(pvals) if p is not None and not math.isnan(p)]
    m = len(idx)
    adj = [math.nan] * len(pvals)
    running = 0.0
    for rank, i in enumerate(sorted(idx, key=lambda j: pvals[j])):
        running = max(running, min(1.0, (m - rank) * pvals[i]))
        adj[i] = running
    return adj


# ---------------------------------------------------------------------------------------------
# Mantel-Haenszel pooled risk difference across strata (models)
# ---------------------------------------------------------------------------------------------
Stratum = tuple[int, int, int, int]  # (k1, n1, k2, n2)


def _usable(strata: Iterable[Stratum]) -> list[Stratum]:
    return [s for s in strata if s[1] > 0 and s[3] > 0]


def mh_rd(strata: Iterable[Stratum]) -> float:
    """Mantel-Haenszel risk difference: weights w = n1*n2/(n1+n2)."""
    s = _usable(strata)
    num = sum((k1 / n1 - k2 / n2) * n1 * n2 / (n1 + n2) for k1, n1, k2, n2 in s)
    den = sum(n1 * n2 / (n1 + n2) for _, n1, _, n2 in s)
    return num / den if den > 0 else math.nan


def mh_rd_sato_ci(strata: Iterable[Stratum], z: float = Z95) -> tuple[float, float]:
    """Trial-level CI for the MH risk difference with the Sato (1989) variance (models fixed)."""
    s = _usable(strata)
    if not s:
        return (math.nan, math.nan)
    rd = mh_rd(s)
    W = sum(n1 * n2 / (n1 + n2) for _, n1, _, n2 in s)
    P = sum((n1 ** 2 * k2 - n2 ** 2 * k1 + n1 * n2 * (n2 - n1) / 2) / (n1 + n2) ** 2 for k1, n1, k2, n2 in s)
    Q = sum((k1 * (n2 - k2) + k2 * (n1 - k1)) / (2 * (n1 + n2)) for k1, n1, k2, n2 in s)
    var = (rd * P + Q) / W ** 2
    se = math.sqrt(max(var, 0.0))
    return (rd - z * se, rd + z * se)


def cmh_test_p(strata: Iterable[Stratum]) -> float:
    """Cochran-Mantel-Haenszel chi-square test (1 df, no continuity correction), two-sided p."""
    s = [t for t in _usable(strata) if t[1] + t[3] > 1]
    num, var = 0.0, 0.0
    for k1, n1, k2, n2 in s:
        N = n1 + n2
        m1 = k1 + k2
        num += k1 - n1 * m1 / N
        var += n1 * n2 * m1 * (N - m1) / (N ** 2 * (N - 1))
    if var <= 0:
        return 1.0 if s else math.nan
    return float(sps.chi2.sf(num ** 2 / var, 1))


def bootstrap_over_strata(strata: Sequence, stat, reps: int = 5000, seed: int = 20261024,
                          levels: Sequence[float] = (0.95, 0.90)) -> dict:
    """Percentile bootstrap resampling strata (models) with replacement.

    ``stat`` maps a list of strata to a number. Returns {"ci95": (lo, hi), "ci90": (lo, hi), "reps": n}.
    Resamples where the statistic is undefined are dropped (count reported as "undefined").
    """
    strata = list(strata)
    out: dict = {"reps": reps}
    if len(strata) == 0:
        for lv in levels:
            out[f"ci{int(round(lv * 100))}"] = (math.nan, math.nan)
        out["undefined"] = reps
        return out
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(strata), size=(reps, len(strata)))
    vals = np.array([stat([strata[i] for i in row]) for row in idx], dtype=float)
    ok = vals[~np.isnan(vals)]
    out["undefined"] = int(reps - ok.size)
    for lv in levels:
        a = (1 - lv) / 2
        out[f"ci{int(round(lv * 100))}"] = ((float(np.quantile(ok, a)), float(np.quantile(ok, 1 - a)))
                                            if ok.size else (math.nan, math.nan))
    return out


def tost_from_ci(ci90: tuple[float, float], margin: float) -> bool:
    """TOST at alpha = .05: equivalent iff the 90% CI lies inside (-margin, +margin)."""
    lo, hi = ci90
    return bool(not math.isnan(lo) and lo > -margin and hi < margin)


# ---------------------------------------------------------------------------------------------
# Paired (matched-trial) risk differences
# ---------------------------------------------------------------------------------------------
def paired_table(pairs: Iterable[tuple[int, int]]) -> tuple[int, int, int, int]:
    """(a, b, c, d) from (outcome_A, outcome_B) pairs: a=1/1, b=1/0, c=0/1, d=0/0."""
    a = b = c = d = 0
    for x, y in pairs:
        if x and y:
            a += 1
        elif x:
            b += 1
        elif y:
            c += 1
        else:
            d += 1
    return a, b, c, d


def paired_rd_ci(a: int, b: int, c: int, d: int, z: float = Z95) -> tuple[float, float, float]:
    """Paired RD p_A - p_B = (b - c)/n with Newcombe's (1998, method 10) hybrid-score interval."""
    n = a + b + c + d
    if n == 0:
        return (math.nan, math.nan, math.nan)
    p1, p2 = (a + b) / n, (a + c) / n
    l1, u1 = wilson(a + b, n, z)
    l2, u2 = wilson(a + c, n, z)
    den = (a + b) * (c + d) * (a + c) * (b + d)
    if den == 0:
        phi = 0.0
    else:
        num = a * d - b * c
        num = max(num - n / 2, 0.0) if num > 0 else num
        phi = num / math.sqrt(den)
    delta = p1 - p2
    lo = delta - math.sqrt(max((p1 - l1) ** 2 - 2 * phi * (p1 - l1) * (u2 - p2) + (u2 - p2) ** 2, 0.0))
    hi = delta + math.sqrt(max((u1 - p1) ** 2 - 2 * phi * (u1 - p1) * (p2 - l2) + (p2 - l2) ** 2, 0.0))
    return delta, max(-1.0, lo), min(1.0, hi)


def mcnemar_exact_p(b: int, c: int) -> float:
    """Exact (binomial) two-sided McNemar test on the discordant pairs."""
    if b + c == 0:
        return 1.0
    return float(sps.binomtest(b, b + c, 0.5).pvalue)


def pooled_paired_rd(tables: Iterable[tuple[int, int, int, int]]) -> float:
    """Pooled paired RD across strata: sum(b - c) / sum(n) (each matched pair weighted equally)."""
    t = list(tables)
    n = sum(sum(x) for x in t)
    return sum(x[1] - x[2] for x in t) / n if n else math.nan


# ---------------------------------------------------------------------------------------------
# Paired per-trial differences, difference-in-differences, sign counts (Studies 2b and 3)
# ---------------------------------------------------------------------------------------------
def sign_count(values: Iterable[float | None], tol: float = 1e-12) -> tuple[int, int, int]:
    """(positive, negative, ties) among the non-missing values; |v| <= tol counts as a tie."""
    pos = neg = tie = 0
    for v in values:
        if v is None or (isinstance(v, float) and math.isnan(v)):
            continue
        if v > tol:
            pos += 1
        elif v < -tol:
            neg += 1
        else:
            tie += 1
    return pos, neg, tie


def matched_differences(da: dict, db: dict) -> list[float]:
    """Per-unit differences da[k] - db[k] over the keys present (non-missing) in both mappings, in key order."""
    return [da[k] - db[k] for k in sorted(set(da) & set(db), key=str)
            if da[k] is not None and db[k] is not None]


def mean_diff_ci(diffs: Sequence[float], z: float = Z95) -> tuple[float, float, float]:
    """Mean of matched differences with a t interval (df = n - 1). (nan, nan, nan) if n == 0; CI nan if n == 1."""
    x = np.asarray(list(diffs), dtype=float)
    n = x.size
    if n == 0:
        return (math.nan, math.nan, math.nan)
    m = float(x.mean())
    if n == 1:
        return (m, math.nan, math.nan)
    se = float(x.std(ddof=1)) / math.sqrt(n)
    t = float(sps.t.ppf(sps.norm.cdf(z), n - 1))
    return (m, m - t * se, m + t * se)


def sign_test_p(diffs: Iterable[float]) -> float:
    """Exact two-sided sign test on the non-zero matched differences (1.0 if all are zero)."""
    pos, neg, _ = sign_count(diffs)
    if pos + neg == 0:
        return 1.0
    return float(sps.binomtest(pos, pos + neg, 0.5).pvalue)


DiffStratum = tuple[float, int]  # (sum of matched differences, number of matched units)


def pooled_mean_diff(strata: Iterable[DiffStratum]) -> float:
    """Pooled mean difference across strata: sum of sums / sum of n (each matched unit weighted equally)."""
    s = [t for t in strata if t[1] > 0]
    n = sum(t[1] for t in s)
    return sum(t[0] for t in s) / n if n else math.nan


def favouritism_did(plant_a: dict, other_a: dict, plant_b: dict, other_b: dict) -> list[float]:
    """Trial-matched difference-in-differences of favouritism.

    Each mapping is {trial: 1 if PASS else 0}. For trial i, d_X(i) = pass_plant - pass_other in condition X
    (only trials where both branches are observed), and the returned list holds d_A(i) - d_B(i) for trials
    observed in both conditions. Its mean is F(A) - F(B) on the matched trials.
    """
    da = {k: plant_a[k] - other_a[k] for k in set(plant_a) & set(other_a)}
    db = {k: plant_b[k] - other_b[k] for k in set(plant_b) & set(other_b)}
    return matched_differences(da, db)


def detector_economics(plant_rate: float, accept_rate: float, report_rate_plant: float,
                       report_rate_benign: float, offers: int = 10_000, benign_volume: int = 10_000) -> dict:
    """Expected counts per ``offers`` alliance offers when a share ``plant_rate`` are planted stings.

    plants = plant_rate * offers; catches = plants * accept_rate; plant_reports = plants * report_rate_plant;
    false_alarms = benign_volume * report_rate_benign; precision = plant_reports / (plant_reports + false_alarms).
    """
    plants = plant_rate * offers
    catches = plants * accept_rate
    plant_reports = plants * report_rate_plant
    false_alarms = benign_volume * report_rate_benign
    tot = plant_reports + false_alarms
    return dict(plants=plants, catches=catches, plant_reports=plant_reports, false_alarms=false_alarms,
                report_precision=plant_reports / tot if tot > 0 else math.nan)
