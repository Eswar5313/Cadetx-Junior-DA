# Methodology Notes

## Data layer
* **Star schema** in `data/processed/`: fact_sales_lines, fact_po_lines, fact_stock_movements, fact_payments; dim_product, dim_branch, dim_supplier, dim_customer, dim_date.
* Cleaning rules live in `src/hwi/clean.py`; every rule has a unit test in `tests/`.

## Classification
* **ABC:** cumulative revenue share A ≤ 80 %, B ≤ 95 %, C > 95 %.
* **XYZ:** coefficient of variation of monthly demand X < 0.5, Y 0.5–1.0, Z > 1.0.
* **Fast/slow movers:** quartiles of monthly OUT velocity; dead stock = no OUT in 180 days.

## Inventory optimisation
* Reorder point `ROP = d̄ × L + SS`, safety stock `SS = z · σ_d · √L` (z = 1.65 for 95 % service).
* EOQ `√(2DS/H)` with S = ordering cost assumption (₹2,500/PO), H = 18 % of unit cost per year (documented in control book).

## Forecasting
* Baselines: naïve, seasonal-naïve, 3-month moving average.
* Models: Holt-Winters (statsmodels), Prophet, XGBoost with lag/rolling features.
* Split: train 2019–2023, test 2024; metric MAPE + RMSE per SKU × branch; report by ABC class.

## Stockout risk
* Target: balance ≤ reorder_level within next 30 days. Features: velocity, lead-time variance, supplier reliability, season, ABC class. Model: gradient-boosted classifier; evaluate AUC, precision@top-20.

## Customer analytics
* RFM on invoices (quintiles), K-means (k chosen by silhouette) for personas; churn = no order > 180 days; cohorts by `customer_since` quarter.

## Anomaly detection
* Isolation Forest on daily movement qty per product × branch; z-score > 3 flag; ADJUSTMENT spikes reviewed for shrinkage.
