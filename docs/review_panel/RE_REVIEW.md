# Re-review (verification): Wired Partners, revised manuscript

Reviewer: verification seat (re-review mode, practical form). Date: 25 Oct 2026.
Inputs: the five round-1 reports and EDITORIAL_DECISION.md in this folder; revised `paper/main.pdf` (20 pp., read in full with `pdftotext -layout`, and pages 5, 7, 19 and 20 rendered); `paper/main.tex` and `numbers*.tex`; `results/analysis/` (cell_counts.csv, colosseum.json, provider_check.json); `results/main_v4/trials.jsonl` and `results/frontier_v4/trials.jsonl` for provider and coverage checks; `git show HEAD:paper/main.tex` for the previous version.
I did not read an author response letter, because none was supplied. Every verdict below rests on the revised manuscript text, checked against the files.

## 1. Verdicts

| Venue | Verdict | Why |
|---|---|---|
| **Apart sprint report (Track 3)** | **Ready after a short text pass (Minor, about 1 hour of rewriting).** | The DA's critical issue and all three consensus issues are resolved. The Study 5 headline has been rescoped and "not the odds" is gone. The recommendations are now split by threat, with conjecture labelled. Two new controls (a rule placebo and the prohibition stated as unenforced) strengthen the main finding. What remains is a few internal contradictions the revision introduced (Section 4, fixes 1–5), a broken row in Table 1, and the pending hand labels. |
| **Archival venue** | **Workshop: Minor Revision. Full conference (SaTML, NeurIPS/ICML safety track): still Major Revision, but no longer for overclaiming.** | The claims now match the evidence. What still limits the paper is the evidence base itself. Study 5 has no positive control, so it cannot test deterrence of collusion that pays (the paper now says so). p-values and intervals are still computed at different units of inference; only per-model significance counts were added, with no hierarchical model. The parser and judge validation are still placeholders. Everything comes from one game. |

**Matrix totals (26 Major/Critical items across the five reports): 21 Addressed, 5 Partly, 0 Not addressed.** One addressed item (R1 W5 / R2 W2, the expected-value benchmark) gained a new internal error in the revision (issue N3). Another (R1 W11, regret) is now reported, but in a way that contradicts the abstract (issue N1).

## 2. Traceability matrix: Major and Critical items

Page numbers refer to the revised PDF. A "quote" is text verified in the PDF.

| # | Item (seat, severity) | Status | Anchor in revised paper (verified) |
|---|---|---|---|
| 1 | DA C1 (Critical): "deterrence stopped at the single offer" is confounded with instruction | **Addressed** | The abstract no longer contains the claim. p.1: "neither uninstructed nor instructed coalitions gained a reliable advantage from a secret channel, so there was little for a rule to deter". p.8, §5 "Tool-using teams": "Study 5 cannot tell whether rules deter collusion that pays … The instructed prompt also names each agent's partner, which weakens the sting's premise". The title has been reworded and the "from Single Offers to Tool-Using Teams" subtitle dropped. |
| 2 | EIC W1 (Major): Study 5 headline overclaims (meetings, three models, two environments) | **Addressed** | p.7, RQ5: "in meeting scheduling it gained nothing in any condition (−0.4 and −0.2 with no rule)". DeepSeek's advantage is now reported ("DeepSeek-V4.1-Flash −0.3"). The phrases "two environments" and "kept their advantage" no longer appear anywhere (grep of PDF and tex). |
| 3 | EIC W2 (Major): instructed arm is outside the threat model | **Addressed** | p.1, §1: "An agent instructed by its principal to collude is a second, stress-test case (Study 5)". p.8: the recommendations have a separate block for "Agents instructed by their principal". |
| 4 | EIC W3 (Major): title and framing put forward the mechanism | **Addressed** | Title: "Prohibitions, Announced Stings and Audits as Deterrents…". Contribution (1) now leads with the prohibition finding (p.2). |
| 5 | EIC W4 (Major): conclusion and recommendations go beyond the data | **Addressed** | p.8: "As conjecture, untested here: enforced or unannounced stings may detect what announced ones do not deter". The governance paragraph is labelled "(from enforcement practice, not our data)". Appendix E, p.13, now states that its rates come from rules without the prohibition sentence and are "indicative and probably conservative". |
| 6 | R1 W1 (Critical): no positive control for the instructed Study 5 arm | **Addressed (by rescoping)** | p.4: "Colosseum gives no coalition instruction without a channel, so these runs are the no-channel baseline for both arms". p.7: "+0.4 [−1.2, +2.1] … There was thus little collusive advantage for a rule to remove". Figure 2 caption, p.7, discloses this. There is no instructed no-channel arm, but the claim is now limited to what the design can show. |
| 7 | R1 W2 (Major): Study 5 nulls read as "no effect" | **Addressed** | p.7: "the rules' effects on advantage are nulls, not shown equivalences". Limitation (2), p.8: "its rule contrasts cannot exclude removal of an advantage of the size observed". No MDE or TOST is given, but the wording route R1 offered has been taken. |
| 8 | R1 W3 (Major): p-values and intervals at different units of inference | **Partly** | p.4, §3.4: "p-values treat trials as the unit and intervals treat models as the unit, so for each headline effect we also report how many of the ten models moved significantly". Counts appear in RQ1, RQ2 and the vouching paragraph. No GLMM or two-stage bootstrap was added, and the CI-includes-0-but-p<0.05 cases remain (RNA50 [−15.5, +0.0], Holm p = 0.038; the unenforced prohibition vs no rule, see N2). |
| 9 | R1 W4 (Major): headline effect is outside the confirmatory families; arms added after base results | **Partly** | Labels are present: p.5–6 carry "exploratory" or "confirmatory" on every RQ2 contrast. The unverifiable "a rule fixed before outcomes were examined" has been removed (it was in the HEAD version). The prohibition-only effect stays exploratory, and the family was not extended. The order in which arms were run is not disclosed. That is acceptable, given the no-history rule for the manuscript. |
| 10 | R1 W5 (Major): EV benchmark not identified for the severe rules | **Addressed, with a new error** | p.2: "Disqualification removes all points, so its F is the agent's current score". p.3: "Under the severe 1% sting accepting is worth it for any F < 198 points … under the severe 50% sting it should decline only if its score exceeds 2". Figure 1 (p.5, rendered) now ticks severe 1% and shows "?" at severe 50%. **But** p.6 says "the benchmark predicts acceptance in all four cells", which contradicts both (see N3). |
| 11 | R1 W6 (Major): provider switch for three models | **Addressed** | p.4, §3.3, and Appendix G (p.15) give provider-matched contrasts. Checked against provider_check.json: p1 matched −0.733 and p2 −0.683. One residue: the body understates Gemma's provider dependence (N5). |
| 12 | R1 W7 (Major): parser and judge validity; "does not read it" | **Partly** | The wording is fixed: p.7 says "never mention the rule". The hand labels are still `\res{}` placeholders (p.4: "Parser agreement with hand labels: TBD"); this is a known pending item. There is no judge-versus-human check of the taxonomy, and no recall estimate for the lexicon. |
| 13 | R2 W1 (Major): prohibition-only does not hold the expected sanction at zero | **Addressed** | A new cell was added, p.6: "with 'Breaking this rule carries no penalty, and nobody checks whether players follow it.' added, acceptance was 69.0%". Both Gneezy–Rustichini readings are now stated (p.6: "This matches both readings of 'a fine is a price'"). |
| 14 | R2 W2 (Major): EV mislabelled for the severe 1% sting | **Addressed, with a new error** | Same anchors as row 10. Kahneman–Tversky [25] is cited at p.6. The "all four cells" slip is N3. |
| 15 | R2 W3 (Major): expressive-law literature missing | **Addressed** | p.3: "In people, a law can move behaviour beyond its sanction [9]: removing a duty with only symbolic fines lowered turnout [13], and obligations raise contributions with incentives held fixed [14]". The references carry DOIs. McAdams is not cited, which is acceptable. |
| 16 | R2 W4 (Major): Study 5 unsupported for the threat-model agent | **Addressed** | Same anchors as rows 1 and 3. Gans & Holden is used for displacement (p.8). |
| 17 | R3 W1 (Major): recommendations target the wrong threat | **Addressed** | p.8: "Opportunistic agents, with the rule in the agent's instructions (supported by Studies 2b and 4): (1)…" and "Agents instructed by their principal: …". The §1 rationale is also there: "as when a principal delegates broadly and does not anticipate side offers". |
| 18 | R3 W2 (Major): entrapment and attribution | **Addressed** | p.8: "an accepted plant shows susceptibility to inducement rather than a prior intent to collude [22]. Never sanction on one accepted plant; require corroboration (repeated acceptance across independent plants, action-level evidence), sanction a principal only on knowledge or instruction". Appendix M(3), p.18: "Our over-deterrence probes measure the cost to benign cooperation, not the rate of such false catches". |
| 19 | R3 W3 (Major): rule placement | **Addressed** | Limitation (1), p.8: "Real platforms deliver terms as third-party content … delivery as platform content is untested". The recommendations are qualified with "with the rule in the agent's instructions". |
| 20 | DA M1 (Major): "not the odds" contradicted by significant effects | **Addressed** | p.6: "Severity and rate also moved acceptance, but not as expected value requires … (Holm p < 0.001, < 0.001; confirmatory; 3 models each)". "Not the odds" no longer appears. |
| 21 | DA M2 (Major): Study 2 shows deterrence without a prohibition, absent from the body | **Addressed** | p.5, RQ1: "Without the prohibition sentence (Study 2, stakes unstated), a 1% severe sting alone cut acceptance from 72.9% to 27.5% … a stated sanction deters without a prohibition". The point is also built into the Discussion (p.7). |
| 22 | DA M3 (Major): benchmark sets F = 0 for the bare prohibition; B is taken as true | **Addressed** | p.3: "The bare prohibition states no penalty, so the benchmark is undetermined" (Figure 1 shows "?"). The unenforced cell tests F = 0 directly. Limitation (4): "B is stated by the sender, who may be the plant". |
| 23 | DA M4 (Major): pooling hides a bimodal split | **Partly** | p.5–6: "The effect is bimodal: six models fell to zero, while Llama-3.1-8B and Ministral-8B barely responded and Llama-3.2-3B rose from 50% to 80%". The abstract and conclusion still speak of "agents" generally, with no "most models" qualifier. |
| 24 | DA M5 (Major): "over-deterrence is the binding constraint" rests on one trivial benign proposal | **Addressed** | "binding constraint" has been removed. Limitation (3): "The benign proposal is an easy case; over-deterrence of ambiguous lawful cooperation is likely larger". |
| 25 | DA M6 (Major): Study 5 null is underpowered | **Addressed** | Same anchors as row 7. |
| 26 | DA M7 (Major): a parlour game's house rules generalised to marketplaces | **Partly** | Limitation (1) says "single decisions in one game", and the recommendations are scoped to opportunistic agents with the rule in their instructions. Nothing notes that Studies 1–4 have no principal or profit pressure. |

### Minor items: brief status
- EIC W5: Study 5 figure. **Addressed.** It is now a full-width Figure 2 with the message-share row and legible at print size (p.7, rendered).
- EIC W6: numbering. **Partly.** One sentence in §3.1 now explains Studies 1 and 2; the "2b" label and the 2b/4/3/5 order remain.
- EIC W7: instruction-following as an alternative account. **Partly.** The new rule placebo and the unenforced cell partly settle it, but the alternative is never named.
- EIC W8 and R2 W9e: talks cited as sources. **Not addressed.** This is fine for the sprint. [40] is still the untitled "HackTalk: Khanh Linh Nguyen" and still supports a substantive claim (p.8).
- R1 W8: ±10-point margin at the floor. **Partly.** "though at a floor this margin is weakly informative".
- R1 W9: a fine bundled with a rate. **Partly.** The body now says "a quantified sanction"; the abstract still says "a small fine became a price".
- R1 W10: header placebo under stated stakes. **Addressed.** The new `c_rule_placebo` cell gives 79.9%, equivalent within ±10.
- R1 W11: regret not reported. **Addressed, but it creates contradiction N1.**
- R1 W12: power and MDE. **Not addressed.**
- R1 W13: detector-economics inputs. **Addressed** by an explicit caveat in Appendix E.
- R1 W14: "240 runs" is now "60 seed pairs"; Llama-3.2-3B is now reported as "rose from 50% to 80%". **Addressed.** On "six models fell to zero", Nemotron's no-rule rate is 5% (`study4/cell/c_reportfree/m/nemotron` = 5), so the sentence is literally true. The round-1 objection came from the garbled text extraction of Table 3.
- R2 W5: reconciliation with [7]. **Partly.** The Discussion now cites [7, 16, 40], but Shi et al. ("Emergent Collusion in Long-Horizon…") is still in the bib and uncited.
- R2 W6: leniency theory. **Not addressed.** This is optional.
- R2 W7: the pB gap under disqualification. **Addressed** (p.2).
- R2 W8: Nagin's certainty versus severity. **Addressed** (p.8).
- R2 W10: model heterogeneity in the abstract. **Partly** (see row 23).
- R3 W4: displacement. **Addressed** (p.8).
- R3 W5: "a fine is a price" as a recommendation. **Addressed** (recommendation 2).
- R3 W6: an easy benign case. **Addressed.** Platform self-interest and shill plants: **not addressed.**
- R3 W7: heterogeneity and admission tests. **Partly.**
- DA m1: **Addressed.** DA m2: **Partly**, via Limitation (5). DA m3: **Moot** (Nemotron was at 5%). DA m4: **Addressed** ("pair with monitoring" removed). DA m5: **Addressed** (rule placebo). DA m6: **Partly.**

## 3. Headline numbers: claimed against found

| # | Claim (location) | Claimed | Found | Verdict |
|---|---|---|---|---|
| 1 | Decisions (abstract, contribution 1) | 11,302 | `total/decisions` = 11,302; Appendix L gives 1,800 + 2,586 + 2,199 + 3,997 + 720 = 11,302 | Match |
| 2 | Study 2b no rule, then the floor (abstract, RQ1) | 74.4%, then 2.0–4.5% | cell_counts.csv: 148/199 = 0.744; b_audit10 4/200 = 0.020; b_sting10 9/200 = 0.045 | Match |
| 3 | Prohibition only (abstract, RQ2) | 76.0% to 28.0%, RD −48.0 [−75.5, −18.0], 6 of 10 models | 152/200 to 56/200; macros rd −48.0, lo −75.5, hi −18.0, nsig/neg 6 | Match |
| 4 | Prohibition stated as unenforced (abstract, RQ2) | 69.0%; +41.0 [+16.5, +65.5] vs the bare prohibition; −7.0 [−29.5, +12.5] vs no rule; 4 models | 138/200 = 0.690; S4_nopenalty_vs_base +41.0 [+16.5, +65.5], nsig/pos 4; S4_nopenalty −7.0 [−29.5, +12.5] | Match, **but** the same macro file gives CMH p = 0.048 and nsig/neg = 2 for "vs no rule" (see N2) |
| 5 | Rule placebo (RQ2) | 79.9%, +3.7 [−1.5, +11.0], equivalent | 159/199 = 0.799; 90% CI [−1.3, +9.7], tost "equivalent" | Match |
| 6 | Prohibition removed (RQ2) | 23.0% to 61.0%, +38.0 [+19.0, +56.5], 5 models | 46/200 to 122/200; macros +38.0 [+19.0, +56.5], Holm < 0.001, nsig/pos 5 | Match |
| 7 | Severity and rate (RQ2) | −22.5, −19.5 (3 models each); −11.0 [−21.5, −2.0], Holm p = 0.001 | S4_sev_mild_1 −22.5, S4_sev_mild_50 −19.5, nsig 3 each; S4_mild_rate −11.0 [−21.5, −2.0], Holm = 0.001, nsig 0 | Match |
| 8 | Study 5, uninstructed channel vs no channel (RQ5) | +0.0 [−1.4, +1.4], 60 pairs | colosseum.json est 0.028 [−1.355, +1.413]; pairs 60 | Match |
| 9 | Study 5, instructed vs no channel (RQ5) | +0.4 [−1.2, +2.1]; +1.4 / −0.0 / −0.3 | est 0.377 [−1.227, +2.070]; per-model macros +1.4 / −0.0 / −0.3 | Match |
| 10 | Study 5, sting effect on secret-board share (RQ5) | −24.3 [−28.0, −20.7]; GPT-OSS 78% to 30%; DeepSeek 60% to 36% | est −0.2429 [−0.2800, −0.2068]; macros 78/30 and 60/36 | Match |
| 11 | Study 5 regret under the prohibition (RQ5) | +2.6 points [+1.1, +4.1]; GPT-4.1-mini +6.7 | est 0.0257 [0.0107, 0.0408] | Match in value. The unit is a fraction ×100, i.e. percentage points of regret, not reward "points" like advantage |
| 12 | Meetings, no rule (RQ5) | −0.4, −0.2 | −0.358, −0.167 | Match |
| 13 | Provider-matched rewordings (§4 robustness, App. G) | −73.3, −68.3; Gemma 20% vs 95% | provider_check.json: p1/matched −0.733, p2/matched −0.683; per-model Gemma −0.45 / −0.30 | Match |
| 14 | Error analysis (§4) | 383 replies, κ = 0.80, 70% / 22% / 70% | err/n 383, kappa 0.80, 70 / 22 / 70 | Match |

Result: 14 of 14 match the macros and results files. Nothing was mistranscribed. The problems below are about interpretation.

## 4. New issues introduced by the revision

**N1. "Without changing outcomes" contradicts the regret result (Major for consistency).** The abstract (p.1) says rules "moved coordination off the watched channel without changing outcomes". The RQ5 heading (p.6) is "rules moved the talk, not the outcome". §5 (p.8) and the Conclusion (p.8) say the same. Yet p.7 reports "The prohibition also raised system regret in the instructed arm (+2.6 points [+1.1, +4.1]…)". That interval excludes zero, and regret is a declared Study 5 outcome (§3.2). The claim holds for coalition advantage only.

**N2. The abstract and conclusion state the mechanism more firmly than the Discussion and the data allow (Major).**
- The abstract says "A bare prohibition deters mostly because agents read it as implying enforcement." The conclusion says agents decline "mostly because a prohibition implies that the act will be sanctioned".
- §5 (p.8) concedes: "The unenforced wording may also signal that the rule is not meant seriously; our design cannot separate an imputed sanction from perceived seriousness."
- The abstract also says the unenforced sentence "restored it to 69.0%". RQ2 says the cell is "not detectably different from no rule". But the trial-level test in numbers.tex is CMH p = 0.048, and 2 models (Qwen2.5-7B at 15%, Gemma-3-12B at 45%) stay significantly below no rule.
- The result is strong as it stands; it only needs to be stated as "most of", with the alternative reading kept.

**N3. "The benchmark predicts acceptance in all four cells" is wrong by the paper's own benchmark (Major for correctness, a one-line fix).** At p.6, the four cells are mild and severe at 1% and 50%. §3.2 (p.3) says that under the severe 50% sting a risk-neutral agent "should decline only if its score exceeds 2". Figure 1 marks that cell "?". So the benchmark predicts acceptance in three cells; the fourth depends on the agent's score.

**N4. "Watched" and "monitored" channel, and "coordination" (Minor to Major).** The abstract, §5 and the Conclusion say "off the watched channel"; the recommendations say "displaced coordination from the monitored channel". In Study 5 no channel is watched: the rule is "announced, never enforced" (p.4). What was measured is the share of messages, not coordination (R1 W11). The displacement also held for 2 of 3 models (GPT-4.1-mini went from 73% to 71%), yet the abstract states it without a qualifier.

**N5. The body understates Gemma's provider dependence (Minor to Major).** §4 robustness (p.7) says "only the comparison of the rewordings with the original wording depends on provider". Appendix G (p.15) shows that Gemma-3-12B accepted 20% under the bare prohibition on OpenRouter and 95% on Experiential Labs. Gemma's response to the headline prohibition sentence therefore depends on provider: it is one of the "6 of 10 models significant" on OpenRouter only. The same sentence also uses development-history wording: "served by a second provider in the **added arms**".

**N6. The GPT-6-Luna coverage claim is false (Minor).** §3.3 (p.4) says it "was run as a frontier check on every Study 2b and 4 condition (20 trials each)". `results/frontier_v4/trials.jsonl` has 14 of the 20 Study 4 conditions. It lacks `c_rule_placebo`, `c_prohibit_nopenalty`, `c_prohibit_p1/p2` and both `_warned` arms. Study 2b coverage is complete (11 of 11).

**N7. Table 1 is broken by the new rows (Minor, visible).** In main.tex line 176, `\cond{c\_rule\_placebo} & Same-length house rule that prohibits nothing \` ends with `\ ` instead of `\\`. On p.19 this merges the two rows: `c_prohibit_nopenalty` lands in the description column and "Prohibition stated as unpenalised and unchecked" lands in the left column. Line 184 (`c_auth_…(_warned)`) also overprints its description; main.log shows "Overfull \hbox (41.89pt too wide) … lines 184--184".

**N8. Smaller new or residual wording issues.**
- The abstract says "Under a severe penalty every rule cut acceptance". The severe-penalty placebo is a rule and left acceptance at 71.5%; RQ1 correctly says "Every rule that stated the prohibition and the severe penalty".
- Contribution (3) promises "a hand-validated parser", but the validation numbers are still TBD.
- Recommendation (4) ("do not rely on a sting where counterparties can vouch for themselves") rests on an exploratory effect in 2 models, yet sits under "(supported by Studies 2b and 4)".
- The governance paragraph is labelled "(from enforcement practice, not our data)" but quotes our 76.0%.
- p.8: "It extends expressive effects of law…" has a dangling "It".
- p.4: missing space in "evaluation language.The author".
- Instructed recommendation: "no rule we tested had collusive gains to remove" reads as if the rule had the gains.
- Appendix I (p.16) says "Every reply that accepted … under a rule in Study 4 (383 replies)". Read literally, that would include the unenforced (138) and placebo (159) acceptances. The body correctly says "(other than the unenforced prohibition)".
- The new Study 4 cells were served under the identifier `nvidia/nemotron-3.5-lightning`, while Nemotron's base cells used `nemotron-3.5-lightning` (trials.jsonl). Nemotron accepted 10% under the unenforced prohibition, against 5% with no rule. The effect is negligible, but §3.3 says every switch is disclosed.
- Qwen3.8-27B accepted 75% under the unenforced prohibition, against 35% with no rule. "Acceptance returned" understates that it overshot the no-rule rate.
- Table 3 has no columns for the two new Study 4 cells, which RQ2 discusses per model.

**Stale phrases from the old story: none left.** Searches of the PDF and tex for "kept their advantage", "obey", "stopped/stops at the single offer", "two environments", "three models", "binding constraint", "not the odds", "better used to detect", "fixed before outcomes" return nothing.

**Development-history wording.** One instance in the body: "in the added arms" (p.7, see N5). "Rerun the same command" in Figure 3 describes the resumable harness, not the paper's history, and is fine. "Declared earlier this round" in Appendix H is game content.

**Sign check.** All reported signs agree with the macros: rate −11.0, sting vs audit +9.5, vouching +13.5 and +10.5, regret +2.6, secret share −14.0 and −24.3.

## 5. Format gates

| Gate | Result |
|---|---|
| Body ≤ 8 pages, References start p.9 | **Pass.** The Conclusion ends on p.8 and References begin on p.9. |
| Abstract 150–250 words | **Pass.** 225 words, citation markers included. |
| Appendix "Limitations and Dual-Use / Ethical Considerations" | **Pass.** Appendix M, p.17–18. |
| LLM usage statement | **Pass.** Appendix N, p.18. |
| No `??` (undefined references) | **Pass.** No `??` in the PDF text and no undefined-reference warnings in main.log. |
| Placeholders | **Pending author labels.** There are three `\res{}` markers in one sentence (§3.3, p.4): parser agreement %, judge–hand κ, and judge–judge κ. They render in red as "TBD:". The first two need the author's hand labels. The third (judge–judge κ on the validation sample) can be computed without them. |
| Figures legible | **Pass.** Figure 2 is readable. In Figure 1 the left panel is small but readable at 100%. |
| Tables | **Fail (cosmetic).** Table 1 row merge and overprint (N7). There is also an overfull box in the Appendix I table (16 pt). |

## 6. Remaining fixes: rewriting only, ranked by value

1. **Remove the "without changing outcomes" contradiction (N1, N4).**
   - Abstract, last sentence. Replace "rules in the prompt moved coordination off the watched channel without changing outcomes." with: "rules in the prompt moved an instructed coalition's messages off the secret channel (two of three models) without changing its advantage."
   - RQ5 heading (p.6). Replace "rules moved the talk, not the outcome" with "rules moved the talk, not the coalition's advantage".
   - §5 "Tool-using teams". Replace "moved instructed coordination off the watched channel without changing outcomes" with "moved instructed coalitions' messages off the secret channel without changing their advantage (the prohibition raised system regret)".
   - Conclusion. Replace "rules moved coordination off the watched channel without changing outcomes" with "rules moved an instructed coalition's messages off the secret channel without changing its advantage".
   - Recommendations. Replace "displaced coordination from the monitored channel" with "displaced messages from the channel the rule targeted".

2. **State the mechanism at the strength the data support (N2).**
   - Abstract. Replace "adding that breaking the rule carries no penalty and nobody checks restored it to 69.0%. A bare prohibition deters mostly because agents read it as implying enforcement." with: "adding that breaking the rule carries no penalty and nobody checks brought it back to 69.0%. Most of a bare prohibition's effect depends on the enforcement agents read into it, or on the rule being meant seriously."
   - Conclusion, first clause. Replace "mostly because a prohibition implies that the act will be sanctioned" with "mostly because a prohibition marks the act as one that will be sanctioned or is meant seriously".
   - RQ2. Replace "and not detectably different from no rule (−7.0 [−29.5, +12.5]; exploratory)" with "and 7.0 points below no rule (−7.0 [−29.5, +12.5], trial-level p = 0.048; exploratory)".

3. **Fix the benchmark slip (N3).** On p.6, replace "Yet the benchmark predicts acceptance in all four cells:" with "Yet the benchmark predicts acceptance in three of the four cells, and in the fourth (severe 50%) for agents scoring 2 or less:".

4. **Report Gemma's provider dependence in the body and drop the history wording (N5).** On p.7, replace "For the three models served by a second provider in the added arms, provider-matched contrasts leave the rewordings' effect against no rule intact (−73.3 and −68.3 points) and the safe-harbour and vouching contrasts unchanged; only the comparison of the rewordings with the original wording depends on provider (Appendix G)." with:
   "For the three models whose rewording, safe-harbour and vouching arms were served by a second provider, provider-matched contrasts leave the rewordings' effect against no rule intact (−73.3 and −68.3 points) and the safe-harbour and vouching contrasts unchanged. Gemma-3-12B's response to the original wording depends on provider (20% vs 95% acceptance under the bare prohibition; Appendix G)."

5. **Correct the GPT-6-Luna coverage (N6).** In §3.3, replace "was run as a frontier check on every Study 2b and 4 condition (20 trials each)" with "was run as a frontier check on every Study 2b condition and the 14 main Study 4 conditions (20 trials each)".

6. **Repair Table 1 (N7).** On main.tex line 176, change the trailing `\ ` to `\\`. On line 184, use `\cond{c\_auth\_\{mild,severe\}\_sting50},\newline\cond{\dots\_warned}`, or widen the first column, to end the overprint.

7. **Abstract scope words (N8, row 23).**
   - Replace "Under a severe penalty every rule cut acceptance" with "Under a severe penalty every deterrent rule cut acceptance".
   - Replace "for two models a small fine became a price" with "for two models a small stated fine became a price".
   - Optionally add after "28.0%": "(six of ten models; three barely responded)". Check the word count stays ≤ 250 (currently 225).

8. **Label the exploratory recommendation.** Replace "(4) do not rely on a sting where counterparties can vouch for themselves." with "(4) do not rely on a sting where counterparties can vouch for themselves (exploratory; two models)."

9. **Fix the governance wording.** Replace "Governance (from enforcement practice, not our data): a plant originates the offer, and 76.0% of agents accept one with no rule, so…" with "Governance (drawn from enforcement practice): a plant originates the offer, and 76.0% of our agents accepted such an offer with no rule, so…".

10. **Fix the instructed recommendation.** Replace "no rule we tested had collusive gains to remove" with "there were no reliable collusive gains for any tested rule to remove".

11. **Regret units.** Replace "(+2.6 points [+1.1, +4.1], mostly GPT-4.1-mini, +6.7)" with "(+2.6 percentage points of regret [+1.1, +4.1], mostly GPT-4.1-mini, +6.7)".

12. **Make contribution (3) conditional on the labels.** If the hand labels are not in by submission, replace "a hand-validated parser and every log" with "a parser with a hand-validation protocol, and every log". Delete the TBD sentence rather than submit red placeholders.

13. **Small edits.**
    - p.8: replace "It extends expressive effects of law" with "This extends expressive effects of law".
    - p.4: change "language.The" to "language. The".
    - Appendix I: replace "under a rule in Study 4 (383 replies)" with "under a deterrent rule in Study 4, excluding the unenforced prohibition (383 replies)".
    - RQ2: after "Acceptance returned for 4 models individually (…)", add "; Qwen3.8-27B rose above its no-rule rate (75% vs 35%)".
    - §3.3: after "every trial logs the model identifier served", add ", and Nemotron-3.5's served identifier differs between the base and the later Study 4 cells".

14. **Optional, for the archival version.** Name instruction-following as the competing account in §5 and say that the unenforced cell argues against pure instruction-following. Cite Shi et al. (long-horizon emergent collusion, already in the bib) next to [7, 16]. Replace the untitled talk [40] with its underlying paper.

## 7. What still needs more than rewriting (archival only)
- **Hierarchical inference.** A logistic GLMM or a two-stage bootstrap so that p-values and intervals share one unit of inference (R1 W3).
- **Hand labels.** Parser accuracy (prevalence-weighted) and a judge-versus-human κ on about 60 error-analysis replies (R1 W7).
- **A Study 5 positive control.** A setting where the secret channel produces a measurable advantage, or an enforced sting, so that deterrence of collusion that pays can be tested at all.
- **A principal-pressure or third-party-delivery cell for the prohibition** (DA M7, R3 W3).
