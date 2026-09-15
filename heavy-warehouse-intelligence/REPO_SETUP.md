# GitHub Repository Setup (copy-paste)

**Repository name:** `heavy-warehouse-intelligence`

**Description (≤350 characters):**
Team analytics portfolio for the CadetX Heavy Supplier, Inventory & Warehouse Analytics programme — 12 agile sprints turning 6 years of multi-branch spare-parts data (POs, sales, invoices, stock ledger) into KPI frameworks, inventory-health and supplier dashboards, demand forecasts, stockout-risk models and optimisation strategy.

**Topics:** `supply-chain` `inventory-analytics` `warehouse-management` `demand-forecasting` `data-science` `power-bi` `python` `pandas` `cadetx` `agile`

**Create & push (after creating the empty repo on GitHub):**
```bash
git remote add origin https://github.com/<org>/heavy-warehouse-intelligence.git
git branch -M main
git push -u origin main
git tag vWeek-01 && git push --tags
```
**Settings:** protect `main` (require 1 PR review) · enable Issues · enable Actions · add teammates as collaborators.
