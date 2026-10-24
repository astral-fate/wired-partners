"""Write paper/permodel.tex: per-model acceptance (%) in the key cells of Studies 2b and 4, from cell_counts.csv.

    python scripts/make_permodel_table.py
"""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLS = [("study2b", "b_reportfree", "none"), ("study2b", "b_penalty", "pen."), ("study2b", "b_audit50", "aud.50"),
        ("study2b", "b_sting50", "st.50"), ("study2b", "b_placebo", "plac."),
        ("study4", "c_reportfree", "none"), ("study4", "c_prohibit", "proh."), ("study4", "c_mild_sting1", "m.st1"),
        ("study4", "c_mild_sting50", "m.st50"), ("study4", "c_mild_audit50", "m.aud50"),
        ("study4", "c_severe_sting50", "s.st50"), ("study4", "c_mild_noprohibit_sting50", "m.st50$-$p")]
NAMES = {"llama-3.1-8b": "Llama-3.1-8B", "qwen2.5-7b": "Qwen2.5-7B", "llama-3.2-3b": "Llama-3.2-3B",
         "ministral-8b": "Ministral-8B", "gpt-4.1-mini": "GPT-4.1-mini", "gemma-3-12b": "Gemma-3-12B",
         "gpt-oss-120b-or": "GPT-OSS-120B", "qwen3.8-27b": "Qwen3.8-27B", "nemotron-3.5-lightning": "Nemotron-3.5",
         "minimax-m3.1-flash": "MiniMax-M3.1"}


def main():
    cell = defaultdict(dict)
    with open(ROOT / "results" / "analysis" / "tables" / "cell_counts.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if int(r["n"]):
                cell[(r["study"], r["model"])][r["condition"]] = (int(r["accept"]), int(r["n"]))
    lines = [r"\begin{table}[h]", r"\centering\scriptsize", r"\setlength{\tabcolsep}{3pt}",
             r"\begin{tabular}{@{}l" + "r" * 5 + "|" + "r" * 7 + r"@{}}", r"\toprule",
             r" & \multicolumn{5}{c|}{Study 2b (severe penalty)} & \multicolumn{7}{c}{Study 4 (stated stakes)} \\",
             "Model & " + " & ".join(c[2] for c in COLS) + r" \\", r"\midrule"]
    for m, name in NAMES.items():
        vals = []
        for study, cond, _ in COLS:
            k = cell[(study, m)].get(cond)
            vals.append("--" if not k else f"{100 * k[0] / k[1]:.0f}")
        lines.append(f"{name} & " + " & ".join(vals) + r" \\")
    lines += [r"\bottomrule", r"\end{tabular}",
              r"\caption{Acceptance (\%) per model, $n=20$ per cell before missing trials. Study~2b: no rule, penalty only, "
              r"50\% audit, 50\% sting, placebo. Study~4: no rule, prohibition only, mild sting at 1\% and 50\%, mild audit "
              r"at 50\%, severe sting at 50\%, mild 50\% sting without the prohibition.}",
              r"\label{tab:permodel}", r"\end{table}"]
    (ROOT / "paper" / "permodel.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("written")


if __name__ == "__main__":
    main()
