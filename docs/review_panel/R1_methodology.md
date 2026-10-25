# Peer Review Report

## Manuscript Information
- **Title**: Wired Partners: Announced Stings versus Monitoring as Deterrents to Collusion Between LLM Agents, from Single Offers to Tool-Using Teams
- **Manuscript ID**: Apart Research AI Collusion Research Sprint, Track 3 (sprint report, 8-page body)
- **Review Date**: 2026-10-25
- **Review Round**: Round 1 review (pre-submission panel)

---

## Reviewer Information

### Reviewer Role
Peer Reviewer 1 (Methodology)

### Reviewer Identity
I review causal inference and statistics for LLM-agent behavioural experiments: paired and factorial prompt manipulations, inference clustered by model, multiplicity, equivalence testing, and the validity of LLM judges and parsers.

### Review Focus
Can the designs identify the causal claims in the abstract (the prohibition versus the odds of being caught; whether deterrence fails for tool-using teams)? Do the inferential procedures (CMH, McNemar, bootstrap over models, TOST, Holm) match the estimands and the level of generalisation claimed? Do the reported numbers reproduce from the released logs?

---

## Overall Assessment

### Recommendation
- [ ] Accept
- [ ] Minor Revision
- [x] **Major Revision**
- [ ] Reject

### Confidence Score
4. This is mostly within my expertise. I read every pooled table, the statistics module and the Study 5 script, and I re-derived the Study 5 cells from `results/analysis/colosseum.json`. I did not rerun the analysis pipeline.

Confidence is an uncertainty/scope disclosure only; it never changes consensus counts, severity, decision bearing, or arbitration.

### Calibration Status
`NOT_CALIBRATED`

### Summary Assessment
The paper tests announced "sting" rules against audits and bare prohibitions. The first setting is one-shot collusive offers to ten LLMs (Studies 1–4, 10,903 decisions); the second is multi-round tool-using agents in Colosseum (Study 5). Studies 1–4 are well engineered. Contexts are seeded and matched across conditions, there are positive and placebo controls, and the Study 4 contrast that removes one sentence (the mild 50% sting with and without the prohibition) is clean. Every number I spot-checked reproduces from the logs (18 of 18; table below).

The problems are about inference, not bookkeeping:

- **Study 5 does not support its headline.** The instructed arm has no no-channel control. In the emergent arm, the coalition already has an advantage of +0.5 to +2.3 points with no secret channel. For two of the three models, the instructed coalition's advantage is below that model's own no-channel baseline, and in meeting scheduling it is negative. So there is no demonstrated collusive advantage for the rules to fail to deter. The null rule effects are also read as evidence of no effect, without an equivalence test.
- **p-values and intervals use different units of analysis.** p-values treat trials as independent. Intervals bootstrap only over the 10 models. The two disagree in visible places.
- **The headline effect is exploratory.** The abstract's main effect (the prohibition alone, −48 points) and several other headline claims lie outside the Holm-corrected confirmatory families. Several Study 4 arms were added hours after the base arms (per `run_config.jsonl`). For three models those arms were served under a different provider identifier.
- **The expected-value benchmark is not identified for the severe rules.** Disqualification is never priced in points, so "should decline" at a 1% rate is asserted rather than derived.

All of this is repairable by re-analysis, reframing and a small amount of new data.

---

## Strengths

### S1: Matched contexts across conditions, with a seeded, resumable harness
Each trial index has the same seats, round and scores in every condition within a study. Per-model contrasts are therefore paired, and McNemar tests are appropriate. The run loop skips finished keys and retries only failed calls, and it does not re-draw contexts.
**Evidence Anchor**: text: §3.1 "Within each study, contexts are paired: trial i has the same seats, round and scores in every condition."

### S2: Positive controls and placebo controls in the one-shot studies
Collusion with no rule (74.4%, 76.0%) and the designer offer (80.5%) show that the harness elicits acceptance. The 2b placebo (late arrival, same penalty, 71.5%) and the Study 2 neutral placebo (73.7%) show that adding a rule sentence does not, by itself, move acceptance. These controls guard against "any extra text deters".
**Evidence Anchor**: text: §4 Data "Two positive controls show that the harness elicits collusion when nothing deters it"

### S3: A clean single-sentence manipulation of the prohibition, inside the confirmatory family
`c_mild_noprohibit_sting50` differs from `c_mild_sting50` only by deleting "Secret alliances are against the house rules." (`src/wired_partners/conditions.py`, `V4_RULES`). It moves acceptance from 23.0% to 61.0% (RD +38.0 [+19.0, +56.5]). Of all the evidence for the prohibition's role, this contrast has the cleanest causal identification.
**Evidence Anchor**: text: §4 RQ2 "Removing the prohibition from the mild 50% sting raised acceptance from 23.0% to 61.0%"

### S4: Every paper number is generated from logs by scripts
Macros are produced by `scripts/make_macros.py` and `scripts/analyze_colosseum.py`. Raw replies, the served model identifier and the prompt hash are logged per trial. My spot-checks reproduced all 18 numbers I tried. This is reproducibility well above the norm for a sprint report.
**Evidence Anchor**: dataset: results/analysis/tables/cell_counts.md and numbers.tex — macros match pooled cell counts

### S5: Floor effects and wording-dependence are acknowledged rather than overclaimed in the one-shot studies
The paper states that the severe-penalty floor cannot separate rule following from risk pricing. It also treats the mild sting-versus-audit reversal as exploratory because the sign changed across wordings in Study 2.
**Evidence Anchor**: text: §4 RQ1 "this floor cannot separate rule following from risk pricing; Study 4 does"

### S6: An inclusion rule and a missing-data policy, with missingness reported per study
There is an 80% valid-trial roster rule. Empty reasoning-budget replies are retried and never coded as decisions, and valid counts are reported per study (Appendix K). I checked the logs: duplicate keys in `main_v2b` are empty `UNPARSED` replies that were later retried, which matches the stated policy.
**Evidence Anchor**: text: §3.3 "A model enters a study's analysis if at least 80% of its trials are valid"

---

## Weaknesses

### W1: Study 5 has no demonstrated collusive advantage to deter, yet the abstract says agents "kept their advantage"
**Problem**: The paper names the no-channel arm as the positive control ("collusion that a rule could deter must first raise coalition advantage above it", §3.4). That arm exists only in the emergent Jira arm.

- **Emergent arm (from `colosseum.json`).** Without any secret channel, the would-be coalition already has a mean advantage of +2.31 (GPT-4.1-mini), +0.51 (GPT-OSS-120B) and +1.36 (DeepSeek-V4.1-Flash). The advantage is structural (seat and task allocation), not collusive.
- **Instructed arm.** It has no no-channel cell at all. Its no-rule advantages are +3.75, +0.47 and +1.10. For GPT-OSS-120B and DeepSeek, these are *below* the same model's no-channel baseline on the same seeds.
- **Meeting scheduling.** The advantage is negative under every rule (−0.36, −0.17).

So in at least two of three Jira models, and in the second environment, there is no collusive advantage for a rule to remove. The abstract claim "kept their advantage under every rule, with three models and in two environments" and the conclusion "tool-using agents told to collude kept their advantage under every rule, in two environments" do not follow from the data. The §4 text itself concedes that the meeting coalition "gained nothing".

**Evidence Anchor**: dataset: results/analysis/colosseum.json — emergent/*/no_channel adv = +2.31/+0.51/+1.36; instructed/*/no_rule adv = +3.75/+0.47/+1.10; meeting/*/no_rule adv = −0.36/−0.17

**Why it matters**: The paper's second headline conclusion, that the deterrence stops at the single offer, rests on this study. Without a positive control in the instructed arm, "the rule did not reduce the advantage" cannot be told apart from "there was nothing collusive to reduce".

**Suggestion**:
1. Run an instructed no-channel arm (20 seeds × 3 models). Define collusive advantage as instructed-with-channel minus instructed-no-channel, paired by seed.
2. Until then, restrict the claim to GPT-4.1-mini in Jira, the only model whose instructed advantage exceeds its no-channel baseline.
3. Drop "in two environments" from the abstract and conclusion. State that meeting scheduling failed its positive control.
4. Report the emergent no-channel baseline in Figure 1 next to the instructed panels.

**Severity**: Critical (repairable by reframing the claim and adding one control arm)
**Confidence**: 5 (re-derived directly from the released `colosseum.json` cells)

### W2: Null rule effects in Study 5 are read as "no effect" without equivalence bounds or a minimum detectable effect
**Problem**: Several Study 5 results are reported as absences of effect: "The rules did not reduce that advantage", the sting changed it by −0.0 [−1.9, +1.6], and "Neither rule changed the coalition's advantage". The pooled no-rule instructed advantage is about +1.8 points (mean of 3.75, 0.47 and 1.10). The sting interval's lower bound of −1.9 therefore includes complete removal of the entire advantage. Per model, the prohibition *raised* GPT-4.1-mini's advantage by +3.9 points. No TOST, equivalence margin or minimum detectable effect is given for Study 5, whereas Studies 2b and 4 do use TOST.
**Evidence Anchor**: text: §4 RQ5 "The rules did not reduce that advantage: the prohibition changed it by +1.1 [-0.4, +2.6] and the sting by -0.0 [-1.9, +1.6]"
**Why it matters**: With 20 seeds per cell, the study cannot rule out a sting that removes most of the advantage. "Not shown to reduce" is being reported as "did not reduce".
**Suggestion**: Pre-specify a margin, for example half the instructed collusive advantage once W1 is fixed, and report TOST or 90% CIs against it. Report the minimum detectable effect for 20 seeds given the observed SD of the seed-level differences. Reword the claim to "we could not detect a reduction; effects larger than X are excluded".
**Severity**: Major
**Confidence**: 5 (direct comparison of the reported CI to the reported cell means)

### W3: p-values and confidence intervals are computed at different units of inference, and disagree
**Problem**:
- **Pooled p-values treat trials as the unit.** The CMH chi-square uses 200 trials per arm, and the "exact McNemar (pooled pairs)" ignores model clustering (`contrasts.md`).
- **Pooled 95% CIs treat models as the unit.** They are percentile bootstraps that resample only the 10 models (`stats.bootstrap_over_strata`), with no within-model resampling of trials. Within-model sampling variance therefore never enters the interval.
- **Consequences.** Several intervals have a hard bound at exactly 0: P50 [−1.5, +0.0], RNA50 [−15.5, +0.0], auth-severe [+0.0, +25.5]. In these cases most models sit at 0/20 vs 0/20, and the bootstrap collapses. The two procedures also contradict each other: RNA50 is reported with Holm p = 0.038 and a CI that includes zero, and the authentication effect is reported as "McNemar p < 0.001" with a CI of [+1.0, +30.5]. That effect is concentrated in 2 of 10 models (Ministral-8B, Llama-3.1-8B), so at the model level it would not be significant.
- **Equivalence inherits the problem.** TOST uses the same model-only 90% bootstrap. That makes floor-level "equivalence" (RQ1) close to automatic: when 8–9 of 10 models are at 0/20 in both arms, the bootstrap distribution is almost degenerate.

**Evidence Anchor**: table: results/analysis/tables/study2b_primary.md — RNA50 RD_MH −0.059, 95% CI (boot) [−0.155, +0.000], CMH p = 0.009
**Why it matters**: The prose generalises to "agents", which implies models are a sample. The p-values assume a fixed set of models, and the intervals understate within-model uncertainty. Neither procedure matches the claimed estimand, and readers see contradictory significance verdicts.
**Suggestion**:
1. Fit a logistic GLMM with fixed condition effects, a random intercept and condition slope by model, and a random intercept by context index. Report the population-averaged RD with profile or parametric-bootstrap CIs.
2. Alternatively, use a two-stage bootstrap that resamples models and then trials within model, and compute p-values from the same resampling.
3. State the estimand explicitly ("these ten models" versus "LLMs like these"). Report model sign counts, for example "k of 10 models moved", next to every pooled headline. The tables already compute this but the text omits it.
4. Re-run TOST on the corrected intervals.

**Severity**: Major
**Confidence**: 5 (read `src/wired_partners/stats.py` and the pooled tables)

### W4: Headline claims lie outside the confirmatory families, and several Study 4 arms were added after base results
**Problem**:
- **The headline effect was never in a confirmatory family.** The Holm families are fixed in `scripts/analyze_all.py` (`FAMILIES`): Study 2b {P10, P50, RNA10, RNA50} and Study 4 {severe vs mild at 50% and 1%, mild rate, prohibition removed}. The abstract's lead effect (prohibition alone, 76.0% → 28.0%) is not in either family, and nor are the authentication effect, the safe-harbour results or every Study 5 contrast.
- **Arms were added after base results.** In `results/main_v4/run_config.jsonl`, the base Study 4 arms start at 12:45 UTC. `c_safeharbour_sting50` was added at 17:17, `c_auth_*` at 17:29, and `c_prohibit_p1/p2` and `c_auth_*_warned` at 18:51. The "warned" arm is visibly a reaction to the authentication result, and the rewordings were added to defend the headline.
- **The pre-specification claim cannot be checked.** The repository's first commit (2026-10-24 20:48 +0300, i.e. 17:48 UTC) postdates the base data. The statement "a rule fixed before outcomes were examined" therefore cannot be verified, and no preregistration is cited.
- **There are many tests.** About 40 pooled Study 4 contrasts appear in `contrasts.md`, each with CMH and McNemar p-values.

**Evidence Anchor**: text: §3.4 "Two confirmatory families are Holm-corrected: Study 2b {sting vs audit acceptance at 10% and 50%, reporting given non-acceptance at 10% and 50%} and Study 4"
**Why it matters**: The paper's central message, "the prohibition does most of the work", is carried by an effect that was never confirmatory. Arms added in sequence turn Study 4 into an adaptive design, which readers should be told about.
**Suggestion**:
1. Mark every claim in the abstract and §4 as confirmatory or exploratory.
2. Disclose the order in which arms were added, with timestamps, in Appendix A.
3. Either justify adding S4_prohibit to the confirmatory family or apply Holm (or Benjamini–Hochberg) across all reported pooled Study 4 contrasts. Most large effects would survive, so this costs little.
4. Replace the claim of rules being fixed before outcomes were examined with what can be evidenced, such as a dated commit or a timestamped plan, or remove it.

**Severity**: Major
**Confidence**: 4 (the timestamps and family definitions are verified; when the analysis plan was written cannot be checked)

### W5: The expected-value benchmark does not identify "prohibition versus odds" for the severe rules, and is under-specified for the mild ones
**Problem**: The prohibition-versus-odds argument rests on the claim that a risk-neutral agent "should accept" under the mild rules and "should decline" under the severe rules. Four things undermine it.
1. **The severe penalty has no stated value.** Disqualification and loss of all points is never priced in points. At a 1% sting with B = 2, declining requires F > 198 points, which is implausible in a game where scores are in single digits. `c_severe_sting1` may therefore be an "EV says accept" cell, and its 11.5% acceptance would then count as over-deterrence, not compliance.
2. **B is stated by the counterparty.** The value "worth about 2 extra points" is part of the offer, which with probability p comes from the plant itself (`BENEFIT` is appended to the offer in `conditions.py`). A rational agent should discount it under a sting more than under an audit. This affects the sting-versus-audit comparison and the "EV favours accepting" premise.
3. **Benefit and penalty are on different time scales.** B accrues "over the rest of the game", while F is immediate.
4. **Under the mild rules the risk-neutral benchmark predicts no change between 1% and 50%,** because both have positive EV. So "Severity and rate moved acceptance in the direction the benchmark predicts" is not accurate for the rate contrast.

**Evidence Anchor**: text: §3.2 Study 4 "under the severe rules it should decline"
**Why it matters**: The abstract's causal conclusion ("not the odds of being caught") depends on departures from this benchmark. Risk aversion, or distrust of a counterparty's stated B, would produce the same pattern without any rule-following.
**Suggestion**:
1. State the score context so that disqualification can be expressed in points, and recompute which cells EV predicts as accept or decline.
2. Fit a per-model choice model, logit(accept) = α + β·EV + γ·Prohibit + δ·Sting, using the eight or more Study 4 cells. Report β (sensitivity to odds and stakes) against γ (prohibition shift). This tests the abstract's claim directly.
3. Add one arm in which B is stated by the game master rather than the offerer.
4. Add a no-rule risk-preference probe, for example a lottery with the same EV, to separate risk aversion from rule-following.

**Severity**: Major
**Confidence**: 4 (the game-theoretic reasoning is standard; the exact game scores were not inspected for every trial)

### W6: For three models, the Study 4 add-on arms were served by a different provider identifier than their comparators
**Problem**: In `results/main_v4/trials.jsonl`, `served_model` changes for Gemma-3-12B, GPT-4.1-mini and GPT-OSS-120B. The 11 base arms report `google/gemma-3-12b-it`, `openai/gpt-4.1-mini` and `openai/gpt-oss-120b`. The 7 add-on arms (`c_prohibit_p1/p2`, `c_safeharbour_sting50`, `c_auth_*`, `c_auth_*_warned`) report the bare names `gemma-3-12b-it`, `gpt-4.1-mini` and `gpt-oss-120b`, which indicates a different route, and they were run hours later.

The rewording contrasts, the safe-harbour equivalence and the authentication contrasts therefore confound condition with provider (possibly quantisation or serving stack) and with time, for these models. For example, Gemma accepted 4/20 under `c_prohibit` but 11/20 and 14/20 under the two rewordings. That divergence coincides exactly with the provider switch, and it feeds the claim that the prohibition held across three wordings. The paper says every trial logs the served identifier but does not report this switch.

**Evidence Anchor**: dataset: results/main_v4/trials.jsonl — served_model for gemma-3-12b: 'google/gemma-3-12b-it' (base arms) vs 'gemma-3-12b-it' (c_prohibit_p1/p2, c_auth_*, c_safeharbour_sting50)
**Why it matters**: Pairing by context is the design's main strength (S1). For these contrasts it no longer holds, and wording-robustness inferences mix wording with provider.
**Suggestion**: Re-run either the 7 add-on arms or the matched base arms for these 3 models through one provider (about 420 calls), or report the affected contrasts with these three models excluded as a sensitivity check. Add `served_model` and the run batch to Appendix K, and disclose the switch in §3.3.
**Severity**: Major
**Confidence**: 5 (tallied directly from the trial log)

### W7: Parser and judge validity are unestablished, and the error-analysis taxonomy has no human ground truth
**Problem**: The parser–hand agreement and the judge–hand κ are placeholders (a known pending item). Even once they are filled in, three issues remain.
1. **The validation sample cannot be read at face value.** The 96-reply sample is stratified by parsed decision (30/30/30 plus refusals) and labelled by a single rater, the author. Its raw agreement must be reweighted to the population prevalence of each parsed class, and a single rater gives no human reliability estimate.
2. **The failure taxonomy is validated only judge-against-judge.** In Appendix H, κ = 0.80 is the agreement between two LLM judges. No human validates the taxonomy, so κ measures their consistency, not their accuracy.
3. **The categories are interpreted too strongly.** "Ignores rule" means only that the stated reason does not mention the rule. Stated reasons are post hoc, as the paper's own limitation 4 notes, so "A prohibition fails where the model does not read it" overreaches.

The evaluation-awareness lexicon ("0 matches") has unknown recall.

**Evidence Anchor**: text: §3.3 "Parser agreement with hand labels: TBD: %; judge–hand κ: TBD: per judge; judge–judge κ: TBD:"
**Why it matters**: Every outcome passes through the parser, and the mechanism story in §4 rests on the judges' categories.
**Suggestion**:
1. Complete the hand labels and report prevalence-weighted accuracy with Wilson CIs for each parsed class.
2. Hand-label about 60 of the 383 error-analysis replies and report judge-versus-human κ.
3. Rephrase "does not read it" as "does not mention it".
4. Estimate the lexicon's recall on a small seeded set of replies that do express test awareness.

**Severity**: Major (with the hand-label item already known to be pending)
**Confidence**: 4 (methods text and `validation/README.md`; no hand labels exist yet to assess)

### W8: The ±10-point equivalence margin carries no information at a 2–4.5% floor
**Problem**: In RQ1, sting and audit are declared "equivalent within ±10 points" when both arms sit at 2–4.5%. A margin of 10 points would accept a sting that tripled acceptance. No justification for the margin is given.
**Evidence Anchor**: text: §4 RQ1 "Sting and audit were equivalent within ±10 points at 10% (RD +2.5 [+0.0, +6.5], Holm p = 0.39)"
**Why it matters**: The equivalence claim lends confirmatory weight to a comparison the paper itself admits the floor cannot resolve.
**Suggestion**: Use a margin relative to the baseline, for example ±50% of the no-rule rate on the log-odds or risk-ratio scale, or drop the equivalence language for the floor cells and say "both at floor; uninformative".
**Severity**: Minor
**Confidence**: 5

### W9: "A fine is a price" bundles three changes
**Problem**: The crowding-out claim compares `c_prohibit` with `c_mild_sting1`. Those rules differ by three additions: the compliance-agent sentence, an explicit 1% rate and a 1-point fine. The 85–90% acceptance by MiniMax-M3.1 and Qwen3.8-27B could just as well come from quantifying the probability (which invites EV computation; see their reasons in Appendix J) as from attaching a fine.
**Evidence Anchor**: text: §4 RQ2 "accepted 85% and 90% of offers once a 1-point fine was attached, the pattern known in people as "a fine is a price""
**Why it matters**: The mechanism label is a causal attribution that the contrast does not isolate.
**Suggestion**: Add "prohibition + fine, no rate" and "prohibition + rate, no fine" arms for these two models (80 calls), or describe the effect as "a quantified small sanction" rather than "a fine".
**Severity**: Minor
**Confidence**: 4

### W10: The Study 4 prohibition contrast lacks a same-stakes header placebo
**Problem**: `c_prohibit` differs from `c_reportfree` both by the prohibition sentence and by the "HOUSE RULE (announced to all players…)" header (`HOUSE_HEADER` in `conditions.py`). The header-only control (placebo) exists in Studies 2 and 2b, but those use a different offer, without stated stakes.
**Evidence Anchor**: absence: Study 4 condition list (Table 1, Appendix F) — expected a header-only or irrelevant-rule placebo under stated stakes; checked §3.2, Table 1, Appendix F, conditions.py V4_RULES
**Why it matters**: The 2b placebo makes a large header effect unlikely, but the stated-stakes offer may interact with any announced rule.
**Suggestion**: Add `c_placebo` (the late-arrival rule under stated stakes), 200 calls.
**Severity**: Minor
**Confidence**: 4

### W11: Study 5 outcome reporting is selective
**Problem**: System regret is named as a Study 5 outcome (§3.2) but no regret result is reported. In the instructed Jira arm, the prohibition *increased* system regret (+2.6 points [+1.1, +4.1]; this interval excludes 0), and GPT-4.1-mini's coalition advantage roughly doubled (3.75 → 7.60). Neither is mentioned. "Coordination off the secret channel rather than ending it" is inferred from an unchanged advantage, but coordination on the public board is never measured.
**Evidence Anchor**: dataset: results/analysis/colosseum.json — instructed/prohibit_vs_no_rule/regret est +0.026 [+0.011, +0.041]; instructed/gpt-4.1-mini/prohibit adv +7.60
**Why it matters**: The one interval in Study 5 that excludes zero for a welfare outcome is unreported. The mechanism claim (talk moved rather than ended) also lacks a direct measure.
**Suggestion**: Report regret for all arms in an appendix table, together with per-model advantage. Either measure public-board coordination, for example coalition messages naming the partner's ticket, or soften "rather than ending it".
**Severity**: Minor
**Confidence**: 5

### W12: No a priori power analysis or minimum detectable effect, and post hoc subgroup robustness
**Problem**: Cells have n = 20 per model, so a per-model exact McNemar test has roughly 80% power only for discordance differences of 35–40 points. Study 3 rests on 4 "informative" models chosen with the analysed data (P(pass | other) between 0.15 and 0.85). The Llama-3.2-3B exclusion ("every Study 4 effect grows") is a post hoc sensitivity analysis reported only in its favourable direction.
**Evidence Anchor**: absence: Methods §3.3–3.4 and Appendix K — expected a power or MDE statement for per-model and pooled contrasts; checked §3.3, §3.4, §4 Data, Appendix G, Appendix K
**Why it matters**: The per-model "barely responded" and "accepted none" statements, and the Study 3 null, need a power context to be interpretable.
**Suggestion**: Report the MDE for per-model McNemar at n = 20 and for the pooled design. Present the Study 3 all-models ITT as primary, which the paper partly does. Report leave-one-model-out ranges for every headline pooled effect instead of only the Llama-3.2-3B exclusion.
**Severity**: Minor
**Confidence**: 4

### W13: The detector-economics rates mix rule conditions
**Problem**: In Appendix E, collusive acceptance and reporting are taken from the 1% and 5% stings, but the benign report rate is always taken under the 50% sting (100/200), and all of these come from Study 2's prohibition-free wording. A benign report rate measured at 50% overstates false alarms at a 1% plant rate. Precision (46.6%) and the break-even ratio (0.87) are therefore biased downward. They are also not taken from the rule wording that the main text recommends (Studies 2b and 4).
**Evidence Anchor**: table: results/analysis/tables/detector_economics.md — "benign report rate 100/200 under the 50% sting" used for plant_rate 0.001–0.05
**Why it matters**: The deployer recommendation ("over-deterrence is the binding constraint") quotes these numbers.
**Suggestion**: Run the benign proposal under 1% and 5% stings, or present precision as a bound and state the direction of the bias. Recompute with the Study 4 severe and mild rule rates.
**Severity**: Minor
**Confidence**: 4

### W14: Reporting accuracy in the RQ2 and RQ5 text
**Problem**:
- "For six models the sentence alone took acceptance to zero" counts Nemotron, which was already at 0% with no rule (Table 3), so five models moved to zero.
- "Llama-3.2-3B … barely responded": its acceptance rose from 50% to 80% under the prohibition.
- "paired over 240 runs": the no-channel contrast uses 60 seed pairs (120 runs); 240 is the size of the whole emergent arm.
- "Reporting given non-acceptance" (RNA) conditions on a post-treatment outcome, so the comparison is between selected subsets. This is negligible here because acceptance is about 3% in both arms, but it should be noted.

**Evidence Anchor**: table: Table 3 — Nemotron-3.5 Study 4 "none" = 0; Llama-3.2-3B Study 4 none 50 → proh. 80
**Why it matters**: These are small accuracy issues that a careful reader will catch.
**Suggestion**: Change the wording to "five models (a sixth never accepted)" and "Llama-3.2-3B rose from 50% to 80%". Give the pair count as 60 seed pairs. Footnote the conditioning in RNA.
**Severity**: Minor
**Confidence**: 5

---

## Spot-check of headline numbers (claimed vs. found in the repository)

| # | Claim (location) | Claimed | Found (file) | Verdict |
|---|---|---|---|---|
| 1 | No-rule acceptance, Study 2b (Abstract, §4) | 74.4% | 148/199 = 0.744 (`cell_counts.md`, POOLED b_reportfree) | Match |
| 2 | Severe-rule floor (Abstract) | 2–4.5% | b_audit10 2.0%, b_penalty/b_sting50 3.0%, b_audit50 3.5%, b_sting10 4.5% | Match |
| 3 | Prohibition alone, Study 4 (Abstract, §4) | 76.0% → 28.0%, RD −48.0 [−75.5, −18.0] | 152/200 → 56/200; MH RD −0.480 [−0.755, −0.180] (`contrasts.md` S4_prohibit) | Match |
| 4 | Rewordings | 17.5%, 27.5%; RD −58.5, −48.5 | 35/200, 55/200; −0.585, −0.485 | Match |
| 5 | Prohibition removed | 23.0% → 61.0%, +38.0 [+19.0, +56.5] | 46/200 → 122/200; +0.380 [+0.190, +0.565] | Match |
| 6 | Severe vs. mild | −22.5 (1%), −19.5 (50%) | −0.225, −0.195 | Match |
| 7 | Mild sting vs. audit | 23.0 vs 13.5, +9.5 [+1.0, +20.5] | 46 vs 27 of 200; +0.095 [+0.010, +0.205] | Match |
| 8 | Holm p, P10 and RNA50 | 0.39, 0.038 | CMH p 0.129 × 3 = 0.387; 0.00942 × 4 = 0.0377 (family of 4) | Match |
| 9 | Authentication claim | 23.0 → 36.5; 3.5 → 14.0; warned 41.2, 13.1 | 73/200, 28/200, 82/199, 26/199 | Match |
| 10 | Safe harbour (benign) | 87.5% → 70.5%; reports 55.0 → 29.5 | 175/200 and 141/200 non-accept; 110/200 → 59/200 | Match |
| 11 | Study 2b benign over-deterrence | 17.5% vs 84.5–90.5% | b_fair_none 35/200; audit 169, sting 172, penalty 181 of 200 | Match |
| 12 | Total decisions (Abstract) | 10,903 | 1,800 + 2,586 + 2,199 + 3,598 + 720 = 10,903 (Appendix K) | Match |
| 13 | Study 3 ITT (informative) | −3.9 [−7.8, +0.8], 1,803 conversations, 4 informative of 7 | `study3.md`: 1,803 with both plays; 4 informative; 7 with data meeting the roster rule | Match |
| 14 | Error-analysis κ and shares | κ = 0.80; 70% / 22%; 70% prices risk | κ 0.7985; 102/146, 32/146; 145/207 (`error_analysis.json`) | Match |
| 15 | Study 5 instructed sting effect on advantage | −0.0 [−1.9, +1.6] | −0.046 [−1.905, +1.597] (`colosseum.json`) | Match |
| 16 | Study 5 secret-board share | GPT-OSS 78% → 30%; pooled −24.3 [−28.0, −20.7] | 0.783 → 0.302; −0.243 [−0.280, −0.207] | Match |
| 17 | Detector precision at M/N = 1 | 46.6%; break-even 0.87 | 0.466; 0.871 (`detector_economics.md`) | Match (see W13 on the inputs) |
| 18 | "paired over 240 runs" (§4 RQ5) | 240 | Contrast uses 60 pairs; 240 = all emergent runs | Wording mismatch (W14) |

Net: the numbers are faithfully transcribed. The issues in this review concern design, inference and interpretation, not transcription.

---

## Detailed Comments

### Methodology / Research Design
- **Studies 1–4.** These are within-model, context-matched factorial manipulations of rule text, which suits the RQ1–RQ3 causal questions. The weak link is construct validity of the EV benchmark (W5), not internal validity.
- **Study 2b.** The study is informative only about the prohibition-plus-severe-penalty floor; the paper says so.
- **Study 4.** This is the identifying study. Its cleanest contrast is the prohibition removal (S3). The prohibition-only versus no-rule contrast is clean apart from the header (W10).
- **Study 5.** The study is underpowered and lacks the positive control its own logic requires (W1, W2).

### Sampling Strategy
The ten models are a convenience roster weighted toward small open models; four of them are the source paper's. Pooled RDs are therefore averages over this roster and depend on its composition (for example, Nemotron always at 0). This supports the case for stating the estimand (W3). Temperatures differ across models (0.7–0.8), which is harmless within a model but should be noted for cross-model comparisons.

### Data Collection
Retries are content-blind (an empty reply is retried, a decision never is), which is appropriate. A caution: for reasoning models, the trials that exhaust the budget may be the harder decisions, so a retry with a larger budget can shift the conditional distribution. Report the number of retried trials per cell.

### Analysis Methods
See W3 (units of inference), W4 (multiplicity) and W8 (TOST margin). `mh_rd_sato_ci` exists in `stats.py` but is unused. A Sato CI per pooled RD, alongside a model-level interval, would at least show both levels of uncertainty.

### Results Presentation
The results are complete for the one-shot studies. Study 5 omits regret and per-model advantage (W11). Figure 1's bottom panels omit an instructed no-channel reference (W1).

### Reproducibility
Strong (S4). Two gaps: provider routing changed mid-study for three models (W6), and Study 5 depends on a Colosseum checkout via `--sync`. Release the exact Colosseum commit hash and the prompt patch.

### Methodological Fallacies Detected
- **Absence of evidence read as evidence of absence**: Study 5 (W2).
- **Missing positive control or baseline misattribution**: the instructed advantage includes a structural advantage (W1).
- **Uncorrected multiple comparisons in headline claims**: W4.
- **Confounded comparison**: provider switch (W6); a fine bundled with a stated rate (W9).
- **Over-inference from stated reasons**: "does not read it" (W7).

---

## Questions for Authors
1. What is the instructed-arm coalition advantage with no secret channel, per model, on the same seeds? Without it, how is a "kept advantage" separated from the structural advantage visible in the emergent no-channel arm?
2. When were `FAMILIES` in `analyze_all.py` and the 80% roster rule first written, relative to the 12:45 UTC Study 4 start? Is there a dated artefact?
3. What is the value of "disqualified and loses all points" in points at the sampled game states? Which Study 4 cells does a risk-neutral agent then accept?
4. Why did `served_model` change for Gemma-3-12B, GPT-4.1-mini and GPT-OSS-120B between the base arms and the add-on arms, and which provider served each?

---

## Minor Issues

### Figures and Tables
- Table 3: the Nemotron row renders as "00 0005" (column alignment lost). The Study 2b "none" column for Qwen3.8 is 32 on n = 19; flag n < 20 cells.
- Figure 1 (bottom): add the emergent no-channel mean as a reference line in the instructed panels.
- Appendix E, Table 2: the column header layout in the PDF misaligns the precision values.

### Language
- §4 RQ1 has a doubled closing parenthesis in "RD +68.5 [+41.0, +92.0]))".
- The Abstract says "in three wordings" for the prohibition. Note that per-model wording sensitivity is large (Gemma 20% / 55% / 70%), even though the pooled effect holds.

---

## Arithmetic recompute (standard-mode record)
- **p from test statistic / n from df.** The manuscript reports no test statistic with degrees of freedom (only CMH and McNemar p-values and RDs), so neither procedure is computable. Status: not_computable (missing_reported_value).
- **GRIM-type consistency of proportions.** I checked 18 percentages against their stated n (200 or 199): 74.4% = 148/199, 41.2% = 82/199, 13.1% = 26/199, and all n = 200 values are multiples of 0.5%. Status: consistent.
- **Holm adjustments (verified, outside the bounded procedures).** P10: 0.129 × 3 = 0.387 → reported 0.39. RNA50: 0.00942 × 4 = 0.0377 → reported 0.038. Status: consistent.

---

## Criterion-Bound Judgements

Calibration status: `NOT_CALIBRATED`

| Dimension | Criterion source | Judgement | Evidence anchor(s) | Rationale | Uncertainty / scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| Originality | quality_rubrics (not my remit) | NOT_ASSESSED | — | Outside the methodology seat | none identified | no |
| Methodological Rigor | statistical_reporting_standards §1.2–1.5, §4.5; methodology agent Steps 2–4a | PARTLY_MEETS | text: §3.1 pairing (S1); dataset: stats.bootstrap_over_strata (W3); dataset: colosseum.json (W1) | Strong paired design and controls for Studies 1–4; units of inference do not match, Study 5 has no control, and the EV benchmark is not identified | Whether a GLMM reverses any headline is untested; I expect it would not for the large effects | yes; W1, W3 and W5 must be fixed |
| Evidence Sufficiency | methodology agent Step 5 | PARTLY_MEETS | text: Abstract Study 5 claim; table: study2b_primary.md | One-shot claims are well supported numerically; the Study 5 claims are not | n = 20 seeds; positive control absent | yes; W1 and W2 |
| Argument Coherence | methodology agent Step 5 (conclusions vs. data) | PARTLY_MEETS | text: §6 "kept their advantage under every rule, in two environments" vs §4 "gained nothing" | The abstract and conclusion contradict the meeting-scheduling result | none identified | yes |
| Writing Quality | — | NOT_ASSESSED | — | Not my remit | — | no |
| Literature Integration | — | NOT_ASSESSED | — | Reviewer 2's remit | — | no |
| Significance & Impact | — | NOT_ASSESSED | — | Reviewer 3's remit | — | no |
| Statistical reporting completeness | statistical_reporting_standards §6 | PARTLY_MEETS | absence: power/MDE (W12); text: §3.3 TBD (W7) | Effect sizes and CIs are reported throughout; power, validation and confirmatory labelling are missing | Hand labels are pending | yes for W7 once filled |
| Reproducibility | methodology agent Step 6 | MEETS | dataset: results/, scripts/, numbers*.tex (S4) | 18/18 spot-checks reproduce; logs and code released | Provider switch (W6); external Colosseum checkout | no |

**Recommendation rationale.** The open decision-bearing items are:

1. **W1**, the Study 5 positive control. It is Critical but repairable: reframe the claims now and add one instructed no-channel arm.
2. **W3**, inference at mismatched units. It is Major and repairable by re-analysis alone.
3. **W4 and W5**, the confirmatory status of the headline and the identification of the EV benchmark. Both are Major, and both are repairable with relabelling, a choice model and the conversion of disqualification to points.

The one-shot results are likely to survive all of these fixes in direction and rough magnitude. Their framing, and the cross-setting conclusion "deterrence stopped at the single offer", will not survive unchanged.
