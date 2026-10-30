# Source-to-target mapping

| Target field (report) | Source table | Source field | Transformation | Rule |
|---|---|---|---|---|
| Month | returns | received_date | First day of month | BR-01 |
| Store code | returns | store_code | Trim, upper-case; must exist in store_master | AC-02.2 |
| Category | product_master | category | Join on sku | None |
| Transaction type | returns | txn_type | Keep "Refund" and "Credit note" only | BR-02 |
| Returned units | returns | quantity | Must be greater than 0 | AC-05.1 |
| Net units sold | orders | quantity - cancelled_quantity | Exclude orders cancelled before shipment | BR-03 |
| Return reason group | returns | reason_code | Map to four groups; blank becomes "Unspecified" | BR-05, AC-04.2 |
| Return value | returns | refund_amount | Sum in USD | None |
