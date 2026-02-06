def recommend_products(metrics, credit_score):

    products = []

    if credit_score >= 80 and metrics["profit_margin"] >= 20:
        products.append("Working capital loan")

    if metrics["receivable"] > metrics["payable"]:
        products.append("Invoice discounting")

    if credit_score < 60:
        products.append("Micro business loan")

    if not products:
        products.append("Basic current account + overdraft")

    return products
