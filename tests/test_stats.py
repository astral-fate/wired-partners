import math

import pytest

from wired_partners import stats as S


def test_wilson_known_values():
    lo, hi = S.wilson(5, 20)
    assert lo == pytest.approx(0.1119, abs=1e-4) and hi == pytest.approx(0.4687, abs=1e-4)
    assert S.wilson(0, 20)[0] == 0.0 and S.wilson(20, 20)[1] == 1.0
    assert all(math.isnan(x) for x in S.wilson(0, 0))


def test_mh_rd_single_stratum_equals_simple_rd():
    assert S.mh_rd([(15, 20, 5, 20)]) == pytest.approx(0.5)
    assert S.mh_rd([(3, 10, 7, 14)]) == pytest.approx(3 / 10 - 7 / 14)


def test_mh_rd_skips_empty_strata_and_weights():
    assert S.mh_rd([(15, 20, 5, 20), (0, 0, 3, 20)]) == pytest.approx(0.5)
    # equal-size strata -> simple mean of stratum RDs
    assert S.mh_rd([(10, 20, 0, 20), (20, 20, 20, 20)]) == pytest.approx(0.25)


def test_newcombe_contains_point_and_matches_reference():
    # Newcombe (1998) example: 56/70 vs 48/80 -> 0.0524 to 0.3339
    lo, hi = S.newcombe_rd_ci(56, 70, 48, 80)
    assert lo == pytest.approx(0.0524, abs=1e-3) and hi == pytest.approx(0.3339, abs=1e-3)


def test_paired_ci_properties():
    # With no association between the two members of a pair (phi = 0) the paired interval reduces to the
    # independent Newcombe interval with n in each arm.
    a, b, c, d = 10, 10, 10, 10  # ad - bc = 0
    delta, lo, hi = S.paired_rd_ci(a, b, c, d)
    ilo, ihi = S.newcombe_rd_ci(a + b, 40, a + c, 40)
    assert delta == 0 and lo == pytest.approx(ilo) and hi == pytest.approx(ihi)
    # positive association narrows the interval; the point estimate is (b - c) / n
    delta, lo, hi = S.paired_rd_ci(12, 9, 2, 21)
    assert delta == pytest.approx(7 / 44) and lo < delta < hi
    ilo, ihi = S.newcombe_rd_ci(21, 44, 14, 44)
    assert hi - lo < ihi - ilo


def test_bootstrap_reproducible_with_seed():
    strata = [(15, 20, 5, 20), (2, 20, 1, 20), (10, 20, 10, 20), (20, 20, 3, 20)]
    a = S.bootstrap_over_strata(strata, S.mh_rd, reps=500, seed=7)
    b = S.bootstrap_over_strata(strata, S.mh_rd, reps=500, seed=7)
    c = S.bootstrap_over_strata(strata, S.mh_rd, reps=500, seed=8)
    assert a == b and a["ci95"] != c["ci95"]
    assert a["ci95"][0] <= S.mh_rd(strata) <= a["ci95"][1]


def test_holm():
    assert S.holm([0.01, 0.04, 0.03]) == pytest.approx([0.03, 0.06, 0.06])
    adj = S.holm([0.02, float("nan")])
    assert adj[0] == pytest.approx(0.02) and math.isnan(adj[1])


def test_tost_and_mcnemar():
    assert S.tost_from_ci((-0.05, 0.08), 0.10) and not S.tost_from_ci((-0.05, 0.12), 0.10)
    assert S.mcnemar_exact_p(0, 0) == 1.0
    assert S.mcnemar_exact_p(10, 0) == pytest.approx(2 * 0.5 ** 10)
    assert S.paired_table([(1, 1), (1, 0), (0, 1), (0, 0), (1, 0)]) == (1, 2, 1, 1)
    assert S.pooled_paired_rd([(1, 2, 1, 1)]) == pytest.approx(0.2)


def test_cmh_p_single_stratum_matches_chi2():
    from scipy.stats import chi2_contingency
    p = S.cmh_test_p([(15, 20, 5, 20)])
    chi2 = chi2_contingency([[15, 5], [5, 15]], correction=False)[0]
    # CMH uses N-1 in the variance: chi2_MH = chi2 * (N-1)/N
    from scipy.stats import chi2 as C
    assert p == pytest.approx(C.sf(chi2 * 39 / 40, 1))


def test_sign_count_and_sign_test():
    assert S.sign_count([0.2, -0.1, 0.0, None, float("nan"), 0.3]) == (2, 1, 1)
    assert S.sign_test_p([0, 0]) == 1.0
    assert S.sign_test_p([1] * 6) == pytest.approx(2 * 0.5 ** 6)


def test_mean_diff_ci():
    m, lo, hi = S.mean_diff_ci([1, 1, 1, 1])
    assert m == 1 and lo == pytest.approx(1) and hi == pytest.approx(1)
    m, lo, hi = S.mean_diff_ci([0, 2])
    from scipy.stats import t
    assert m == 1 and hi - m == pytest.approx(t.ppf(0.975, 1) * 1.0)
    assert math.isnan(S.mean_diff_ci([])[0]) and math.isnan(S.mean_diff_ci([1])[1])


def test_favouritism_did_synthetic():
    trials = range(10)
    # condition A: always pass the plant, never the other (F = 1); control B: pass both on even trials (F = 0)
    pa, oa = {i: 1 for i in trials}, {i: 0 for i in trials}
    pb, ob = {i: int(i % 2 == 0) for i in trials}, {i: int(i % 2 == 0) for i in trials}
    d = S.favouritism_did(pa, oa, pb, ob)
    assert len(d) == 10 and sum(d) / len(d) == pytest.approx(1.0)
    # identical conditions -> DiD exactly 0
    assert sum(S.favouritism_did(pb, ob, pb, ob)) == 0
    # only matched trials with both branches observed count
    oa_missing = {i: 0 for i in range(5)}
    pb_short = {i: 0 for i in range(3, 10)}
    d = S.favouritism_did(pa, oa_missing, pb_short, ob)
    assert len(d) == 2  # trials 3 and 4
    # DiD equals F(A) - F(B) computed from paired tables on the same trials
    import random
    rng = random.Random(1)
    p1, o1, p2, o2 = ({i: rng.randint(0, 1) for i in trials} for _ in range(4))
    d = S.favouritism_did(p1, o1, p2, o2)
    fa = S.pooled_paired_rd([S.paired_table((p1[i], o1[i]) for i in trials)])
    fb = S.pooled_paired_rd([S.paired_table((p2[i], o2[i]) for i in trials)])
    assert sum(d) / len(d) == pytest.approx(fa - fb)


def test_pooled_mean_diff_weights_units():
    assert S.pooled_mean_diff([(10.0, 10), (0.0, 30)]) == pytest.approx(0.25)
    assert S.pooled_mean_diff([(5.0, 10), (0.0, 0)]) == pytest.approx(0.5)
    assert math.isnan(S.pooled_mean_diff([]))
    boot = S.bootstrap_over_strata([(10.0, 10), (0.0, 30), (3.0, 10)], S.pooled_mean_diff, reps=200, seed=1)
    assert boot["ci95"][0] <= boot["ci95"][1]


def test_detector_economics():
    e = S.detector_economics(0.01, 0.2, 0.5, 0.05)
    assert e["plants"] == pytest.approx(100) and e["catches"] == pytest.approx(20)
    assert e["plant_reports"] == pytest.approx(50) and e["false_alarms"] == pytest.approx(500)
    assert e["report_precision"] == pytest.approx(50 / 550)
    assert math.isnan(S.detector_economics(0.01, 0, 0, 0)["report_precision"])
