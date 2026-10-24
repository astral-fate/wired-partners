# Detector economics (Study 2 rates; benign-to-collusive ratio swept)

Per 10,000 collusive offers, a share pi are plants. Catches = plants accepted. Genuine reports = reports of non-plant collusive offers, (1 - pi) N rho_c. False alarms = reports of benign private proposals, M rho_b (benign report rate 100/200 under the 50% sting). Precision = genuine / (genuine + false). Break-even ratio: M/N at which precision is 0.5.

| plant_rate | tested_condition | benign_ratio | accept | report_rate_collusive | plants | catches | genuine_reports | false_alarms | precision | breakeven_ratio |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.001 | n_sting1 | 0.100 | 55/200 | 0.440 | 10.000 | 2.800 | 4395.600 | 500.000 | 0.898 | 0.879 |
| 0.001 | n_sting1 | 1.000 | 55/200 | 0.440 | 10.000 | 2.800 | 4395.600 | 5000.000 | 0.468 | 0.879 |
| 0.001 | n_sting1 | 10.000 | 55/200 | 0.440 | 10.000 | 2.800 | 4395.600 | 50000.000 | 0.081 | 0.879 |
| 0.010 | n_sting1 | 0.100 | 55/200 | 0.440 | 100.000 | 27.500 | 4356.000 | 500.000 | 0.897 | 0.871 |
| 0.010 | n_sting1 | 1.000 | 55/200 | 0.440 | 100.000 | 27.500 | 4356.000 | 5000.000 | 0.466 | 0.871 |
| 0.010 | n_sting1 | 10.000 | 55/200 | 0.440 | 100.000 | 27.500 | 4356.000 | 50000.000 | 0.080 | 0.871 |
| 0.050 | n_sting5 | 0.100 | 49/200 | 0.515 | 500.000 | 122.500 | 4892.500 | 500.000 | 0.907 | 0.979 |
| 0.050 | n_sting5 | 1.000 | 49/200 | 0.515 | 500.000 | 122.500 | 4892.500 | 5000.000 | 0.495 | 0.979 |
| 0.050 | n_sting5 | 10.000 | 49/200 | 0.515 | 500.000 | 122.500 | 4892.500 | 50000.000 | 0.089 | 0.979 |
