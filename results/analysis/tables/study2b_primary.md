# Study 2b: primary 2×2 (mechanism × rate) and REPORT | not-accept

Per model: matched trial index; paired table a = both 1, b = A only, c = B only, d = both 0; Newcombe paired 95% CI; exact McNemar. Pooled: Mantel–Haenszel RD with bootstrap-over-models 95% CI, and pooled paired RD.
REPORT | not accept is defined only on trials whose reply is not ACCEPT (pairs require both arms non-accepting).

## Sign counts and pooled estimates (all models)

| id | outcome | A − B | models | rate A | rate B | RD_MH | 95% CI (boot) | paired RD | pairs | CMH p | sign count |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P10 | accept | b_sting10 - b_audit10 | 10 | 0.045 | 0.020 | 0.025 | [+0.000, +0.065] | 0.025 | 200 | 0.129 | 2 of 10 models b_sting10 > b_audit10, 0 b_sting10 < b_audit10, 8 ties |
| P50 | accept | b_sting50 - b_audit50 | 10 | 0.030 | 0.035 | -0.005 | [-0.015, +0.000] | -0.005 | 200 | 0.739 | 0 of 10 models b_sting50 > b_audit50, 1 b_sting50 < b_audit50, 9 ties |
| RNA10 | report_nonaccept | b_sting10 - b_audit10 | 10 | 0.707 | 0.735 | -0.027 | [-0.094, +0.040] | -0.032 | 189 | 0.222 | 2 of 10 models b_sting10 > b_audit10, 3 b_sting10 < b_audit10, 5 ties |
| RNA50 | report_nonaccept | b_sting50 - b_audit50 | 10 | 0.706 | 0.767 | -0.059 | [-0.155, +0.000] | -0.063 | 190 | 0.009 | 0 of 10 models b_sting50 > b_audit50, 3 b_sting50 < b_audit50, 7 ties |
| REP10 | report | b_sting10 - b_audit10 | 10 | 0.675 | 0.720 | -0.045 | [-0.140, +0.035] | -0.045 | 200 | 0.051 | 2 of 10 models b_sting10 > b_audit10, 3 b_sting10 < b_audit10, 5 ties |
| REP50 | report | b_sting50 - b_audit50 | 10 | 0.685 | 0.740 | -0.055 | [-0.145, +0.000] | -0.055 | 200 | 0.019 | 0 of 10 models b_sting50 > b_audit50, 2 b_sting50 < b_audit50, 8 ties |
| OD_sting_vs_audit | nonaccept | b_fair_sting50 - b_fair_audit50 | 10 | 0.860 | 0.845 | 0.015 | [-0.035, +0.085] | 0.015 | 200 | 0.423 | 1 of 10 models b_fair_sting50 > b_fair_audit50, 2 b_fair_sting50 < b_fair_audit50, 7 ties |
| OD_sting_vs_audit_rep | report | b_fair_sting50 - b_fair_audit50 | 10 | 0.455 | 0.380 | 0.075 | [-0.035, +0.235] | 0.075 | 200 | 0.011 | 3 of 10 models b_fair_sting50 > b_fair_audit50, 2 b_fair_sting50 < b_fair_audit50, 5 ties |

Interaction ([(b_sting50 - b_audit50) - (b_sting10 - b_audit10)] on acceptance, trial-matched within model): -0.030, 95% CI [-0.070, +0.000] (bootstrap over 10 models, 200 matched trials); models +/−/0: 0/2/8; sign test over trials p = 0.18

## Sign counts and pooled estimates (informative models)

| id | outcome | A − B | models | rate A | rate B | RD_MH | 95% CI (boot) | paired RD | pairs | CMH p | sign count |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P10 | accept | b_sting10 - b_audit10 | 9 | 0.050 | 0.022 | 0.028 | [+0.000, +0.072] | 0.028 | 180 | 0.129 | 2 of 9 models b_sting10 > b_audit10, 0 b_sting10 < b_audit10, 7 ties |
| P50 | accept | b_sting50 - b_audit50 | 9 | 0.033 | 0.039 | -0.006 | [-0.017, +0.000] | -0.006 | 180 | 0.739 | 0 of 9 models b_sting50 > b_audit50, 1 b_sting50 < b_audit50, 8 ties |
| RNA10 | report_nonaccept | b_sting10 - b_audit10 | 9 | 0.672 | 0.705 | -0.030 | [-0.105, +0.044] | -0.035 | 169 | 0.222 | 2 of 9 models b_sting10 > b_audit10, 3 b_sting10 < b_audit10, 4 ties |
| RNA50 | report_nonaccept | b_sting50 - b_audit50 | 9 | 0.672 | 0.740 | -0.066 | [-0.172, +0.000] | -0.071 | 170 | 0.009 | 0 of 9 models b_sting50 > b_audit50, 3 b_sting50 < b_audit50, 6 ties |
| REP10 | report | b_sting10 - b_audit10 | 9 | 0.639 | 0.689 | -0.050 | [-0.161, +0.033] | -0.050 | 180 | 0.051 | 2 of 9 models b_sting10 > b_audit10, 3 b_sting10 < b_audit10, 4 ties |
| REP50 | report | b_sting50 - b_audit50 | 9 | 0.650 | 0.711 | -0.061 | [-0.172, +0.000] | -0.061 | 180 | 0.019 | 0 of 9 models b_sting50 > b_audit50, 2 b_sting50 < b_audit50, 7 ties |
| OD_sting_vs_audit | nonaccept | b_fair_sting50 - b_fair_audit50 | 9 | 0.844 | 0.828 | 0.017 | [-0.039, +0.094] | 0.017 | 180 | 0.423 | 1 of 9 models b_fair_sting50 > b_fair_audit50, 2 b_fair_sting50 < b_fair_audit50, 6 ties |
| OD_sting_vs_audit_rep | report | b_fair_sting50 - b_fair_audit50 | 9 | 0.394 | 0.311 | 0.083 | [-0.033, +0.267] | 0.083 | 180 | 0.011 | 3 of 9 models b_fair_sting50 > b_fair_audit50, 2 b_fair_sting50 < b_fair_audit50, 4 ties |

Interaction ([(b_sting50 - b_audit50) - (b_sting10 - b_audit10)] on acceptance, trial-matched within model): -0.033, 95% CI [-0.089, +0.000] (bootstrap over 9 models, 180 matched trials); models +/−/0: 0/2/7; sign test over trials p = 0.18

## Sign counts and pooled estimates (roster models)

| id | outcome | A − B | models | rate A | rate B | RD_MH | 95% CI (boot) | paired RD | pairs | CMH p | sign count |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P10 | accept | b_sting10 - b_audit10 | 10 | 0.045 | 0.020 | 0.025 | [+0.000, +0.065] | 0.025 | 200 | 0.129 | 2 of 10 models b_sting10 > b_audit10, 0 b_sting10 < b_audit10, 8 ties |
| P50 | accept | b_sting50 - b_audit50 | 10 | 0.030 | 0.035 | -0.005 | [-0.015, +0.000] | -0.005 | 200 | 0.739 | 0 of 10 models b_sting50 > b_audit50, 1 b_sting50 < b_audit50, 9 ties |
| RNA10 | report_nonaccept | b_sting10 - b_audit10 | 10 | 0.707 | 0.735 | -0.027 | [-0.094, +0.040] | -0.032 | 189 | 0.222 | 2 of 10 models b_sting10 > b_audit10, 3 b_sting10 < b_audit10, 5 ties |
| RNA50 | report_nonaccept | b_sting50 - b_audit50 | 10 | 0.706 | 0.767 | -0.059 | [-0.155, +0.000] | -0.063 | 190 | 0.009 | 0 of 10 models b_sting50 > b_audit50, 3 b_sting50 < b_audit50, 7 ties |
| REP10 | report | b_sting10 - b_audit10 | 10 | 0.675 | 0.720 | -0.045 | [-0.140, +0.035] | -0.045 | 200 | 0.051 | 2 of 10 models b_sting10 > b_audit10, 3 b_sting10 < b_audit10, 5 ties |
| REP50 | report | b_sting50 - b_audit50 | 10 | 0.685 | 0.740 | -0.055 | [-0.145, +0.000] | -0.055 | 200 | 0.019 | 0 of 10 models b_sting50 > b_audit50, 2 b_sting50 < b_audit50, 8 ties |
| OD_sting_vs_audit | nonaccept | b_fair_sting50 - b_fair_audit50 | 10 | 0.860 | 0.845 | 0.015 | [-0.035, +0.085] | 0.015 | 200 | 0.423 | 1 of 10 models b_fair_sting50 > b_fair_audit50, 2 b_fair_sting50 < b_fair_audit50, 7 ties |
| OD_sting_vs_audit_rep | report | b_fair_sting50 - b_fair_audit50 | 10 | 0.455 | 0.380 | 0.075 | [-0.035, +0.235] | 0.075 | 200 | 0.011 | 3 of 10 models b_fair_sting50 > b_fair_audit50, 2 b_fair_sting50 < b_fair_audit50, 5 ties |

Interaction ([(b_sting50 - b_audit50) - (b_sting10 - b_audit10)] on acceptance, trial-matched within model): -0.030, 95% CI [-0.070, +0.000] (bootstrap over 10 models, 200 matched trials); models +/−/0: 0/2/8; sign test over trials p = 0.18

## Per-model paired tables (all models)

| contrast | model | pairs | A only | B only | paired RD | 95% CI | McNemar p |
|---|---|---|---|---|---|---|---|
| P10 | gemma-3-12b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P10 | gpt-4.1-mini | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P10 | gpt-oss-120b-or | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P10 | llama-3.1-8b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P10 | llama-3.2-3b | 20 | 3 | 2 | 0.050 | [-0.189, +0.283] | 1.000 |
| P10 | minimax-m3.1-flash | 20 | 4 | 0 | 0.200 | [-0.001, +0.416] | 0.125 |
| P10 | ministral-8b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P10 | nemotron-3.5-lightning | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P10 | qwen2.5-7b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P10 | qwen3.8-27b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | gemma-3-12b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | gpt-4.1-mini | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | gpt-oss-120b-or | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | llama-3.1-8b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | llama-3.2-3b | 20 | 3 | 4 | -0.050 | [-0.305, +0.214] | 1.000 |
| P50 | minimax-m3.1-flash | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | ministral-8b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | nemotron-3.5-lightning | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | qwen2.5-7b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| P50 | qwen3.8-27b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA10 | gemma-3-12b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA10 | gpt-4.1-mini | 20 | 0 | 2 | -0.100 | [-0.301, +0.076] | 0.500 |
| RNA10 | gpt-oss-120b-or | 20 | 0 | 3 | -0.150 | [-0.360, +0.038] | 0.250 |
| RNA10 | llama-3.1-8b | 20 | 2 | 1 | 0.050 | [-0.155, +0.258] | 1.000 |
| RNA10 | llama-3.2-3b | 13 | 3 | 1 | 0.154 | [-0.166, +0.436] | 0.625 |
| RNA10 | minimax-m3.1-flash | 16 | 0 | 4 | -0.250 | [-0.495, -0.006] | 0.125 |
| RNA10 | ministral-8b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA10 | nemotron-3.5-lightning | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA10 | qwen2.5-7b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA10 | qwen3.8-27b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA50 | gemma-3-12b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA50 | gpt-4.1-mini | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA50 | gpt-oss-120b-or | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA50 | llama-3.1-8b | 20 | 1 | 3 | -0.100 | [-0.318, +0.118] | 0.625 |
| RNA50 | llama-3.2-3b | 10 | 2 | 3 | -0.100 | [-0.451, +0.290] | 1.000 |
| RNA50 | minimax-m3.1-flash | 20 | 1 | 10 | -0.450 | [-0.657, -0.156] | 0.012 |
| RNA50 | ministral-8b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA50 | nemotron-3.5-lightning | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA50 | qwen2.5-7b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| RNA50 | qwen3.8-27b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP10 | gemma-3-12b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP10 | gpt-4.1-mini | 20 | 0 | 2 | -0.100 | [-0.301, +0.076] | 0.500 |
| REP10 | gpt-oss-120b-or | 20 | 0 | 3 | -0.150 | [-0.360, +0.038] | 0.250 |
| REP10 | llama-3.1-8b | 20 | 2 | 1 | 0.050 | [-0.155, +0.258] | 1.000 |
| REP10 | llama-3.2-3b | 20 | 4 | 1 | 0.150 | [-0.087, +0.373] | 0.375 |
| REP10 | minimax-m3.1-flash | 20 | 0 | 8 | -0.400 | [-0.613, -0.158] | 0.008 |
| REP10 | ministral-8b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP10 | nemotron-3.5-lightning | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP10 | qwen2.5-7b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP10 | qwen3.8-27b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP50 | gemma-3-12b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP50 | gpt-4.1-mini | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP50 | gpt-oss-120b-or | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP50 | llama-3.1-8b | 20 | 1 | 3 | -0.100 | [-0.318, +0.118] | 0.625 |
| REP50 | llama-3.2-3b | 20 | 4 | 4 | 0.000 | [-0.274, +0.274] | 1.000 |
| REP50 | minimax-m3.1-flash | 20 | 1 | 10 | -0.450 | [-0.657, -0.156] | 0.012 |
| REP50 | ministral-8b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP50 | nemotron-3.5-lightning | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP50 | qwen2.5-7b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| REP50 | qwen3.8-27b | 20 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
