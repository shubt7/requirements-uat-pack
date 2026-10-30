# Requirements and UAT Pack: Monthly Returns Report

A complete set of business analysis deliverables for one reporting project, from the business requirements through to user acceptance testing. It shows how a business problem becomes requirements, user stories, business rules, a source-to-target mapping and a traced set of tests.

**Brightline Outfitters is a fictional company.** The scenario, data and results are invented for this portfolio project.

## The business problem

Finance and Operations each produce their own monthly returns numbers, which often disagree. The report takes three days by hand. This pack defines the agreed report and the checks that prove it works.

## What's in the pack

| Folder / file | What it is | Why it matters |
|---|---|---|
| `docs/01_business_requirements.md` | Business requirements document: objectives, scope, stakeholders, business rules, risks, success criteria | Agrees what is being built and why |
| `docs/02_user_stories.md` | User stories with Given/When/Then acceptance criteria | Makes each requirement testable |
| `docs/03_process_map.md` | Current and future process, with a flow diagram | Shows what changes for each team |
| `docs/04_source_to_target_mapping.md` | Each report field traced to its source | Gives data engineering a clear build spec |
| `uat/uat_test_plan.md` | Entry and exit criteria, roles, severity scale | Defines what "ready to go live" means |
| `uat/test_cases.csv` | Test cases linked to acceptance criteria | Proves each requirement is tested |
| `uat/defect_log.csv` | Defects found in testing, with severity and owner | Tracks what must be fixed before sign-off |
| `scripts/summarize_uat.py` | Builds the UAT summary and checks traceability | Shows the exit-criteria status at a glance |

## Traceability

Every acceptance criterion in the user stories links to at least one test case. The script checks this automatically. If someone adds a new criterion and forgets to test it, the summary shows the gap.

## Sample UAT result

Running `python3 scripts/summarize_uat.py` on the sample data:

| Measure | Result |
|---|---|
| Test cases | 12 |
| Executed | 9 of 12 (75%) |
| Pass / Fail / Not run | 7 / 2 / 3 |
| Acceptance criteria covered | 11 of 11 |
| Open defects | 2 (1 High) |
| Exit criteria met | No |

The sample run shows what good UAT looks like in practice. It finds two defects, both logged with steps to reproduce, an expected result and an owner. The go-live decision waits until the High defect is fixed and the remaining tests are run.

## How to run

Requires Python 3.9+ with pandas.

```bash
pip install pandas
python3 scripts/summarize_uat.py
```

## What I'd do next

- Add a reference workbook and a script that compares the report output against it.
- Add a traceability matrix that links each business rule (BR-01 to BR-05) to its tests.
- Add a change request template for scope changes after sign-off.
