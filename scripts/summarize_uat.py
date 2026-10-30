"""Summarise UAT results and check traceability to acceptance criteria.

Run from the project root:  python3 scripts/summarize_uat.py
Reads uat/test_cases.csv, uat/defect_log.csv and docs/02_user_stories.md.
"""
import pandas as pd
import re

tests = pd.read_csv("uat/test_cases.csv")
defects = pd.read_csv("uat/defect_log.csv")

# Every acceptance criterion (AC-xx.y) in the user stories
with open("docs/02_user_stories.md", encoding="utf-8") as f:
    criteria = sorted(set(re.findall(r"AC-\d{2}\.\d", f.read())))

covered = set(tests["acceptance_criteria"])
gaps = [ac for ac in criteria if ac not in covered]

status_counts = tests["status"].value_counts().to_dict()
executed = len(tests) - status_counts.get("Not run", 0)
open_defects = defects[defects["status"] == "Open"]
high_open = open_defects[open_defects["severity"].isin(["Critical", "High"])]

lines = [
    "# UAT summary",
    "",
    f"Test cases: {len(tests)} · Executed: {executed} of {len(tests)} "
    f"({executed / len(tests):.0%})",
    "",
    "| Status | Count |",
    "|---|---:|",
    *[f"| {s} | {status_counts.get(s, 0)} |" for s in ["Pass", "Fail", "Not run"]],
    "",
    f"Acceptance criteria: {len(criteria)} · Covered by a test: {len(criteria) - len(gaps)}",
    f"Coverage gaps: {', '.join(gaps) if gaps else 'none'}",
    "",
    f"Open defects: {len(open_defects)} (High or Critical: {len(high_open)})",
    "",
    "## Exit criteria check",
    f"- All tests executed: {'Yes' if executed == len(tests) else 'No'}",
    f"- No open High or Critical defects: {'Yes' if high_open.empty else 'No'}",
    f"- Traceability complete: {'Yes' if not gaps else 'No'}",
]
text = "\n".join(lines) + "\n"
with open("uat/uat_summary.md", "w", encoding="utf-8") as f:
    f.write(text)
print(text)
