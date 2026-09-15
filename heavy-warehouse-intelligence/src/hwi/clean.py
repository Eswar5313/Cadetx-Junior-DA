"""Cleaning & validation rules (see docs/03_data_quality_report.md for IDs)."""
import pandas as pd

def reconcile_stock(inventory: pd.DataFrame, ledger: pd.DataFrame) -> pd.DataFrame:
    """DQ-002 / RSK-01: compare inventory_master.current_stock with last ledger running_balance."""
    last = (ledger.sort_values("movement_date").groupby(["product_id", "branch_id"])["running_balance"].last()
            .rename("ledger_balance").reset_index())
    out = inventory.merge(last, on=["product_id", "branch_id"], how="left")
    out["reconciliation_gap"] = out["current_stock"] - out["ledger_balance"]
    return out

def ledger_continuity(ledger: pd.DataFrame) -> pd.DataFrame:
    """DQ-007: balance(t) should equal balance(t-1) + signed qty."""
    df = ledger.sort_values(["product_id", "branch_id", "movement_date", "movement_id"]).copy()
    sign = df["movement_type"].map({"IN": 1, "OUT": -1, "ADJUSTMENT": 1})
    df["expected"] = df.groupby(["product_id", "branch_id"])["running_balance"].shift() + sign * df["quantity"]
    df["break"] = df["expected"].notna() & (df["expected"] != df["running_balance"])
    return df[df["break"]]
