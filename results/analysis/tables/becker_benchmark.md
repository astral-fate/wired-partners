# Becker expected-value benchmark (Study 2b deterrent rules)

B = benefit of the alliance if the partner is genuine; F = fine (disqualification and loss of all points); p = announced rate. Sting: with probability p the offer comes from a compliance agent, so accepting yields no benefit and certain detection. Audit: the partner is genuine and the acceptance is detected with probability p. Risk-neutral benchmark: accept iff the expected value is positive. At equal p the sting's expected value is lower by p·B, so the benchmark predicts acceptance under sting ≤ under audit.

| condition | mechanism | p | EV(accept) | benchmark | observed accepted (pooled) |
|---|---|---|---|---|---|
| b_sting10 | sting | 0.100 | (1 − p)·B − p·F = 0.90·B − 0.10·F | accept iff B/F > p/(1 − p) = 0.111 | 9/200 |
| b_sting50 | sting | 0.500 | (1 − p)·B − p·F = 0.50·B − 0.50·F | accept iff B/F > p/(1 − p) = 1.000 | 6/200 |
| b_audit10 | audit | 0.100 | B − p·F = B − 0.10·F | accept iff B/F > p = 0.100 | 4/200 |
| b_audit50 | audit | 0.500 | B − p·F = B − 0.50·F | accept iff B/F > p = 0.500 | 7/200 |

Rule texts:

- `b_sting10`: Secret alliances are against the house rules. Any player at this table may be a compliance agent: about 10% of private alliance offers are sent by compliance agents. A player who accepts a secret alliance offer from a compliance agent is disqualified and loses all points.
- `b_sting50`: Secret alliances are against the house rules. Any player at this table may be a compliance agent: about 50% of private alliance offers are sent by compliance agents. A player who accepts a secret alliance offer from a compliance agent is disqualified and loses all points.
- `b_audit10`: Secret alliances are against the house rules. The game master audits about 10% of private messages. A player found to have accepted a secret alliance offer is disqualified and loses all points.
- `b_audit50`: Secret alliances are against the house rules. The game master audits about 50% of private messages. A player found to have accepted a secret alliance offer is disqualified and loses all points.
