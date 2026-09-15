from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
TABLES = ["branches", "products", "suppliers", "customers", "inventory_master",
          "purchase_orders_header", "purchase_orders_lines", "sales_orders_header",
          "sales_orders_lines", "invoices", "payments", "stock_ledger"]
DATE_COLS = {"customers": ["customer_since", "last_purchase_date"], "products": ["last_purchase_date"],
             "purchase_orders_header": ["order_date", "expected_delivery_date", "received_date"],
             "sales_orders_header": ["order_date", "delivery_date"], "invoices": ["invoice_date", "due_date"],
             "payments": ["payment_date"], "stock_ledger": ["movement_date"]}
# Analysis constants (documented in control book › 03_KPI_Framework)
SERVICE_LEVEL_Z = 1.65      # 95 % service level
HOLDING_COST_RATE = 0.18    # 18 % of unit cost per year
ORDERING_COST_INR = 2500    # per PO
DEAD_STOCK_DAYS = 180
PALETTE = {"navy": "#1F2A44", "gold": "#C9A227", "grey": "#8A8F98", "green": "#2E7D32", "red": "#C62828"}
