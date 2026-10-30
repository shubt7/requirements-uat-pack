# User stories and acceptance criteria

## US-01: Monthly return rate by category

**As** a Finance Controller,
**I want** to see the return rate for each product category for a chosen month,
**so that** I can confirm the figures against the ledger.

**Acceptance criteria**
- **AC-01.1** Given a month is selected, when the report runs, then each category shows returned units, net units sold and return rate (BR-04).
- **AC-01.2** Given a return was received in August but the item was sold in July, when the August report runs, then the return counts in August (BR-01).
- **AC-01.3** Given an order was cancelled before shipment, when the report runs, then it is excluded from net units sold (BR-03).

## US-02: Return rate by store

**As** an Operations Manager,
**I want** to compare return rates across stores,
**so that** I can spot stores with unusual return activity.

**Acceptance criteria**
- **AC-02.1** Given a store with no returns in the month, when the report runs, then the store shows 0.0% and is not dropped.
- **AC-02.2** Given a return with a store code not in the store master, when the report runs, then the row appears on the exception list and not in store totals.

## US-03: Exchanges are not returns

**As** a Finance Controller,
**I want** exchanges excluded from return figures,
**so that** return rates are not overstated.

**Acceptance criteria**
- **AC-03.1** Given a transaction type of "Exchange", when the report runs, then it is not counted as a return (BR-02).
- **AC-03.2** Given a "Refund" or "Credit note" transaction, when the report runs, then it is counted as a return.

## US-04: Return reasons

**As** a Merchandising Lead,
**I want** returns grouped by reason,
**so that** I can see which product problems drive returns.

**Acceptance criteria**
- **AC-04.1** Given a return with no reason, when the report runs, then it is shown as "Unspecified" and included in totals (BR-05).
- **AC-04.2** Given the four reason groups, when the report runs, then every return maps to exactly one group.

## US-05: Data quality exceptions

**As** a Data Analyst,
**I want** a list of records that fail data checks,
**so that** I can fix them at source.

**Acceptance criteria**
- **AC-05.1** Given a return with a negative quantity, when the report runs, then it appears on the exception list.
- **AC-05.2** Given the exception list is not empty, when the report is published, then the report header shows the exception count.
