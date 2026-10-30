# UAT test plan: Monthly Returns Report

## Objective
Confirm that the report meets every acceptance criterion in `docs/02_user_stories.md` before go-live.

## Entry criteria
- Build complete and deployed to the UAT environment.
- Test data loaded for July and August 2026, including the edge cases in the test cases.
- Reference workbook agreed by Finance for August 2026.

## Exit criteria
- 100% of test cases executed.
- No open High or Critical defects.
- Finance Controller signs off the August figures.

## Roles
| Role | Responsibility |
|---|---|
| Business Analyst | Writes and runs test cases, logs defects, tracks traceability |
| Finance Controller | Signs off the reference numbers |
| Operations Manager | Tests the store view |
| Data Engineering | Fixes defects in the data pipeline |

## Traceability
Every acceptance criterion must have at least one test case. `scripts/summarize_uat.py` checks this and reports any gaps.

## Defect severity
| Severity | Meaning | Example |
|---|---|---|
| Critical | Report unusable or wrong totals for all users | Totals double-counted |
| High | A business rule is broken | Cancelled orders counted |
| Medium | Wrong output for a specific case | Blank reason dropped |
| Low | Cosmetic | Label spelling |

## Sample run result
The test cases in `uat/test_cases.csv` are sample data, and the results are illustrative. Two defects are logged against failed tests, and four tests have not been run yet.
