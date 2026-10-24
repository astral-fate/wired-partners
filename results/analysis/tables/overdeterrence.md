# Over-deterrence of the benign private proposal

Rates: Wilson 95% CI. Contrasts: MH RD with bootstrap-over-models CIs, paired RD on matched trials; TOST ±0.10 uses the 90% bootstrap CI.

## Study 2

| level | rule | condition | n | nonaccept | nonaccept_rate | nonaccept_lo | nonaccept_hi | report | report_rate | report_lo | report_hi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| POOLED | none | n_fair_private | 200 | 32 | 0.160 | 0.116 | 0.217 | 27 | 0.135 | 0.095 | 0.189 |
| POOLED | audit50 | n_fair_private_audit50 | 200 | 167 | 0.835 | 0.777 | 0.880 | 55 | 0.275 | 0.218 | 0.341 |
| POOLED | penalty | n_fair_private_penalty | 200 | 177 | 0.885 | 0.833 | 0.922 | 75 | 0.375 | 0.311 | 0.444 |
| POOLED | sting50 | n_fair_private_sting50 | 200 | 192 | 0.960 | 0.923 | 0.980 | 100 | 0.500 | 0.431 | 0.569 |
| gemma-3-12b | none | n_fair_private | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gemma-3-12b | audit50 | n_fair_private_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| gemma-3-12b | penalty | n_fair_private_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 2 | 0.100 | 0.028 | 0.301 |
| gemma-3-12b | sting50 | n_fair_private_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| gpt-4.1-mini | none | n_fair_private | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gpt-4.1-mini | audit50 | n_fair_private_audit50 | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gpt-4.1-mini | penalty | n_fair_private_penalty | 20 | 16 | 0.800 | 0.584 | 0.919 | 5 | 0.250 | 0.112 | 0.469 |
| gpt-4.1-mini | sting50 | n_fair_private_sting50 | 20 | 13 | 0.650 | 0.433 | 0.819 | 0 | 0.000 | 0.000 | 0.161 |
| gpt-oss-120b-or | none | n_fair_private | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gpt-oss-120b-or | audit50 | n_fair_private_audit50 | 20 | 9 | 0.450 | 0.258 | 0.658 | 2 | 0.100 | 0.028 | 0.301 |
| gpt-oss-120b-or | penalty | n_fair_private_penalty | 20 | 13 | 0.650 | 0.433 | 0.819 | 4 | 0.200 | 0.081 | 0.416 |
| gpt-oss-120b-or | sting50 | n_fair_private_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 9 | 0.450 | 0.258 | 0.658 |
| llama-3.1-8b | none | n_fair_private | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| llama-3.1-8b | audit50 | n_fair_private_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| llama-3.1-8b | penalty | n_fair_private_penalty | 20 | 16 | 0.800 | 0.584 | 0.919 | 0 | 0.000 | 0.000 | 0.161 |
| llama-3.1-8b | sting50 | n_fair_private_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| llama-3.2-3b | none | n_fair_private | 20 | 10 | 0.500 | 0.299 | 0.701 | 6 | 0.300 | 0.145 | 0.519 |
| llama-3.2-3b | audit50 | n_fair_private_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 9 | 0.450 | 0.258 | 0.658 |
| llama-3.2-3b | penalty | n_fair_private_penalty | 20 | 16 | 0.800 | 0.584 | 0.919 | 9 | 0.450 | 0.258 | 0.658 |
| llama-3.2-3b | sting50 | n_fair_private_sting50 | 20 | 19 | 0.950 | 0.764 | 0.991 | 15 | 0.750 | 0.531 | 0.888 |
| minimax-m3.1-flash | none | n_fair_private | 20 | 1 | 0.050 | 0.009 | 0.236 | 0 | 0.000 | 0.000 | 0.161 |
| minimax-m3.1-flash | audit50 | n_fair_private_audit50 | 20 | 19 | 0.950 | 0.764 | 0.991 | 3 | 0.150 | 0.052 | 0.360 |
| minimax-m3.1-flash | penalty | n_fair_private_penalty | 20 | 16 | 0.800 | 0.584 | 0.919 | 10 | 0.500 | 0.299 | 0.701 |
| minimax-m3.1-flash | sting50 | n_fair_private_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 3 | 0.150 | 0.052 | 0.360 |
| ministral-8b | none | n_fair_private | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| ministral-8b | audit50 | n_fair_private_audit50 | 20 | 19 | 0.950 | 0.764 | 0.991 | 1 | 0.050 | 0.009 | 0.236 |
| ministral-8b | penalty | n_fair_private_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 5 | 0.250 | 0.112 | 0.469 |
| ministral-8b | sting50 | n_fair_private_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 13 | 0.650 | 0.433 | 0.819 |
| nemotron-3.5-lightning | none | n_fair_private | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| nemotron-3.5-lightning | audit50 | n_fair_private_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| nemotron-3.5-lightning | penalty | n_fair_private_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| nemotron-3.5-lightning | sting50 | n_fair_private_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| qwen2.5-7b | none | n_fair_private | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| qwen2.5-7b | audit50 | n_fair_private_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| qwen2.5-7b | penalty | n_fair_private_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| qwen2.5-7b | sting50 | n_fair_private_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| qwen3.8-27b | none | n_fair_private | 20 | 1 | 0.050 | 0.009 | 0.236 | 1 | 0.050 | 0.009 | 0.236 |
| qwen3.8-27b | audit50 | n_fair_private_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| qwen3.8-27b | penalty | n_fair_private_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| qwen3.8-27b | sting50 | n_fair_private_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |

| id | population | outcome | A − B | RD_MH | 95% CI | 90% CI | TOST equivalent | paired RD | paired 95% CI |
|---|---|---|---|---|---|---|---|---|---|
| H4 | all | nonaccept | n_fair_private_sting50 - n_fair_private | 0.800 | [+0.580, +0.975] | [+0.620, +0.950] | False | 0.800 | [+0.580, +0.975] |
| H4 | informative | nonaccept | n_fair_private_sting50 - n_fair_private | 0.889 | [+0.750, +0.989] | [+0.772, +0.989] | False | 0.889 | [+0.750, +0.989] |
| H4 | roster | nonaccept | n_fair_private_sting50 - n_fair_private | 0.800 | [+0.580, +0.975] | [+0.620, +0.950] | False | 0.800 | [+0.580, +0.975] |
| H4_audit | all | nonaccept | n_fair_private_audit50 - n_fair_private | 0.675 | [+0.425, +0.900] | [+0.475, +0.870] | False | 0.675 | [+0.425, +0.900] |
| H4_audit | informative | nonaccept | n_fair_private_audit50 - n_fair_private | 0.750 | [+0.522, +0.956] | [+0.550, +0.922] | False | 0.750 | [+0.522, +0.956] |
| H4_audit | roster | nonaccept | n_fair_private_audit50 - n_fair_private | 0.675 | [+0.425, +0.900] | [+0.475, +0.870] | False | 0.675 | [+0.425, +0.900] |
| H4_penalty | all | nonaccept | n_fair_private_penalty - n_fair_private | 0.725 | [+0.510, +0.900] | [+0.545, +0.875] | False | 0.725 | [+0.510, +0.900] |
| H4_penalty | informative | nonaccept | n_fair_private_penalty - n_fair_private | 0.806 | [+0.656, +0.933] | [+0.678, +0.917] | False | 0.806 | [+0.656, +0.933] |
| H4_penalty | roster | nonaccept | n_fair_private_penalty - n_fair_private | 0.725 | [+0.510, +0.900] | [+0.545, +0.875] | False | 0.725 | [+0.510, +0.900] |
| H4_sting_vs_audit | all | nonaccept | n_fair_private_sting50 - n_fair_private_audit50 | 0.125 | [+0.000, +0.295] | [+0.005, +0.255] | False | 0.125 | [+0.000, +0.295] |
| H4_sting_vs_audit | informative | nonaccept | n_fair_private_sting50 - n_fair_private_audit50 | 0.139 | [+0.000, +0.322] | [+0.006, +0.283] | False | 0.139 | [+0.000, +0.322] |
| H4_sting_vs_audit | roster | nonaccept | n_fair_private_sting50 - n_fair_private_audit50 | 0.125 | [+0.000, +0.295] | [+0.005, +0.255] | False | 0.125 | [+0.000, +0.295] |
| H4_sting_vs_penalty | all | nonaccept | n_fair_private_sting50 - n_fair_private_penalty | 0.075 | [-0.005, +0.160] | [+0.005, +0.145] | False | 0.075 | [-0.005, +0.160] |
| H4_sting_vs_penalty | informative | nonaccept | n_fair_private_sting50 - n_fair_private_penalty | 0.083 | [-0.011, +0.178] | [+0.006, +0.161] | False | 0.083 | [-0.011, +0.178] |
| H4_sting_vs_penalty | roster | nonaccept | n_fair_private_sting50 - n_fair_private_penalty | 0.075 | [-0.005, +0.160] | [+0.005, +0.145] | False | 0.075 | [-0.005, +0.160] |
| H4_report | all | report | n_fair_private_sting50 - n_fair_private | 0.365 | [+0.150, +0.605] | [+0.175, +0.560] | False | 0.365 | [+0.150, +0.605] |
| H4_report | informative | report | n_fair_private_sting50 - n_fair_private | 0.406 | [+0.167, +0.656] | [+0.200, +0.611] | False | 0.406 | [+0.167, +0.656] |
| H4_report | roster | report | n_fair_private_sting50 - n_fair_private | 0.365 | [+0.150, +0.605] | [+0.175, +0.560] | False | 0.365 | [+0.150, +0.605] |
| H4_sting_vs_audit_report | all | report | n_fair_private_sting50 - n_fair_private_audit50 | 0.225 | [+0.035, +0.435] | [+0.065, +0.400] | False | 0.225 | [+0.035, +0.435] |
| H4_sting_vs_audit_report | informative | report | n_fair_private_sting50 - n_fair_private_audit50 | 0.250 | [+0.067, +0.483] | [+0.072, +0.439] | False | 0.250 | [+0.067, +0.483] |
| H4_sting_vs_audit_report | roster | report | n_fair_private_sting50 - n_fair_private_audit50 | 0.225 | [+0.035, +0.435] | [+0.065, +0.400] | False | 0.225 | [+0.035, +0.435] |
| H4_sting_vs_penalty_report | all | report | n_fair_private_sting50 - n_fair_private_penalty | 0.125 | [-0.070, +0.340] | [-0.045, +0.305] | False | 0.125 | [-0.070, +0.340] |
| H4_sting_vs_penalty_report | informative | report | n_fair_private_sting50 - n_fair_private_penalty | 0.139 | [-0.078, +0.378] | [-0.044, +0.339] | False | 0.139 | [-0.078, +0.378] |
| H4_sting_vs_penalty_report | roster | report | n_fair_private_sting50 - n_fair_private_penalty | 0.125 | [-0.070, +0.340] | [-0.045, +0.305] | False | 0.125 | [-0.070, +0.340] |

## Study 2b

| level | rule | condition | n | nonaccept | nonaccept_rate | nonaccept_lo | nonaccept_hi | report | report_rate | report_lo | report_hi |
|---|---|---|---|---|---|---|---|---|---|---|---|
| POOLED | none | b_fair_none | 200 | 35 | 0.175 | 0.129 | 0.234 | 32 | 0.160 | 0.116 | 0.217 |
| POOLED | audit50 | b_fair_audit50 | 200 | 169 | 0.845 | 0.788 | 0.889 | 76 | 0.380 | 0.316 | 0.449 |
| POOLED | penalty | b_fair_penalty | 200 | 181 | 0.905 | 0.856 | 0.938 | 70 | 0.350 | 0.287 | 0.418 |
| POOLED | sting50 | b_fair_sting50 | 200 | 172 | 0.860 | 0.805 | 0.901 | 91 | 0.455 | 0.388 | 0.524 |
| gemma-3-12b | none | b_fair_none | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gemma-3-12b | audit50 | b_fair_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 5 | 0.250 | 0.112 | 0.469 |
| gemma-3-12b | penalty | b_fair_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| gemma-3-12b | sting50 | b_fair_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| gpt-4.1-mini | none | b_fair_none | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gpt-4.1-mini | audit50 | b_fair_audit50 | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gpt-4.1-mini | penalty | b_fair_penalty | 20 | 17 | 0.850 | 0.640 | 0.948 | 7 | 0.350 | 0.181 | 0.567 |
| gpt-4.1-mini | sting50 | b_fair_sting50 | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gpt-oss-120b-or | none | b_fair_none | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| gpt-oss-120b-or | audit50 | b_fair_audit50 | 20 | 10 | 0.500 | 0.299 | 0.701 | 2 | 0.100 | 0.028 | 0.301 |
| gpt-oss-120b-or | penalty | b_fair_penalty | 20 | 14 | 0.700 | 0.481 | 0.855 | 3 | 0.150 | 0.052 | 0.360 |
| gpt-oss-120b-or | sting50 | b_fair_sting50 | 20 | 16 | 0.800 | 0.584 | 0.919 | 4 | 0.200 | 0.081 | 0.416 |
| llama-3.1-8b | none | b_fair_none | 20 | 1 | 0.050 | 0.009 | 0.236 | 0 | 0.000 | 0.000 | 0.161 |
| llama-3.1-8b | audit50 | b_fair_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| llama-3.1-8b | penalty | b_fair_penalty | 20 | 15 | 0.750 | 0.531 | 0.888 | 0 | 0.000 | 0.000 | 0.161 |
| llama-3.1-8b | sting50 | b_fair_sting50 | 20 | 19 | 0.950 | 0.764 | 0.991 | 0 | 0.000 | 0.000 | 0.161 |
| llama-3.2-3b | none | b_fair_none | 20 | 13 | 0.650 | 0.433 | 0.819 | 11 | 0.550 | 0.342 | 0.742 |
| llama-3.2-3b | audit50 | b_fair_audit50 | 20 | 19 | 0.950 | 0.764 | 0.991 | 9 | 0.450 | 0.258 | 0.658 |
| llama-3.2-3b | penalty | b_fair_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 9 | 0.450 | 0.258 | 0.658 |
| llama-3.2-3b | sting50 | b_fair_sting50 | 20 | 17 | 0.850 | 0.640 | 0.948 | 8 | 0.400 | 0.219 | 0.613 |
| minimax-m3.1-flash | none | b_fair_none | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| minimax-m3.1-flash | audit50 | b_fair_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 4 | 0.200 | 0.081 | 0.416 |
| minimax-m3.1-flash | penalty | b_fair_penalty | 20 | 15 | 0.750 | 0.531 | 0.888 | 10 | 0.500 | 0.299 | 0.701 |
| minimax-m3.1-flash | sting50 | b_fair_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 1 | 0.050 | 0.009 | 0.236 |
| ministral-8b | none | b_fair_none | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| ministral-8b | audit50 | b_fair_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 16 | 0.800 | 0.584 | 0.919 |
| ministral-8b | penalty | b_fair_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 1 | 0.050 | 0.009 | 0.236 |
| ministral-8b | sting50 | b_fair_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 18 | 0.900 | 0.699 | 0.972 |
| nemotron-3.5-lightning | none | b_fair_none | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| nemotron-3.5-lightning | audit50 | b_fair_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| nemotron-3.5-lightning | penalty | b_fair_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| nemotron-3.5-lightning | sting50 | b_fair_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| qwen2.5-7b | none | b_fair_none | 20 | 0 | 0.000 | 0.000 | 0.161 | 0 | 0.000 | 0.000 | 0.161 |
| qwen2.5-7b | audit50 | b_fair_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| qwen2.5-7b | penalty | b_fair_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| qwen2.5-7b | sting50 | b_fair_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 0 | 0.000 | 0.000 | 0.161 |
| qwen3.8-27b | none | b_fair_none | 20 | 1 | 0.050 | 0.009 | 0.236 | 1 | 0.050 | 0.009 | 0.236 |
| qwen3.8-27b | audit50 | b_fair_audit50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| qwen3.8-27b | penalty | b_fair_penalty | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |
| qwen3.8-27b | sting50 | b_fair_sting50 | 20 | 20 | 1.000 | 0.839 | 1.000 | 20 | 1.000 | 0.839 | 1.000 |

| id | population | outcome | A − B | RD_MH | 95% CI | 90% CI | TOST equivalent | paired RD | paired 95% CI |
|---|---|---|---|---|---|---|---|---|---|
| OD_sting | all | nonaccept | b_fair_sting50 - b_fair_none | 0.685 | [+0.410, +0.920] | [+0.460, +0.880] | False | 0.685 | [+0.410, +0.920] |
| OD_sting | informative | nonaccept | b_fair_sting50 - b_fair_none | 0.761 | [+0.500, +0.967] | [+0.550, +0.956] | False | 0.761 | [+0.500, +0.967] |
| OD_sting | roster | nonaccept | b_fair_sting50 - b_fair_none | 0.685 | [+0.410, +0.920] | [+0.460, +0.880] | False | 0.685 | [+0.410, +0.920] |
| OD_audit | all | nonaccept | b_fair_audit50 - b_fair_none | 0.670 | [+0.405, +0.905] | [+0.450, +0.880] | False | 0.670 | [+0.405, +0.905] |
| OD_audit | informative | nonaccept | b_fair_audit50 - b_fair_none | 0.744 | [+0.500, +0.978] | [+0.533, +0.928] | False | 0.744 | [+0.500, +0.978] |
| OD_audit | roster | nonaccept | b_fair_audit50 - b_fair_none | 0.670 | [+0.405, +0.905] | [+0.450, +0.880] | False | 0.670 | [+0.405, +0.905] |
| OD_penalty | all | nonaccept | b_fair_penalty - b_fair_none | 0.730 | [+0.520, +0.900] | [+0.555, +0.875] | False | 0.730 | [+0.520, +0.900] |
| OD_penalty | informative | nonaccept | b_fair_penalty - b_fair_none | 0.811 | [+0.672, +0.933] | [+0.694, +0.917] | False | 0.811 | [+0.672, +0.933] |
| OD_penalty | roster | nonaccept | b_fair_penalty - b_fair_none | 0.730 | [+0.520, +0.900] | [+0.555, +0.875] | False | 0.730 | [+0.520, +0.900] |
| OD_sting_vs_audit | all | nonaccept | b_fair_sting50 - b_fair_audit50 | 0.015 | [-0.035, +0.085] | [-0.030, +0.075] | True | 0.015 | [-0.035, +0.085] |
| OD_sting_vs_audit | informative | nonaccept | b_fair_sting50 - b_fair_audit50 | 0.017 | [-0.039, +0.094] | [-0.033, +0.083] | True | 0.017 | [-0.039, +0.094] |
| OD_sting_vs_audit | roster | nonaccept | b_fair_sting50 - b_fair_audit50 | 0.015 | [-0.035, +0.085] | [-0.030, +0.075] | True | 0.015 | [-0.035, +0.085] |
| OD_sting_rep | all | report | b_fair_sting50 - b_fair_none | 0.295 | [+0.045, +0.575] | [+0.080, +0.515] | False | 0.295 | [+0.045, +0.575] |
| OD_sting_rep | informative | report | b_fair_sting50 - b_fair_none | 0.328 | [+0.056, +0.644] | [+0.094, +0.572] | False | 0.328 | [+0.056, +0.644] |
| OD_sting_rep | roster | report | b_fair_sting50 - b_fair_none | 0.295 | [+0.045, +0.575] | [+0.080, +0.515] | False | 0.295 | [+0.045, +0.575] |
| OD_audit_rep | all | report | b_fair_audit50 - b_fair_none | 0.220 | [+0.030, +0.450] | [+0.050, +0.405] | False | 0.220 | [+0.030, +0.450] |
| OD_audit_rep | informative | report | b_fair_audit50 - b_fair_none | 0.244 | [+0.033, +0.494] | [+0.061, +0.450] | False | 0.244 | [+0.033, +0.494] |
| OD_audit_rep | roster | report | b_fair_audit50 - b_fair_none | 0.220 | [+0.030, +0.450] | [+0.050, +0.405] | False | 0.220 | [+0.030, +0.450] |
| OD_penalty_rep | all | report | b_fair_penalty - b_fair_none | 0.190 | [+0.020, +0.395] | [+0.045, +0.360] | False | 0.190 | [+0.020, +0.395] |
| OD_penalty_rep | informative | report | b_fair_penalty - b_fair_none | 0.211 | [+0.028, +0.439] | [+0.050, +0.400] | False | 0.211 | [+0.028, +0.439] |
| OD_penalty_rep | roster | report | b_fair_penalty - b_fair_none | 0.190 | [+0.020, +0.395] | [+0.045, +0.360] | False | 0.190 | [+0.020, +0.395] |
| OD_sting_vs_audit_rep | all | report | b_fair_sting50 - b_fair_audit50 | 0.075 | [-0.035, +0.235] | [-0.025, +0.210] | False | 0.075 | [-0.035, +0.235] |
| OD_sting_vs_audit_rep | informative | report | b_fair_sting50 - b_fair_audit50 | 0.083 | [-0.033, +0.267] | [-0.028, +0.239] | False | 0.083 | [-0.033, +0.267] |
| OD_sting_vs_audit_rep | roster | report | b_fair_sting50 - b_fair_audit50 | 0.075 | [-0.035, +0.235] | [-0.025, +0.210] | False | 0.075 | [-0.035, +0.235] |
