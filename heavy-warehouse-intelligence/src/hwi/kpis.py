"""KPI calculators — IDs match docs/02_kpi_framework.md."""
import numpy as np
import pandas as pd
from .config import SERVICE_LEVEL_Z

def abc_class(so_lines: pd.DataFrame) -> pd.DataFrame:  # INV-08
    rev = so_lines.groupby("product_id")["line_total"].sum().sort_values(ascending=False)
    share = rev.cumsum() / rev.sum()
    return pd.DataFrame({"revenue": rev, "cum_share": share,
                         "abc": np.where(share <= 0.8, "A", np.where(share <= 0.95, "B", "C"))}).reset_index()

def supplier_otd(po: pd.DataFrame) -> pd.DataFrame:  # SUP-01..04
    r = po.assign(on_time=po["received_date"] <= po["expected_delivery_date"],
                  lead=(po["received_date"] - po["order_date"]).dt.days, cancelled=po["po_status"] == "Cancelled")
    return r.groupby("supplier_id").agg(po_count=("po_id", "count"), otd_pct=("on_time", "mean"),
                                        avg_lead=("lead", "mean"), lead_sd=("lead", "std"),
                                        cancel_rate=("cancelled", "mean"), spend=("grand_total", "sum")).reset_index()

def reorder_point(daily_demand: pd.Series, lead_time_days: float) -> tuple[float, float]:  # FC-02 / FC-03
    ss = SERVICE_LEVEL_Z * daily_demand.std() * np.sqrt(lead_time_days)
    return daily_demand.mean() * lead_time_days + ss, ss
