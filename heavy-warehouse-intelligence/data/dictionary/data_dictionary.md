# Data Dictionary — Heavy Warehouse Intelligence

Auto-generated from `data/raw/*.csv` on 2026-09-15 by `src/hwi/dictionary.py`; descriptions curated by the team from the CadetX *Fields Documentation*.

Currency = INR (₹). Dates = ISO `YYYY-MM-DD`. GST rates = 18 % / 28 %.


## `branches.csv` — Warehouse / branch master — one row per physical site

**Rows:** 6 · **Columns:** 13 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `branch_id` | text | 6 | 6 | DEL001 | Primary key (e.g. DEL001) |
| `branch_name` | text | 6 | 6 | Delhi Central | Branch display name |
| `city` | text | 6 | 6 | Delhi | City |
| `state` | text | 6 | 6 | Delhi | Indian state |
| `region` | text | 6 | 4 | North | North / South / East / West |
| `warehouse_type` | text | 6 | 4 | Central | Central · Regional · Branch · Service Hub |
| `warehouse_capacity` | text | 6 | 6 | 45230 sqft | Storage area as text '45230 sqft' → parse to int (sq ft) |
| `service_center_available` | text | 6 | 2 | Yes | Yes/No — on-site service centre |
| `manager_id` | int | 6 | 6 | 9593 | Branch manager employee id |
| `total_employees` | int | 6 | 6 | 92 | Headcount |
| `avg_monthly_revenue` | int | 6 | 6 | 5234890 | Average monthly revenue (₹) |
| `monthly_operational_cost` | int | 6 | 6 | 3189000 | Monthly operating cost (₹) |
| `market_demand_index` | int | 6 | 4 | 9 | Demand score 1–10 (10 = highest) |

## `products.csv` — Product / SKU master — heavy-machinery spare parts

**Rows:** 30 · **Columns:** 23 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `product_id` | text | 30 | 30 | P001 | Primary key (P001–P030) |
| `product_name` | text | 30 | 30 | Hydraulic Pump HP-300 | Part name + part code |
| `category` | text | 30 | 15 | Hydraulic | Hydraulic, Filters, Engine, Undercarriage… |
| `machine_type` | text | 30 | 6 | Excavator | Excavator, Loader, Bulldozer, Crane, Dumper, All |
| `brand` | text | 30 | 6 | CAT | CAT, JCB, Komatsu, Volvo, Tata Hitachi, Generic |
| `model_compatibility` | text | 30 | 18 | CAT 320D | Compatible machine model |
| `unit_cost` | int | 30 | 30 | 18950 | Standard purchase cost (₹) |
| `unit_price` | int | 30 | 28 | 24500 | List selling price (₹) |
| `margin_percentage` | float | 30 | 30 | 29.2 | (price − cost) ÷ cost × 100 |
| `gst_rate` | int | 30 | 2 | 28 | GST % (18 or 28) |
| `weight_kg` | float | 30 | 29 | 38.5 | Unit weight (kg) — drives space & freight |
| `dimensions_cm` | text | 30 | 29 | 40x25x25 | L×W×H in cm |
| `material_type` | text | 30 | 10 | steel | steel, rubber, alloy… |
| `warranty_months` | int | 30 | 5 | 12 | Warranty period |
| `reorder_level` | int | 30 | 20 | 15 | Master reorder point (units) |
| `safety_stock` | int | 30 | 17 | 10 | Master safety stock (units) |
| `max_stock_level` | int | 30 | 19 | 40 | Master max stock (units) |
| `lead_time_days` | int | 30 | 19 | 21 | Standard replenishment lead time |
| `criticality_level` | text | 30 | 3 | High | High / Medium / Low |
| `usage_frequency` | text | 30 | 3 | Medium | High / Medium / Low |
| `uom` | text | 30 | 3 | piece | piece, set, cartridge |
| `last_purchase_price` | int | 30 | 30 | 18500 | Last PO unit price (₹) |
| `last_purchase_date` | date | 30 | 30 | 2019-03-15 | Date of last purchase |

## `suppliers.csv` — Supplier master — 8 China-based OEM / distributor / local vendors

**Rows:** 8 · **Columns:** 12 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `supplier_id` | text | 8 | 8 | SUP0001 | Primary key (SUP0001–SUP0008) |
| `supplier_name` | text | 8 | 8 | Shenzhen OEM Supplies | Supplier name |
| `supplier_type` | text | 8 | 3 | OEM | OEM · Distributor · Local Vendor |
| `product_category` | text | 8 | 3 | Medium Parts | Small / Medium / Large Parts |
| `city` | text | 8 | 8 | Shenzhen | Supplier city (China) |
| `province` | text | 8 | 6 | Guangdong | Chinese province |
| `region` | text | 8 | 3 | South China | South / East / North China |
| `pincode` | int | 8 | 8 | 586808 | Postal code (synthetic, Indian format) |
| `lead_time_days` | int | 8 | 7 | 19 | Contracted lead time |
| `reliability_score` | int | 8 | 3 | 5 | 1–5 (5 = best) |
| `import_duty_rate` | int | 8 | 4 | 8 | Import duty % applied to landed cost |
| `china_tax_id` | text | 8 | 8 | 90SUZHOU398241 | Supplier tax identifier |

## `customers.csv` — Customer master — 500 B2B accounts

**Rows:** 500 · **Columns:** 15 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `customer_id` | text | 500 | 500 | C0001 | Primary key (C0001–C0500) |
| `customer_type` | text | 500 | 5 | Retail | Government · Corporate · Dealer · Fleet Owner · Retail |
| `industry_segment` | text | 500 | 6 | Construction | Mining, Logistics, Construction, Infrastructure, Manufacturing, Rental |
| `city` | text | 500 | 21 | Kolkata | City |
| `state` | text | 500 | 16 | West Bengal | State |
| `pincode` | int | 500 | 500 | 991035 | Postal code |
| `region` | text | 500 | 6 | East | North / South / East / West |
| `branch_id` | text | 500 | 6 | KOL001 | FK → branches (home branch) |
| `credit_limit` | int | 500 | 500 | 45896 | Approved credit limit (₹) |
| `current_balance` | int | 500 | 499 | 43284 | Outstanding receivable (₹) |
| `payment_terms` | text | 500 | 5 | Advance | Advance · Net 15/30/45/60 |
| `customer_since` | text | 500 | 467 | 2024-04-10 | Onboarding date |
| `last_purchase_date` | date | 500 | 449 | 2024-04-25 | Most recent order date |
| `total_purchase_value` | int | 500 | 500 | 3892818 | Lifetime purchase value (₹) |
| `customer_rating` | int | 500 | 5 | 4 | Internal rating 1–5 |

## `inventory_master.csv` — Stock position per product × branch (30 × 6 = 180 rows)

**Rows:** 180 · **Columns:** 8 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `product_id` | text | 180 | 30 | P001 | FK → products |
| `branch_id` | text | 180 | 6 | DEL001 | FK → branches |
| `opening_stock` | int | 180 | 127 | 196 | Stock at period start (units) |
| `reorder_level` | int | 180 | 75 | 59 | Branch-level reorder point |
| `safety_stock` | int | 180 | 63 | 46 | Branch-level safety stock |
| `max_stock` | int | 180 | 148 | 340 | Branch-level max stock |
| `current_stock` | int | 180 | 180 | 115928 | Current on-hand — ⚠ values ~100k vs max ~500: reconcile with ledger |
| `warehouse_bin` | text | 180 | 95 | C15 | Bin location (e.g. C15) |

## `purchase_orders_header.csv` — Purchase order header — one row per PO to a supplier

**Rows:** 24,000 · **Columns:** 10 · **Nulls:** 2,370 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `po_id` | text | 24,000 | 24,000 | PO-141186 | Primary key |
| `supplier_id` | text | 24,000 | 8 | SUP0001 | FK → suppliers |
| `branch_id` | text | 24,000 | 6 | PUN001 | FK → branches (receiving site) |
| `order_date` | date | 24,000 | 2,192 | 2019-04-10 | PO raised date |
| `expected_delivery_date` | date | 24,000 | 2,207 | 2019-04-29 | Promised delivery |
| `received_date` | date | 21,630 | 2,207 | 2019-04-29 | Actual receipt — NULL for Cancelled POs |
| `po_status` | text | 24,000 | 2 | Received | Received · Cancelled |
| `total_cost` | float | 24,000 | 24,000 | 22955232.11 | Sum of line totals ex-GST (₹) |
| `total_gst_amount` | float | 24,000 | 24,000 | 6427464.990800001 | GST (₹) |
| `grand_total` | float | 24,000 | 24,000 | 29382697.1008 | Incl. GST (₹) |

## `purchase_orders_lines.csv` — Purchase order line items

**Rows:** 155,495 · **Columns:** 9 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `po_id` | text | 155,495 | 24,000 | PO-141186 | FK → purchase_orders_header |
| `line_number` | int | 155,495 | 12 | 1 | Line sequence within PO |
| `product_id` | text | 155,495 | 30 | P004 | FK → products |
| `quantity` | int | 155,495 | 281 | 234 | Units ordered |
| `unit_cost` | float | 155,495 | 142,292 | 34709.54 | Negotiated unit cost (₹) |
| `gst_rate` | int | 155,495 | 2 | 28 | GST % |
| `line_total` | float | 155,495 | 155,224 | 8122032.36 | qty × unit_cost |
| `gst_amount` | float | 155,495 | 155,254 | 2274169.0608 | line_total × gst_rate |
| `line_grand_total` | float | 155,495 | 155,269 | 10396201.4208 | line_total + gst |

## `sales_orders_header.csv` — Sales order header — one row per customer order

**Rows:** 20,000 · **Columns:** 11 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `so_id` | text | 20,000 | 20,000 | SO-990591 | Primary key |
| `customer_id` | text | 20,000 | 500 | C0070 | FK → customers |
| `branch_id` | text | 20,000 | 6 | AHM001 | FK → branches (fulfilling site) |
| `order_date` | date | 20,000 | 2,192 | 2022-05-24 | Order date |
| `delivery_date` | date | 20,000 | 2,204 | 2022-05-28 | Delivery date |
| `order_status` | text | 20,000 | 2 | Delivered | Delivered · Cancelled |
| `payment_terms` | text | 20,000 | 5 | Net 30 | Advance · Net 15/30/45/60 |
| `total_order_value` | int | 20,000 | 17,905 | 1345720 | Ex-GST (₹) |
| `total_gst_amount` | float | 20,000 | 18,749 | 374439.6 | GST (₹) |
| `grand_total` | float | 20,000 | 18,735 | 1720159.6 | Incl. GST (₹) |
| `sales_channel` | text | 20,000 | 4 | Counter Sale | Field Sales · Dealer Network · Counter Sale · Online |

## `sales_orders_lines.csv` — Sales order line items

**Rows:** 130,402 · **Columns:** 9 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `so_id` | text | 130,402 | 20,000 | SO-990591 | FK → sales_orders_header |
| `line_number` | int | 130,402 | 12 | 1 | Line sequence |
| `product_id` | text | 130,402 | 30 | P018 | FK → products |
| `quantity` | int | 130,402 | 20 | 19 | Units sold |
| `unit_price` | int | 130,402 | 28 | 11300 | Selling price (₹) |
| `gst_rate` | int | 130,402 | 2 | 28 | GST % |
| `line_total` | int | 130,402 | 534 | 214700 | qty × unit_price |
| `gst_amount` | float | 130,402 | 534 | 60116.00000000001 | GST (₹) |
| `line_grand_total` | float | 130,402 | 534 | 274816.0 | Incl. GST (₹) |

## `invoices.csv` — Invoices — one per delivered sales order

**Rows:** 18,033 · **Columns:** 10 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `invoice_id` | text | 18,033 | 17,836 | INV-325361 | Primary key |
| `so_id` | text | 18,033 | 18,033 | SO-990591 | FK → sales_orders_header |
| `customer_id` | text | 18,033 | 500 | C0070 | FK → customers |
| `branch_id` | text | 18,033 | 6 | AHM001 | FK → branches |
| `invoice_date` | date | 18,033 | 2,203 | 2022-05-28 | Invoice date |
| `due_date` | date | 18,033 | 2,235 | 2022-06-27 | Payment due date |
| `total_order_value` | int | 18,033 | 16,248 | 1345720 | Ex-GST (₹) |
| `total_gst_amount` | float | 18,033 | 16,951 | 374439.6 | GST (₹) |
| `grand_total` | float | 18,033 | 16,938 | 1720159.6 | Incl. GST (₹) |
| `payment_status` | text | 18,033 | 3 | Unpaid | Paid · Partially Paid · Unpaid |

## `payments.csv` — Payments received against invoices

**Rows:** 19,257 · **Columns:** 5 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `payment_id` | text | 19,257 | 19,055 | PAY-207775 | Primary key |
| `invoice_id` | text | 19,257 | 16,036 | INV-786913 | FK → invoices |
| `payment_date` | date | 19,257 | 2,243 | 2023-10-07 | Payment date |
| `payment_amount` | float | 19,257 | 18,778 | 3354624.0 | Amount received (₹) |
| `payment_method` | text | 19,257 | 5 | Cheque | UPI · Credit Card · Bank Transfer · Cheque · Cash |

## `stock_ledger.csv` — Stock movement ledger — every IN / OUT / ADJUSTMENT per product × branch

**Rows:** 237,230 · **Columns:** 9 · **Nulls:** 0 · **Duplicate rows:** 0

| Column | Type | Non-null | Unique | Example | Description |
|---|---|---:|---:|---|---|
| `movement_id` | text | 237,230 | 237,230 | MOV-OUT-184742 | Primary key |
| `product_id` | text | 237,230 | 30 | P001 | FK → products |
| `branch_id` | text | 237,230 | 6 | AHM001 | FK → branches |
| `movement_type` | text | 237,230 | 3 | OUT | IN (PO receipt) · OUT (SO despatch) · ADJUSTMENT |
| `movement_date` | date | 237,230 | 2,218 | 2019-01-03 | Movement date |
| `quantity` | int | 237,230 | 300 | 8 | Units moved |
| `reference_type` | text | 237,230 | 3 | SO | PO · SO · ADJ |
| `reference_id` | text | 237,230 | 43,709 | SO-157767 | FK → PO / SO id |
| `running_balance` | int | 237,230 | 98,171 | 228 | Balance after movement |

## Join keys

| From | To | Key | Cardinality |
|---|---|---|---|
| `purchase_orders_lines` | `purchase_orders_header` | `po_id` | many→1 |
| `purchase_orders_header` | `suppliers` | `supplier_id` | many→1 |
| `purchase_orders_header` | `branches` | `branch_id` | many→1 |
| `purchase_orders_lines` | `products` | `product_id` | many→1 |
| `sales_orders_lines` | `sales_orders_header` | `so_id` | many→1 |
| `sales_orders_header` | `customers` | `customer_id` | many→1 |
| `sales_orders_header` | `branches` | `branch_id` | many→1 |
| `sales_orders_lines` | `products` | `product_id` | many→1 |
| `invoices` | `sales_orders_header` | `so_id` | 1→1 |
| `payments` | `invoices` | `invoice_id` | many→1 |
| `inventory_master` | `products + branches` | `product_id, branch_id` | 1→1 per pair |
| `stock_ledger` | `products + branches` | `product_id, branch_id` | many→1 |
| `stock_ledger` | `purchase_orders_header / sales_orders_header` | `reference_id` | many→1 |