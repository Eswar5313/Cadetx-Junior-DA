"""Typed loaders for the 12 raw tables. `python -m hwi.load --check` validates keys."""
import sys
import pandas as pd
from .config import RAW, TABLES, DATE_COLS

def load(table: str) -> pd.DataFrame:
    df = pd.read_csv(RAW / f"{table}.csv", parse_dates=DATE_COLS.get(table, []))
    money = [c for c in df.columns if c.endswith(("_total", "_amount", "_cost", "_value", "_price")) and df[c].dtype == float]
    df[money] = df[money].round(2)
    if table == "branches":
        df["capacity_sqft"] = df["warehouse_capacity"].str.replace(" sqft", "").astype(int)
    return df

def load_all() -> dict[str, pd.DataFrame]:
    return {t: load(t) for t in TABLES}

def check(db: dict[str, pd.DataFrame]) -> list[str]:
    issues = []
    fks = [("purchase_orders_header", "supplier_id", "suppliers"), ("purchase_orders_header", "branch_id", "branches"),
           ("purchase_orders_lines", "po_id", "purchase_orders_header"), ("purchase_orders_lines", "product_id", "products"),
           ("sales_orders_header", "customer_id", "customers"), ("sales_orders_header", "branch_id", "branches"),
           ("sales_orders_lines", "so_id", "sales_orders_header"), ("sales_orders_lines", "product_id", "products"),
           ("invoices", "so_id", "sales_orders_header"), ("payments", "invoice_id", "invoices"),
           ("stock_ledger", "product_id", "products"), ("stock_ledger", "branch_id", "branches")]
    for child, key, parent in fks:
        orphans = (~db[child][key].isin(db[parent][key])).sum()
        if orphans:
            issues.append(f"{child}.{key}: {orphans} orphan rows vs {parent}")
    return issues

if __name__ == "__main__":
    db = load_all()
    for t, df in db.items():
        print(f"{t:26s} {len(df):>9,} rows  {df.shape[1]:>2} cols")
    if "--check" in sys.argv:
        problems = check(db)
        print("FK integrity:", "OK" if not problems else problems)
        sys.exit(1 if problems else 0)
