# KPI Framework — Heavy Warehouse Intelligence

Each KPI has one owner, one source of truth (table + formula) and one dashboard home. Targets are first-pass benchmarks for heavy-equipment spare-parts distribution in India; revise after Week-3 baselining.

| ID | Domain | KPI | Formula | Source tables | Grain | Target | Owner | Dashboard |
|----|--------|-----|---------|---------------|-------|--------|-------|-----------|
| INV-01 | Inventory | Inventory Turnover | Σ(OUT qty × unit_cost) ÷ avg(running_balance × unit_cost) | stock_ledger, products | product × branch × year | ≥ 4× | DA1 | Inventory Health |
| INV-02 | Inventory | Days Inventory Outstanding | 365 ÷ INV-01 | derived | product × branch | ≤ 90 days | DA1 | Inventory Health |
| INV-03 | Inventory | Stockout Rate | days with running_balance ≤ 0 ÷ total days | stock_ledger | product × branch | ≤ 2 % | DS | Inventory Health |
| INV-04 | Inventory | Overstock % | SKU-branch pairs with balance > max_stock ÷ 180 | stock_ledger, inventory_master | branch | ≤ 10 % | DA1 | Inventory Health |
| INV-05 | Inventory | Understock % | pairs with balance < reorder_level ÷ 180 | stock_ledger, inventory_master | branch | ≤ 5 % | DA1 | Inventory Health |
| INV-06 | Inventory | Inventory Ageing (days) | today − date of last OUT movement | stock_ledger | product × branch | ≤ 120 | DA1 | Inventory Health |
| INV-07 | Inventory | Dead-stock value | Σ balance × unit_cost where no OUT in 180 d | stock_ledger, products | branch | ↓ 30 % | DA1 | Inventory Health |
| INV-08 | Inventory | ABC class | cumulative revenue share: A ≤ 80 %, B ≤ 95 %, C rest | sales_orders_lines, products | product | — | DA1 | Product Performance |
| INV-09 | Inventory | Capital locked in stock | Σ running_balance × unit_cost (latest) | stock_ledger, products | branch | ↓ 15 % | DA1 | Inventory Health |
| PRD-01 | Product | Revenue contribution | Σ line_total ÷ total revenue | sales_orders_lines | product | — | DA1 | Product Performance |
| PRD-02 | Product | Gross margin % | Σ(qty × (unit_price − unit_cost)) ÷ Σ line_total | sales_orders_lines, products | product | ≥ 30 % | DA1 | Product Performance |
| PRD-03 | Product | Velocity (units/month) | Σ OUT qty ÷ months active | stock_ledger | product × branch | — | DA1 | Product Performance |
| PRD-04 | Product | Fast / slow mover flag | velocity quartile: Q4 fast, Q1 slow | derived | product | — | DA1 | Product Performance |
| PRD-05 | Product | Demand trend (YoY %) | (units yr n − yr n-1) ÷ yr n-1 | sales_orders_lines | product × year | — | DS | Product Performance |
| WH-01 | Warehouse | Throughput / day | Σ(IN + OUT qty) ÷ operating days | stock_ledger | branch | ↑ | DA1 | Warehouse Efficiency |
| WH-02 | Warehouse | Revenue per sq ft | avg_monthly_revenue ÷ capacity_sqft | branches | branch | ≥ ₹110 | DA1 | Warehouse Efficiency |
| WH-03 | Warehouse | Revenue per employee | avg_monthly_revenue ÷ total_employees | branches | branch | ≥ ₹55k | DA1 | Warehouse Efficiency |
| WH-04 | Warehouse | Operating margin % | (revenue − op cost) ÷ revenue | branches | branch | ≥ 35 % | DA1 | Warehouse Efficiency |
| WH-05 | Warehouse | Space utilisation % | Σ(balance × unit volume) ÷ capacity volume | stock_ledger, products, branches | branch | 65–85 % | DA1 | Warehouse Efficiency |
| WH-06 | Warehouse | Order-to-delivery days | delivery_date − order_date | sales_orders_header | branch | ≤ 5 | DA1 | Warehouse Efficiency |
| WH-07 | Warehouse | Warehouse Performance Score | weighted z-score of WH-01…06 | derived | branch | rank | DA1 | Warehouse Efficiency |
| SUP-01 | Supplier | On-time delivery % | received_date ≤ expected_delivery_date ÷ received POs | purchase_orders_header | supplier | ≥ 90 % | DA2 | Supplier Performance |
| SUP-02 | Supplier | Actual lead time (days) | received_date − order_date | purchase_orders_header | supplier | ≤ contracted | DA2 | Supplier Performance |
| SUP-03 | Supplier | Lead-time variance | σ(actual − contracted lead time) | purchase_orders_header, suppliers | supplier | ≤ 3 d | DA2 | Supplier Performance |
| SUP-04 | Supplier | Cancellation rate | Cancelled ÷ total POs | purchase_orders_header | supplier | ≤ 5 % | DA2 | Supplier Performance |
| SUP-05 | Supplier | Spend share | Σ grand_total ÷ total spend | purchase_orders_header | supplier | no supplier > 35 % | DA2 | Supplier Performance |
| SUP-06 | Supplier | Dependency risk (HHI) | Σ(spend share²) per product | purchase_orders_lines, header | product | < 0.25 | DA2 | Supplier Performance |
| SUP-07 | Supplier | Landed cost index | unit_cost × (1 + import_duty_rate) ÷ list unit_cost | PO lines, suppliers, products | supplier × product | — | DA2 | Supplier Performance |
| CUS-01 | Customer | RFM score | quintiles of recency, frequency, monetary | invoices | customer | — | DA2 | Customer Analytics |
| CUS-02 | Customer | CLV (historic) | Σ grand_total × margin % | invoices, products | customer | — | DA2 | Customer Analytics |
| CUS-03 | Customer | Retention rate | customers active in yr n and yr n-1 ÷ active yr n-1 | sales_orders_header | year | ≥ 80 % | DA2 | Customer Analytics |
| CUS-04 | Customer | Churn flag | no order in > 180 days | sales_orders_header | customer | ≤ 15 % | DS | Customer Analytics |
| CUS-05 | Customer | DSO | avg(payment_date − invoice_date) | invoices, payments | customer / branch | ≤ 45 d | DA2 | Customer Analytics |
| CUS-06 | Customer | Collection rate | Σ payment_amount ÷ Σ invoice grand_total | invoices, payments | branch | ≥ 95 % | DA2 | Customer Analytics |
| CUS-07 | Customer | Credit utilisation | current_balance ÷ credit_limit | customers | customer | ≤ 80 % | DA2 | Customer Analytics |
| FC-01 | Forecast | Forecast accuracy (MAPE) | mean(|actual − forecast| ÷ actual) | model output | product × month | ≤ 20 % | DS | Inventory Health |
| FC-02 | Forecast | Reorder point | avg daily demand × lead time + safety stock | derived | product × branch | — | DS | Inventory Health |
| FC-03 | Forecast | Safety stock | z × σ_demand × √lead_time (z = 1.65 @ 95 %) | derived | product × branch | — | DS | Inventory Health |
| FC-04 | Forecast | Stockout risk probability | classifier P(balance ≤ 0 in next 30 d) | model output | product × branch | — | DS | Inventory Health |
| RSK-01 | Risk | Ledger reconciliation gap | inventory_master.current_stock − last running_balance | inventory_master, stock_ledger | product × branch | = 0 | DS | Anomaly Monitor |
| RSK-02 | Risk | Adjustment rate | ADJUSTMENT qty ÷ total movement qty | stock_ledger | branch | ≤ 1 % | DS | Anomaly Monitor |
| RSK-03 | Risk | Movement anomaly count | Isolation-Forest / z-score > 3 on daily qty | stock_ledger | branch | ↓ | DS | Anomaly Monitor |

**Owners:** DS = Data Scientist (Eswar) · DA1 = Data Analyst 1 · DA2 = Data Analyst 2.
