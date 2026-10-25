# Editorial decision: Wired Partners

Panel (25 Oct 2026). Five reviewers in role-separated seats: Journal-Fit (EIC.md), Methodology (R1_methodology.md), Domain (R2_domain.md), Perspective (R3_perspective.md), Devil's Advocate (DA.md). All five ran on the same model family in fresh contexts, with no reviewer seeing another's output, so errors may be correlated. Status: NOT_CALIBRATED.

**Decision: Major Revision** for an archival safety venue. As an Apart sprint report it is strong once the Study 5 claims are rescoped. Recommendations by seat: EIC, Major (Minor as a sprint report); R1, Major; R2, Major; R3, Major; DA, one CRITICAL issue.

## Consensus (3 or more seats)
1. **The Study 5 headline overclaims** (EIC W1, R1 W1, R2 W4, DA C1; R3 indirectly).
   - No collusion emerged without instructions, so "deterrence stopped at the single offer" is untested for the agent the threat model describes.
   - In meeting scheduling there was no advantage to keep.
   - The instructed arm has no no-channel baseline, and part of the "advantage" is structural.
   - Fix: rescope to "rules in the prompt do not bind agents told to collude". Add an instructed arm without a secret channel, or limit the claim to GPT-4.1-mini in Jira.
2. **"Not the odds of being caught" overstates the result** (EIC W3, R2, DA M1). Severity and rate have significant effects. The expected-value benchmark leaves disqualification unpriced and lets an unstated penalty count as zero (R1 W5, R2 W1/W2, DA M3).
   - Fix: say "mostly through the stated prohibition", put disqualification in points, correct the "EV says accept" ticks, and test the prohibition stated with an explicit "no penalty".
3. **The recommendations go beyond the data** (EIC W4, R3 W1/W2, R2): "must be enforced" and "better used to detect" were never tested, and the recommendations don't separate opportunistic agents from instructed ones. Fix: split them by threat and label untested claims as conjecture.

## Majority or single-seat findings with high value
- R1 W9: a provider identifier differs between the added Study 4 arms and the base arms for three models. It coincides with Gemma's rewording jump. Fix: rerun the matched base cells on the same provider.
- R1 W3: the p-values (trial as the unit) and the bootstrap intervals (model as the unit) disagree. Report how many models moved for each effect.
- R1 W4: the abstract's lead effect is outside the Holm families. Label each claim confirmatory or exploratory.
- DA M2: in Appendix B, the 1% severe sting without the prohibition deters as much as the bare prohibition. The body must mention this.
- R3 W3: the rule sits in the operator's prompt header. Add this as a limitation.
- R2: expressive-law and leniency literature is missing. Check each reference before citing it.
- EIC: the Study 5 panel of the figure is unreadable at print size.

## Devil's Advocate CRITICAL issue
C1 (the deterrence-stops claim confounded with instruction): **upheld.** It is corroborated by EIC W1, R1 W1 and R2 W4, and it blocks acceptance until the claim is rescoped.

## Revision roadmap (in source order; triage is the author's)
1. Rescope the Study 5 claims in the abstract, subtitle, results, Discussion and conclusion.
2. Add an instructed no-channel arm (optional; about 60 runs).
3. Add a no-penalty prohibition cell (optional; about 200 calls).
4. Rerun the provider-matched base cells for Gemma-3-12B, GPT-4.1-mini and GPT-OSS-120B.
5. Fix the expected-value benchmark: put disqualification in points and correct the figure ticks.
6. Replace "not the odds of being caught".
7. Split the recommendations by threat.
8. Add the confirmatory or exploratory labels and the count of models moved.
9. Report Appendix B's severe-sting-without-prohibition result in the body.
10. Add the rule-placement limitation.
11. Add verified references.
