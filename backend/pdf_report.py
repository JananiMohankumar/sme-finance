from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from io import BytesIO


def generate_pdf_report(data: dict):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("SME Financial Health Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Business : {data['business_name']}", styles["Normal"]))
    elements.append(Paragraph(f"Industry : {data['industry']}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    m = data["metrics"]

    table_data = [
        ["Metric", "Value"],
        ["Revenue", m["revenue"]],
        ["Expenses", m["expenses"]],
        ["Profit", m["profit"]],
        ["Profit margin", f"{m['profit_margin']} %"],
        ["Receivable", m["receivable"]],
        ["Payable", m["payable"]],
        ["Credit score", data["credit_score"]]
    ]

    elements.append(Table(table_data))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("AI Report (English)", styles["Heading2"]))
    elements.append(Paragraph(data["report_en"], styles["Normal"]))

    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf
