# Data Quality Report — Week 1 Baseline

Generated from `notebooks/01_data_profiling.ipynb` (15 Sep 2026). Re-run after every cleaning change.

## Summary
| Table | Rows | Nulls | Dup rows | PK unique | FK integrity | Verdict |
|---|---:|---:|---:|---|---|---|
| branches | 6 | 0 | 0 | ✔ | — | Clean; parse `warehouse_capacity` |
| products | 30 | 0 | 0 | ✔ | — | Clean |
| suppliers | 8 | 0 | 0 | ✔ | — | Clean; pincode synthetic |
| customers | 500 | 0 | 0 | ✔ | branch_id ✔ | Clean |
| inventory_master | 180 | 0 | 0 | ✔ (composite) | ✔ | ⚠ `current_stock` outlier |
| purchase_orders_header | 24,000 | 2,370 | 0 | ✔ | ✔ | Nulls = cancelled POs (expected) |
| purchase_orders_lines | 155,495 | 0 | 0 | ✔ (composite) | ✔ | Clean |
| sales_orders_header | 20,000 | 0 | 0 | ✔ | ✔ | Clean |
| sales_orders_lines | 130,402 | 0 | 0 | ✔ (composite) | ✔ | Clean |
| invoices | 18,033 | 0 | 0 | ✔ | so_id ✔ (1:1 with Delivered SOs) | Clean |
| payments | 19,257 | 0 | 0 | ✔ | ✔ | Clean |
| stock_ledger | 237,230 | 0 | 0 | ✔ | ✔ | Validate running_balance continuity |

## Issue log
| ID | Table.column | Issue | Severity | Rule / fix | Owner | Status |
|---|---|---|---|---|---|---|
| DQ-001 | purchase_orders_header.received_date | 2,370 nulls | Low | Keep null; exclude Cancelled from lead-time KPIs | DA1 | Accepted |
| DQ-002 | inventory_master.current_stock | ~100k units vs max_stock ≤ 582 | High | Recompute from ledger; flag as reconciliation gap RSK-01 | DS | Open |
| DQ-003 | branches.warehouse_capacity | Text with unit | Low | `str.replace(' sqft','').astype(int)` | DA1 | Open |
| DQ-004 | suppliers.pincode | 6-digit Indian format on Chinese addresses | Info | Do not geocode | DA2 | Accepted |
| DQ-005 | *.gst_amount / grand_total | Floating-point tails (e.g. 60116.00000000001) | Low | `round(2)` on load | DA1 | Open |
| DQ-006 | purchase_orders_header.grand_total | PO spend (₹44,169 Cr) ≫ sales (₹3,242 Cr) | High | Check PO qty scale vs SO; possible synthetic inflation — document, don't "fix" | DS | Open |
| DQ-007 | stock_ledger.running_balance | Verify balance(t) = balance(t-1) ± qty per product×branch | Medium | Continuity test in `clean.py` | DS | Open |
| DQ-008 | customers.last_purchase_date | Min 2015-04-30 predates ledger (2019) | Low | Keep; flag pre-2019 as legacy | DA2 | Accepted |
| DQ-009 | products.lead_time_days vs suppliers.lead_time_days | Two lead-time sources | Info | Use PO actuals; masters as reference | DA2 | Accepted |
