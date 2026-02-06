def tax_compliance_checks(df, metrics):

    warnings = []

    if metrics["revenue"] > 4000000:
        warnings.append("Turnover exceeds GST registration threshold. GST registration may be required.")

    if "type" in df.columns:
        if (df["type"].str.lower() == "expense").any():
            warnings.append("Ensure expense invoices are properly maintained for GST and audit.")

    return warnings
