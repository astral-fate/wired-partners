"""Figure for Study 4 (stated stakes): pooled acceptance per condition with Wilson 95% CIs, marked by what the
risk-neutral benchmark predicts. A sting rule makes accepting worth it iff (1-p)B > pF with B = 2. Mild rules have
F = 1, so accept at every tested rate. Disqualification loses all points, so its F is the agent's current score
(0-6 in the generator): at 1% accepting is worth it for any F < 198 (accept); at 50% only if F < 2 (depends on the
score). With no stated penalty (prohibition alone) the benchmark is undetermined; stated as unenforced, F = 0.

    python scripts/fig_study4.py
"""
import csv
import math
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
ROWS = [("c_reportfree", "No rule", "#999999"), ("c_prohibit", "Prohibition only", "#000000"),
        ("c_prohibit_nopenalty", "Prohibition,\nstated unenforced", "#777777"),
        ("c_mild_noprohibit_sting50", "Mild sting 50%,\nno prohibition", "#E69F00"),
        ("c_mild_sting1", "Mild sting 1%", "#E69F00"), ("c_mild_sting10", "Mild sting 10%", "#E69F00"),
        ("c_mild_sting50", "Mild sting 50%", "#E69F00"), ("c_mild_audit50", "Mild audit 50%", "#56B4E9"),
        ("c_severe_sting1", "Severe sting 1%", "#D55E00"), ("c_severe_sting50", "Severe sting 50%", "#D55E00"),
        ("c_safeharbour_sting50", "Severe sting 50%,\nsafe harbour", "#D55E00")]
EV_ACCEPT = {"c_reportfree", "c_prohibit_nopenalty", "c_mild_noprohibit_sting50", "c_mild_sting1", "c_mild_sting10",
             "c_mild_sting50", "c_mild_audit50", "c_severe_sting1"}
EV_UNDETERMINED = {"c_prohibit", "c_severe_sting50", "c_safeharbour_sting50"}  # penalty unstated / depends on score


def wilson(k, n, z=1.96):
    if n == 0:
        return 0, 0
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def main():
    agg = defaultdict(lambda: [0, 0])
    with open(ROOT / "results" / "analysis" / "tables" / "cell_counts.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["study"] == "study4":
                agg[r["condition"]][0] += int(r["accept"])
                agg[r["condition"]][1] += int(r["n"])
    plt.rcParams.update({"font.size": 7, "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42})
    fig, ax = plt.subplots(figsize=(3.3, 3.3))
    for i, (c, label, col) in enumerate(ROWS):
        k, n = agg[c]
        if not n:
            continue
        p = k / n
        lo, hi = wilson(k, n)
        ax.errorbar(p, i, xerr=[[p - lo], [hi - p]], fmt="o", color=col, ms=4, capsize=1.5, lw=0.8)
        ax.text(min(hi + 0.03, 0.9), i, f"{100 * p:.0f}%", va="center", fontsize=6)
        if c in EV_ACCEPT and c != "c_reportfree":
            ax.plot([0.97], [i], marker="$\\checkmark$", color="#009E73", ms=5)
        elif c in EV_UNDETERMINED:
            ax.text(0.97, i, "?", ha="center", va="center", fontsize=7, color="#555555")
    ax.set_yticks(range(len(ROWS)), [r[1] for r in ROWS])
    ax.invert_yaxis()
    ax.set_xlim(0, 1.02)
    ax.set_xlabel("Share accepting the alliance (pooled, 10 models)")
    ax.set_title("Study 4: stated stakes (B = 2 points)", fontsize=7.5)
    ax.text(0.97, -0.9, "EV:\naccept", ha="center", fontsize=5.5, color="#009E73")
    out = ROOT / "results" / "analysis" / "figures"
    fig.savefig(out / "fig_study4.pdf", bbox_inches="tight")
    fig.savefig(out / "fig_study4.png", dpi=250, bbox_inches="tight")
    print("written")


if __name__ == "__main__":
    main()
