import pandas as pd


def check_tax_compliance(df: pd.DataFrame):
    """
    Very simple rule based tax compliance checker
    """

    result = {
        "enabled": True,
        "issues": []
    }

    # Basic validation
    if "amount" not in df.columns or "type" not in df.columns:
        result["enabled"] = False
        result["issues"].append("Missing required columns for tax checking")
        return result

    # Check if revenue exists
    revenue_rows = df[df["type"].str.lower() == "revenue"]

    if revenue_rows.empty:
        result["issues"].append("No revenue records found – GST / sales tax may be missing")

    # Check negative values
    if (df["amount"] < 0).any():
        result["issues"].append("Negative transaction values found")

    # Check very large cash flow (dummy threshold)
    total_revenue = revenue_rows["amount"].sum()

    if total_revenue > 1_000_000:
        result["issues"].append("High revenue detected – verify GST filing and returns")

    return result


def tax_compliance_checks(df: pd.DataFrame, metrics: dict):
    """
    Soft warnings based on metrics
    """
    warnings = []

    profit_margin = metrics.get("profit_margin", 0)

    if profit_margin > 60:
        warnings.append("High profit margin – verify correct tax classification")

    if metrics.get("revenue", 0) == 0:
        warnings.append("Zero revenue detected – verify tax return data")

    return warnings
