"""Feature engineering helpers used by notebooks and models."""
import pandas as pd

def po_lead_times(po: pd.DataFrame) -> pd.DataFrame:
    r = po[po["po_status"] == "Received"].copy()
    r["actual_lead_days"] = (r["received_date"] - r["order_date"]).dt.days
    r["promised_lead_days"] = (r["expected_delivery_date"] - r["order_date"]).dt.days
    r["on_time"] = r["received_date"] <= r["expected_delivery_date"]
    return r

def monthly_demand(so_lines: pd.DataFrame, so_header: pd.DataFrame) -> pd.DataFrame:
    d = so_lines.merge(so_header[so_header["order_status"] == "Delivered"][["so_id", "branch_id", "order_date"]], on="so_id")
    d["month"] = d["order_date"].dt.to_period("M").dt.to_timestamp()
    return d.groupby(["product_id", "branch_id", "month"])["quantity"].sum().reset_index()

def rfm(invoices: pd.DataFrame, asof: str = "2025-01-31") -> pd.DataFrame:
    asof = pd.Timestamp(asof)
    g = invoices.groupby("customer_id").agg(recency=("invoice_date", lambda s: (asof - s.max()).days),
                                            frequency=("invoice_id", "count"), monetary=("grand_total", "sum"))
    for c, asc in [("recency", False), ("frequency", True), ("monetary", True)]:
        g[c[0].upper()] = pd.qcut(g[c].rank(method="first", ascending=asc), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    g["rfm_score"] = g["R"] + g["F"] + g["M"]
    return g.reset_index()
