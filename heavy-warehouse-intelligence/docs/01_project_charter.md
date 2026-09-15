# Project Charter — Heavy Warehouse Intelligence

| Item | Detail |
|---|---|
| Programme | CadetX Virtual Work Experience — Data Analytics & Data Science |
| Project | Heavy Supplier, Inventory & Warehouse Analytics |
| Duration | 12 weekly sprints (3 months) · kick-off Week 1: 14 Sep 2026 |
| Team | 2 × Data Analyst, 1 × Data Scientist (rotating Scrum Master) |
| Sponsor (simulated) | Head of Supply Chain & Operations |
| Deliverable | GitHub portfolio: cleaned data layer, KPI framework, 5 BI dashboards, forecasting & stockout-risk models, strategy recommendations, final presentation |

## Problem statement
Warehouse and supply-chain teams operate reactively on manual reports and intuition, producing excess inventory, frequent stockouts, poor space usage and delayed decisions.

## Objective
Build a unified analytics framework that uses six years of warehouse and supplier history to **analyse, predict and optimise** product movement, inventory levels and warehouse performance.

## Scope
**In:** 6 branches, 30 SKUs, 8 suppliers, 500 customers, 2019–2024 transactions; descriptive, diagnostic, predictive and prescriptive analytics; Power BI/Plotly dashboards.
**Out:** live ERP integration, pricing strategy, HR analytics, real-time alerting infrastructure.

## Success criteria
1. Every KPI in `02_kpi_framework.md` computed, validated and visualised.
2. Demand forecast MAPE ≤ 20 % on 2024 hold-out for A-class SKUs.
3. Stockout-risk classifier AUC ≥ 0.80.
4. Quantified savings case: capital release, stockout reduction, supplier cost avoidance (₹ Cr).
5. 12 / 12 weekly GitHub submissions with sprint notes.

## Stakeholders & decisions supported
| Stakeholder | Decision |
|---|---|
| Warehouse Manager | What to move, bin, count, write off |
| Procurement Lead | Whom to order from, how much, when |
| Planning Analyst | Reorder points, safety stock, forecasts |
| Finance Controller | Working capital, DSO, credit exposure |
| Sales Head | Which customers to retain, upsell, chase |

## Risks
| Risk | Mitigation |
|---|---|
| `current_stock` inconsistent with ledger | Treat ledger as source of truth; document reconciliation |
| Single-country supplier base | Model duty / lead-time shocks in scenario forecasting |
| Team availability | Rotating SM + shared task board in control book |
| Scope creep from open catalogue | Lock sprint goal Monday; park extras in backlog sheet |
