import pandas as pd

def analyze_financials(df):

    df["type"] = df["type"].astype(str).str.strip().str.lower()

    revenue = df[df["type"] == "revenue"]["amount"].sum()
    expenses = df[df["type"] == "expense"]["amount"].sum()
    receivable = df[df["type"] == "receivable"]["amount"].sum()
    payable = df[df["type"] == "payable"]["amount"].sum()

    profit = revenue - expenses

    profit_margin = 0
    if revenue != 0:
        profit_margin = (profit / revenue) * 100

    metrics = {
        "revenue": float(revenue),
        "expenses": float(expenses),
        "profit": float(profit),
        "profit_margin": round(profit_margin, 2),
        "receivable": float(receivable),
        "payable": float(payable)
    }

    score = 100

    if profit_margin < 10:
        score -= 20
    if payable > receivable:
        score -= 15
    if expenses > revenue:
        score -= 30

    risks = []

    if profit < 0:
        risks.append("Negative profit")

    if payable > receivable:
        risks.append("High outstanding payables")

    if profit_margin < 10:
        risks.append("Low profit margin")

    return metrics, risks, score
