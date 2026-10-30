# Business Requirements Document: Monthly Returns Report

**Fictional company:** Brightline Outfitters (sample scenario)
**Version:** 1.0 · **Status:** Approved for build · **Owner:** Business Analyst

## 1. Background

Brightline sells outdoor clothing through stores and an online shop. Each month the Finance and Operations teams build a returns report by hand. It takes about three working days, and the two teams often report different return rates for the same month.

## 2. Business objectives

1. Produce one monthly returns report that Finance and Operations both accept.
2. Cut report preparation from three days to one hour or less.
3. Show return rate by category and store so the merchandising team can act on problem products.

## 3. Scope

**In scope**
- Monthly return rate by product category, store and sales channel.
- Return reasons, grouped into four categories.
- Month-on-month and year-on-year comparison.
- Exception list of returns that fail data checks.

**Out of scope**
- Refund processing and payment reconciliation (owned by Finance systems).
- Customer-level analysis and personal data.
- Forecasting of future returns.

## 4. Stakeholders

| Stakeholder | Role | Interest |
|---|---|---|
| Finance Controller | Approves the report | One agreed set of numbers |
| Operations Manager | Uses the report weekly | Store-level return rates |
| Merchandising Lead | Acts on the results | Category and product problems |
| Data Engineering | Provides the source data | Clear source definitions |

## 5. Business rules

| ID | Rule |
|---|---|
| BR-01 | A return counts in the month the item is received back at the warehouse or store, not the month it was sold. |
| BR-02 | Exchanges are not returns. Only refunds and credit notes count. |
| BR-03 | Orders cancelled before shipment are excluded from both the numerator and the denominator. |
| BR-04 | Return rate = returned units ÷ net units sold, shown to one decimal place. |
| BR-05 | Returns with no return reason are reported under "Unspecified" and are included in totals. |

## 6. Key metrics

- **Return rate %** = returned units ÷ net units sold (BR-04).
- **Return value** = refund amount of returned items.
- **Top return reason** = the reason group with the most returned units.

## 7. Assumptions and dependencies

- The orders, returns and product master tables are refreshed daily by 06:00.
- Store codes in the returns table match the store master.
- Finance has signed off the definition of "net units sold" (BR-03).

## 8. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Store codes do not match the master list | Returns missing from store reports | Exception list plus a daily data check |
| Finance and Operations keep their own definitions | Numbers still disagree | Business rules agreed and signed before build |
| Late refresh of source data | Report delayed | Report runs after the 06:00 refresh and shows the data date |

## 9. Success criteria

- Finance and Operations agree the August test month to the unit.
- Report produced in one hour or less after data refresh.
- All UAT test cases pass or have an approved workaround.
