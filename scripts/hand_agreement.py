"""Agreement between the decision parser and the author's hand labels.

    python scripts/hand_agreement.py

Hand labels are read from the annotation database (DATABASE_URL, or ../annotation-space/.dburl), project
wired_partners, or, without a database, from validation/hand_labels_author.csv; item wp-NNN is row NNN of validation/answer_key_DO_NOT_OPEN.csv, whose reply text is checked against
the logged trial before it is used. Hand NOT_A_DECISION is compared with the parser's SAFETY-REFUSAL and UNPARSED
codes. Writes results/analysis/hand_agreement.json and paper/numbers_hand.tex (\\N{hand/...} macros).
"""
import csv
import json
import os
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIRS = {"study1": "main_v1", "study2": "main_v2", "study2b": "main_v2b", "study4": "main_v4"}
DBURL = ROOT.parent / "annotation-space" / ".dburl"
url = os.environ.get("DATABASE_URL") or (DBURL.read_text().strip() if DBURL.exists() else None)
EXPORT = ROOT / "validation" / "hand_labels_author.csv"
if url and os.environ.get("HAND_LABELS") != "csv":
    import psycopg
    with psycopg.connect(url, connect_timeout=20) as c:
        hand = {r[0]: r[1] for r in c.execute(
            "select item_id, label from collusion_annotations where project = 'wired_partners' and label is not null")}
        hand_reason = {r[0]: r[1] for r in c.execute(
            "select item_id, reason from collusion_annotations where project = 'wired_partners' and reason is not null")}
else:  # no database: use the exported labels
    rows = list(csv.DictReader(open(EXPORT, encoding="utf-8")))
    hand = {r["item"]: r["hand_label"] for r in rows}
    hand_reason = {r["item"]: r["hand_reason"] for r in rows if r["hand_reason"]}

key = {f"wp-{int(r['item']):03d}": r for r in csv.DictReader(open(ROOT / "validation" / "answer_key_DO_NOT_OPEN.csv",
                                                                 encoding="utf-8-sig"))}
items = {json.loads(x)["id"]: json.loads(x)["text"] for x in
         open(ROOT.parent / "annotation-space" / "items" / "wired_partners.jsonl", encoding="utf-8")}


def coarse(d):
    return d if d in ("ACCEPT", "DECLINE", "REPORT") else "NOT_A_DECISION"


pairs, mismatch_text = [], 0
for iid, lab in sorted(hand.items()):
    k = key.get(iid)
    if not k:
        continue
    # confirm the item text is the logged reply of that trial
    trials = ROOT / "results" / DIRS.get(k["study"], "") / "trials.jsonl"
    ok = False
    if trials.exists():
        for line in open(trials, encoding="utf-8"):
            r = json.loads(line)
            if (r["model"], r["condition"], str(r["trial"])) == (k["model"], k["condition"], k["trial"]):
                ok = r.get("response", "").strip()[:80] == items.get(iid, "").strip()[:80]
                if ok:
                    break
    mismatch_text += not ok
    pairs.append((coarse(k["parser_decision"]), lab, ok))

use = [(p, h) for p, h, ok in pairs if ok] or [(p, h) for p, h, _ in pairs]
n = len(use)
agree = sum(p == h for p, h in use)
cats = sorted({x for pr in use for x in pr})
po = agree / n if n else 0
pp, ph = Counter(p for p, _ in use), Counter(h for _, h in use)
pe = sum(pp[c] * ph[c] for c in cats) / n ** 2 if n else 0
kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0
res = {"n": n, "agree": agree, "agreement": po, "kappa": kappa, "text_unverified": mismatch_text,
       "confusion": {f"{p}|{h}": v for (p, h), v in Counter(use).items()}}
M = {"hand/n": str(n), "hand/agree": str(agree), "hand/agreement": f"{100 * po:.0f}", "hand/kappa": f"{kappa:.2f}"}


def cohen(pairs_):
    n_ = len(pairs_)
    if not n_:
        return None
    po_ = sum(a == b for a, b in pairs_) / n_
    ca, cb = Counter(a for a, _ in pairs_), Counter(b for _, b in pairs_)
    pe_ = sum(ca[c] * cb[c] for c in set(ca) | set(cb)) / n_ ** 2
    return (po_ - pe_) / (1 - pe_) if pe_ < 1 else 1.0


# main reason: each LLM judge (results/analysis/reasons.jsonl) against the hand label, and judge against judge
judged = {}
rpath = ROOT / "results" / "analysis" / "reasons.jsonl"
if rpath.exists():
    for line in open(rpath, encoding="utf-8"):
        r = json.loads(line)
        if r["label"] not in ("ERROR", "UNPARSED"):
            judged[(r["study"], r["model"], r["condition"], str(r["trial"]), r["judge"])] = r["label"]
    judges = sorted({k[-1] for k in judged})
    for j in judges:
        pr = [(hand_reason[i], judged[(key[i]["study"], key[i]["model"], key[i]["condition"], key[i]["trial"], j)])
              for i in hand_reason if i in key
              and (key[i]["study"], key[i]["model"], key[i]["condition"], key[i]["trial"], j) in judged]
        k_ = cohen(pr)
        if k_ is not None:
            res[f"reason_kappa/{j}"] = {"n": len(pr), "kappa": k_, "agree": sum(a == b for a, b in pr)}
            M[f"hand/reason/{j}/kappa"], M[f"hand/reason/{j}/n"] = f"{k_:.2f}", str(len(pr))
            M[f"hand/reason/{j}/agreement"] = f"{100 * sum(a == b for a, b in pr) / len(pr):.0f}"
    if len(judges) == 2:
        a_, b_ = judges
        both = [(judged[k[:-1] + (a_,)], judged[k[:-1] + (b_,)]) for k in judged if k[-1] == a_ and k[:-1] + (b_,) in judged]
        res["judge_judge"] = {"n": len(both), "kappa": cohen(both)}
        M["hand/judges/kappa"], M["hand/judges/n"] = f"{cohen(both):.2f}", f"{len(both):,}"
(ROOT / "results" / "analysis" / "hand_agreement.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
lines = ["% Generated by scripts/hand_agreement.py. Do not edit by hand.", r"\makeatletter"]
lines += [rf"\expandafter\def\csname wp@{k}\endcsname{{{v}}}" for k, v in sorted(M.items())]
(ROOT / "paper" / "numbers_hand.tex").write_text("\n".join(lines + [r"\makeatother"]) + "\n", encoding="utf-8")
print(json.dumps(res, indent=1))
