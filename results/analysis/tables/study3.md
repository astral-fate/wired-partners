# Study 3: follow-through favouritism

F = P(pass | plant) − P(pass | other) within trial (paired). ITT DiD = trial-matched mean of [d(condition) − d(control)], d = pass_plant − pass_other; pooled over matched trials, CI by bootstrap over models.

## Study 3 (v2)

Data `results/main_v3b/trials.jsonl`; 2040 trial keys, 1803 with both plays observed. Floor/ceiling rule: P(pass | other) over all conditions < 0.15 or > 0.85.

| model | keys | turn1_error | both_plays_observed | n | p_pass_other | status |
|---|---|---|---|---|---|---|
| gemma-3-12b | 120 | 0 | 120 | 120 | 0.000 | floor |
| gpt-4.1-mini | 120 | 0 | 120 | 120 | 0.975 | ceiling |
| gpt-oss-120b-or | 360 | 0 | 360 | 360 | 0.792 | informative |
| llama-3.1-8b | 360 | 0 | 360 | 360 | 0.236 | informative |
| llama-3.2-3b | 120 | 0 | 120 | 120 | 0.033 | floor |
| ministral-8b | 360 | 0 | 360 | 360 | 0.825 | informative |
| nemotron-3.5-lightning | 120 | 0 | 0 | 0 |  | no data |
| qwen2.5-7b | 360 | 0 | 360 | 360 | 0.297 | informative |
| qwen3.8-27b | 120 | 52 | 3 | 3 | 1.000 | ceiling |

### Favouritism per model × condition

| model | condition | n | turn-1 accept | P(pass|plant) | P(pass|other) | plant-only pass | other-only pass | F | 95% CI (paired) | McNemar p |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma-3-12b | b_reportfree | 30 | 30 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.114, +0.114] | 1.000 |
| gemma-3-12b | b_audit50 | 30 | 0 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.114, +0.114] | 1.000 |
| gemma-3-12b | b_sting50 | 30 | 0 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.114, +0.114] | 1.000 |
| gemma-3-12b | b_fair_none | 30 | 30 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.114, +0.114] | 1.000 |
| gpt-4.1-mini | b_reportfree | 30 | 30 | 1.000 | 0.967 | 1 | 0 | 0.033 | [-0.083, +0.167] | 1.000 |
| gpt-4.1-mini | b_audit50 | 30 | 0 | 0.933 | 0.933 | 2 | 2 | 0.000 | [-0.158, +0.158] | 1.000 |
| gpt-4.1-mini | b_sting50 | 30 | 0 | 1.000 | 1.000 | 0 | 0 | 0.000 | [-0.114, +0.114] | 1.000 |
| gpt-4.1-mini | b_fair_none | 30 | 30 | 0.967 | 1.000 | 0 | 1 | -0.033 | [-0.167, +0.083] | 1.000 |
| gpt-oss-120b-or | b_reportfree | 90 | 67 | 0.922 | 0.833 | 14 | 6 | 0.089 | [-0.009, +0.188] | 0.115 |
| gpt-oss-120b-or | b_audit50 | 90 | 0 | 0.756 | 0.800 | 11 | 15 | -0.044 | [-0.157, +0.069] | 0.557 |
| gpt-oss-120b-or | b_sting50 | 90 | 0 | 0.811 | 0.767 | 18 | 14 | 0.044 | [-0.079, +0.166] | 0.597 |
| gpt-oss-120b-or | b_fair_none | 90 | 90 | 0.822 | 0.767 | 13 | 8 | 0.056 | [-0.047, +0.158] | 0.383 |
| llama-3.1-8b | b_reportfree | 90 | 88 | 0.211 | 0.289 | 15 | 22 | -0.078 | [-0.206, +0.054] | 0.324 |
| llama-3.1-8b | b_audit50 | 90 | 0 | 0.200 | 0.222 | 13 | 15 | -0.022 | [-0.139, +0.095] | 0.851 |
| llama-3.1-8b | b_sting50 | 90 | 0 | 0.200 | 0.178 | 16 | 14 | 0.022 | [-0.098, +0.141] | 0.856 |
| llama-3.1-8b | b_fair_none | 90 | 89 | 0.267 | 0.256 | 18 | 17 | 0.011 | [-0.117, +0.139] | 1.000 |
| llama-3.2-3b | b_reportfree | 30 | 14 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.114, +0.114] | 1.000 |
| llama-3.2-3b | b_audit50 | 30 | 6 | 0.000 | 0.033 | 0 | 1 | -0.033 | [-0.167, +0.083] | 1.000 |
| llama-3.2-3b | b_sting50 | 30 | 11 | 0.067 | 0.033 | 1 | 0 | 0.033 | [-0.093, +0.173] | 1.000 |
| llama-3.2-3b | b_fair_none | 30 | 9 | 0.100 | 0.067 | 2 | 1 | 0.033 | [-0.119, +0.191] | 1.000 |
| ministral-8b | b_reportfree | 90 | 89 | 1.000 | 0.967 | 3 | 0 | 0.033 | [-0.013, +0.093] | 0.250 |
| ministral-8b | b_audit50 | 90 | 0 | 0.844 | 0.744 | 18 | 9 | 0.100 | [-0.015, +0.212] | 0.122 |
| ministral-8b | b_sting50 | 90 | 0 | 0.878 | 0.833 | 15 | 11 | 0.044 | [-0.068, +0.156] | 0.557 |
| ministral-8b | b_fair_none | 90 | 90 | 0.856 | 0.756 | 16 | 7 | 0.100 | [-0.006, +0.205] | 0.093 |
| nemotron-3.5-lightning | b_reportfree | 0 | 0 |  |  | 0 | 0 |  |  |  |
| nemotron-3.5-lightning | b_audit50 | 0 | 0 |  |  | 0 | 0 |  |  |  |
| nemotron-3.5-lightning | b_sting50 | 0 | 0 |  |  | 0 | 0 |  |  |  |
| nemotron-3.5-lightning | b_fair_none | 0 | 0 |  |  | 0 | 0 |  |  |  |
| qwen2.5-7b | b_reportfree | 90 | 90 | 0.044 | 0.089 | 4 | 8 | -0.044 | [-0.128, +0.035] | 0.388 |
| qwen2.5-7b | b_audit50 | 90 | 0 | 0.478 | 0.422 | 27 | 22 | 0.056 | [-0.095, +0.203] | 0.568 |
| qwen2.5-7b | b_sting50 | 90 | 0 | 0.600 | 0.533 | 26 | 20 | 0.067 | [-0.079, +0.209] | 0.461 |
| qwen2.5-7b | b_fair_none | 90 | 90 | 0.133 | 0.144 | 10 | 11 | -0.011 | [-0.114, +0.092] | 1.000 |
| qwen3.8-27b | b_reportfree | 3 | 3 | 1.000 | 1.000 | 0 | 0 | 0.000 | [-0.561, +0.561] | 1.000 |
| qwen3.8-27b | b_audit50 | 0 | 0 |  |  | 0 | 0 |  |  |  |
| qwen3.8-27b | b_sting50 | 0 | 0 |  |  | 0 | 0 |  |  |  |
| qwen3.8-27b | b_fair_none | 0 | 11 |  |  | 0 | 0 |  |  |  |

### Pooled (all models)

| condition | models | trials | plant-only | other-only | F | 95% CI (boot) | McNemar p |
|---|---|---|---|---|---|---|---|
| b_reportfree | 8 | 453 | 37 | 36 | 0.002 | [-0.046, +0.053] | 1.000 |
| b_audit50 | 7 | 450 | 71 | 64 | 0.016 | [-0.029, +0.060] | 0.606 |
| b_sting50 | 7 | 450 | 76 | 59 | 0.038 | [+0.021, +0.051] | 0.168 |
| b_fair_none | 7 | 450 | 59 | 45 | 0.031 | [-0.003, +0.064] | 0.202 |

- ITT DiD F(b_reportfree) - F(b_fair_none): -0.029, 95% CI [-0.064, +0.015] (bootstrap over 7 models, 450 matched trials); models +/−/0: 2/4/1; sign test over trials p = 0.302
  - per model: gemma-3-12b +0.000 [+0.000, +0.000] (n=30); gpt-4.1-mini +0.067 [-0.028, +0.161] (n=30); gpt-oss-120b-or +0.033 [-0.102, +0.168] (n=90); llama-3.1-8b -0.089 [-0.279, +0.101] (n=90); llama-3.2-3b -0.033 [-0.153, +0.086] (n=30); ministral-8b -0.067 [-0.170, +0.036] (n=90); nemotron-3.5-lightning n=0; qwen2.5-7b -0.033 [-0.161, +0.094] (n=90); qwen3.8-27b n=0
- ITT DiD F(b_audit50) - F(b_fair_none): -0.016, 95% CI [-0.062, +0.031] (bootstrap over 7 models, 450 matched trials); models +/−/0: 2/3/2; sign test over trials p = 0.821
  - per model: gemma-3-12b +0.000 [+0.000, +0.000] (n=30); gpt-4.1-mini +0.033 [-0.121, +0.188] (n=30); gpt-oss-120b-or -0.100 [-0.251, +0.051] (n=90); llama-3.1-8b -0.033 [-0.207, +0.140] (n=90); llama-3.2-3b -0.067 [-0.203, +0.070] (n=30); ministral-8b +0.000 [-0.160, +0.160] (n=90); nemotron-3.5-lightning n=0; qwen2.5-7b +0.067 [-0.141, +0.275] (n=90); qwen3.8-27b n=0
- ITT DiD F(b_sting50) - F(b_fair_none): +0.007, 95% CI [-0.027, +0.045] (bootstrap over 7 models, 450 matched trials); models +/−/0: 3/2/2; sign test over trials p = 0.882
  - per model: gemma-3-12b +0.000 [+0.000, +0.000] (n=30); gpt-4.1-mini +0.033 [-0.035, +0.102] (n=30); gpt-oss-120b-or -0.011 [-0.173, +0.150] (n=90); llama-3.1-8b +0.011 [-0.186, +0.208] (n=90); llama-3.2-3b +0.000 [-0.139, +0.139] (n=30); ministral-8b -0.056 [-0.223, +0.112] (n=90); nemotron-3.5-lightning n=0; qwen2.5-7b +0.078 [-0.095, +0.250] (n=90); qwen3.8-27b n=0

### Pooled (informative models)

| condition | models | trials | plant-only | other-only | F | 95% CI (boot) | McNemar p |
|---|---|---|---|---|---|---|---|
| b_reportfree | 4 | 360 | 36 | 36 | 0.000 | [-0.061, +0.061] | 1.000 |
| b_audit50 | 4 | 360 | 69 | 61 | 0.022 | [-0.033, +0.078] | 0.539 |
| b_sting50 | 4 | 360 | 75 | 59 | 0.044 | [+0.028, +0.061] | 0.195 |
| b_fair_none | 4 | 360 | 57 | 43 | 0.039 | [+0.000, +0.078] | 0.193 |

- ITT DiD F(b_reportfree) - F(b_fair_none): -0.039, 95% CI [-0.078, +0.008] (bootstrap over 4 models, 360 matched trials); models +/−/0: 1/3/0; sign test over trials p = 0.254
  - per model: gpt-oss-120b-or +0.033 [-0.102, +0.168] (n=90); llama-3.1-8b -0.089 [-0.279, +0.101] (n=90); ministral-8b -0.067 [-0.170, +0.036] (n=90); qwen2.5-7b -0.033 [-0.161, +0.094] (n=90)
- ITT DiD F(b_audit50) - F(b_fair_none): -0.017, 95% CI [-0.075, +0.042] (bootstrap over 4 models, 360 matched trials); models +/−/0: 1/2/1; sign test over trials p = 0.877
  - per model: gpt-oss-120b-or -0.100 [-0.251, +0.051] (n=90); llama-3.1-8b -0.033 [-0.207, +0.140] (n=90); ministral-8b +0.000 [-0.160, +0.160] (n=90); qwen2.5-7b +0.067 [-0.141, +0.275] (n=90)
- ITT DiD F(b_sting50) - F(b_fair_none): +0.006, 95% CI [-0.039, +0.056] (bootstrap over 4 models, 360 matched trials); models +/−/0: 2/2/0; sign test over trials p = 0.94
  - per model: gpt-oss-120b-or -0.011 [-0.173, +0.150] (n=90); llama-3.1-8b +0.011 [-0.186, +0.208] (n=90); ministral-8b -0.056 [-0.223, +0.112] (n=90); qwen2.5-7b +0.078 [-0.095, +0.250] (n=90)

### Descriptive split by turn-1 decision (post-treatment; not causal)

| condition | turn1 | n | p_pass_plant | p_pass_other | F | mcnemar_p |
|---|---|---|---|---|---|---|
| b_reportfree | ACCEPT | 410 | 0.507 | 0.500 | 0.007 | 0.807 |
| b_reportfree | not ACCEPT | 43 | 0.488 | 0.535 | -0.046 | 0.688 |
| b_audit50 | ACCEPT | 6 | 0.000 | 0.000 | 0.000 | 1.000 |
| b_audit50 | not ACCEPT | 444 | 0.525 | 0.509 | 0.016 | 0.606 |
| b_sting50 | ACCEPT | 11 | 0.000 | 0.000 | 0.000 | 1.000 |
| b_sting50 | not ACCEPT | 439 | 0.583 | 0.544 | 0.039 | 0.168 |
| b_fair_none | ACCEPT | 428 | 0.507 | 0.477 | 0.030 | 0.237 |
| b_fair_none | not ACCEPT | 22 | 0.091 | 0.045 | 0.045 | 1.000 |

## Study 3 pilot (v1; no benign control, random states)

Data `results/main_v3/trials.jsonl`; 435 trial keys, 414 with both plays observed. Floor/ceiling rule: P(pass | other) over all conditions < 0.15 or > 0.85.

| model | keys | turn1_error | both_plays_observed | n | p_pass_other | status |
|---|---|---|---|---|---|---|
| gemma-3-12b | 60 | 0 | 60 | 60 | 0.000 | floor |
| gpt-4.1-mini | 60 | 0 | 60 | 60 | 0.500 | informative |
| gpt-oss-120b-or | 60 | 0 | 54 | 54 | 0.630 | informative |
| llama-3.1-8b | 60 | 0 | 60 | 60 | 0.050 | floor |
| llama-3.2-3b | 60 | 0 | 60 | 60 | 0.000 | floor |
| ministral-8b | 60 | 0 | 60 | 60 | 0.067 | floor |
| qwen2.5-7b | 60 | 0 | 60 | 60 | 0.250 | informative |
| qwen3.8-27b | 15 | 15 | 0 | 0 |  | no data |

### Favouritism per model × condition

| model | condition | n | turn-1 accept | P(pass|plant) | P(pass|other) | plant-only pass | other-only pass | F | 95% CI (paired) | McNemar p |
|---|---|---|---|---|---|---|---|---|---|---|
| gemma-3-12b | n_reportfree | 20 | 20 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| gemma-3-12b | n_audit50 | 20 | 0 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| gemma-3-12b | n_sting50 | 20 | 0 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| gpt-4.1-mini | n_reportfree | 20 | 20 | 1.000 | 0.600 | 8 | 0 | 0.400 | [+0.158, +0.613] | 0.008 |
| gpt-4.1-mini | n_audit50 | 20 | 0 | 0.550 | 0.550 | 1 | 1 | 0.000 | [-0.156, +0.156] | 1.000 |
| gpt-4.1-mini | n_sting50 | 20 | 0 | 0.500 | 0.350 | 3 | 0 | 0.150 | [-0.031, +0.312] | 0.250 |
| gpt-oss-120b-or | n_reportfree | 20 | 15 | 0.950 | 0.650 | 6 | 0 | 0.300 | [+0.058, +0.518] | 0.031 |
| gpt-oss-120b-or | n_audit50 | 19 | 0 | 0.368 | 0.737 | 3 | 10 | -0.368 | [-0.627, -0.011] | 0.092 |
| gpt-oss-120b-or | n_sting50 | 15 | 0 | 0.667 | 0.467 | 5 | 2 | 0.200 | [-0.141, +0.484] | 0.453 |
| llama-3.1-8b | n_reportfree | 20 | 20 | 0.100 | 0.050 | 2 | 1 | 0.050 | [-0.155, +0.258] | 1.000 |
| llama-3.1-8b | n_audit50 | 20 | 0 | 0.100 | 0.100 | 2 | 2 | 0.000 | [-0.221, +0.221] | 1.000 |
| llama-3.1-8b | n_sting50 | 20 | 0 | 0.100 | 0.000 | 2 | 0 | 0.100 | [-0.076, +0.301] | 0.500 |
| llama-3.2-3b | n_reportfree | 20 | 12 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| llama-3.2-3b | n_audit50 | 20 | 5 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| llama-3.2-3b | n_sting50 | 20 | 9 | 0.000 | 0.000 | 0 | 0 | 0.000 | [-0.161, +0.161] | 1.000 |
| ministral-8b | n_reportfree | 20 | 20 | 0.350 | 0.200 | 6 | 3 | 0.150 | [-0.138, +0.408] | 0.508 |
| ministral-8b | n_audit50 | 20 | 0 | 0.150 | 0.000 | 3 | 0 | 0.150 | [-0.038, +0.360] | 0.250 |
| ministral-8b | n_sting50 | 20 | 1 | 0.100 | 0.000 | 2 | 0 | 0.100 | [-0.076, +0.301] | 0.500 |
| qwen2.5-7b | n_reportfree | 20 | 20 | 0.650 | 0.300 | 8 | 1 | 0.350 | [+0.064, +0.563] | 0.039 |
| qwen2.5-7b | n_audit50 | 20 | 4 | 0.100 | 0.250 | 1 | 4 | -0.150 | [-0.380, +0.094] | 0.375 |
| qwen2.5-7b | n_sting50 | 20 | 10 | 0.100 | 0.200 | 2 | 4 | -0.100 | [-0.339, +0.150] | 0.688 |
| qwen3.8-27b | n_reportfree | 0 | 0 |  |  | 0 | 0 |  |  |  |

### Pooled (all models)

| condition | models | trials | plant-only | other-only | F | 95% CI (boot) | McNemar p |
|---|---|---|---|---|---|---|---|
| n_reportfree | 7 | 140 | 30 | 5 | 0.179 | [+0.064, +0.293] | 2.24e-05 |
| n_audit50 | 7 | 139 | 10 | 17 | -0.050 | [-0.175, +0.043] | 0.248 |
| n_sting50 | 7 | 135 | 14 | 6 | 0.059 | [-0.014, +0.128] | 0.115 |

- Contrast vs reference (pilot) F(n_audit50) - F(n_reportfree): -0.230, 95% CI [-0.435, -0.057] (bootstrap over 7 models, 139 matched trials); models +/−/0: 0/4/3; sign test over trials p = 0.000198
  - per model: gemma-3-12b +0.000 [+0.000, +0.000] (n=20); gpt-4.1-mini -0.400 [-0.719, -0.082] (n=20); gpt-oss-120b-or -0.684 [-1.111, -0.258] (n=19); llama-3.1-8b -0.050 [-0.333, +0.233] (n=20); llama-3.2-3b +0.000 [+0.000, +0.000] (n=20); ministral-8b +0.000 [-0.304, +0.304] (n=20); qwen2.5-7b -0.500 [-0.856, -0.144] (n=20); qwen3.8-27b n=0
- Contrast vs reference (pilot) F(n_sting50) - F(n_reportfree): -0.118, 95% CI [-0.254, -0.007] (bootstrap over 7 models, 135 matched trials); models +/−/0: 1/4/2; sign test over trials p = 0.0357
  - per model: gemma-3-12b +0.000 [+0.000, +0.000] (n=20); gpt-4.1-mini -0.250 [-0.585, +0.085] (n=20); gpt-oss-120b-or -0.133 [-0.545, +0.278] (n=15); llama-3.1-8b +0.050 [-0.189, +0.289] (n=20); llama-3.2-3b +0.000 [+0.000, +0.000] (n=20); ministral-8b -0.050 [-0.371, +0.271] (n=20); qwen2.5-7b -0.450 [-0.805, -0.095] (n=20); qwen3.8-27b n=0

### Pooled (informative models)

| condition | models | trials | plant-only | other-only | F | 95% CI (boot) | McNemar p |
|---|---|---|---|---|---|---|---|
| n_reportfree | 3 | 60 | 22 | 1 | 0.350 | [+0.300, +0.400] | 5.72e-06 |
| n_audit50 | 3 | 59 | 5 | 15 | -0.170 | [-0.368, +0.000] | 0.041 |
| n_sting50 | 3 | 55 | 10 | 6 | 0.073 | [-0.100, +0.200] | 0.455 |

- Contrast vs reference (pilot) F(n_audit50) - F(n_reportfree): -0.525, 95% CI [-0.684, -0.400] (bootstrap over 3 models, 59 matched trials); models +/−/0: 0/3/0; sign test over trials p = 1.29e-05
  - per model: gpt-4.1-mini -0.400 [-0.719, -0.082] (n=20); gpt-oss-120b-or -0.684 [-1.111, -0.258] (n=19); qwen2.5-7b -0.500 [-0.856, -0.144] (n=20)
- Contrast vs reference (pilot) F(n_sting50) - F(n_reportfree): -0.291, 95% CI [-0.450, -0.133] (bootstrap over 3 models, 55 matched trials); models +/−/0: 0/3/0; sign test over trials p = 0.0107
  - per model: gpt-4.1-mini -0.250 [-0.585, +0.085] (n=20); gpt-oss-120b-or -0.133 [-0.545, +0.278] (n=15); qwen2.5-7b -0.450 [-0.805, -0.095] (n=20)

### Descriptive split by turn-1 decision (post-treatment; not causal)

| condition | turn1 | n | p_pass_plant | p_pass_other | F | mcnemar_p |
|---|---|---|---|---|---|---|
| n_reportfree | ACCEPT | 127 | 0.449 | 0.268 | 0.181 | 6.62e-05 |
| n_reportfree | not ACCEPT | 13 | 0.308 | 0.154 | 0.154 | 0.500 |
| n_audit50 | ACCEPT | 9 | 0.000 | 0.000 | 0.000 | 1.000 |
| n_audit50 | not ACCEPT | 130 | 0.192 | 0.246 | -0.054 | 0.248 |
| n_sting50 | ACCEPT | 20 | 0.100 | 0.150 | -0.050 | 1.000 |
| n_sting50 | not ACCEPT | 115 | 0.209 | 0.130 | 0.078 | 0.035 |
