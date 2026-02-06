def auto_bookkeeping(df):

    if "description" not in df.columns:
        return {
            "enabled": False,
            "message": "No description column found."
        }

    categories = []

    for text in df["description"].fillna("").str.lower():

        if "rent" in text:
            categories.append("Rent")
        elif "electric" in text or "power" in text:
            categories.append("Utilities")
        elif "salary" in text or "wage" in text:
            categories.append("Payroll")
        elif "transport" in text or "fuel" in text:
            categories.append("Logistics")
        elif "amazon" in text or "purchase" in text:
            categories.append("Office Supplies")
        else:
            categories.append("Other")

    df["auto_category"] = categories

    summary = df["auto_category"].value_counts().to_dict()

    return {
        "enabled": True,
        "category_summary": summary
    }
