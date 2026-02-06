from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def _extract_text(response):
    """
    Safely extract text from OpenAI Responses API output.
    """
    try:
        return response.output[0].content[0].text
    except Exception:
        return str(response)


def generate_financial_report(
    business_name: str,
    industry: str,
    metrics: dict,
    risks: list,
    credit_score: int
):

    prompt = f"""
You are a professional financial advisor for Small and Medium Enterprises (SMEs).

Business name: {business_name}
Industry: {industry}

Financial metrics (JSON):
{json.dumps(metrics, indent=2)}

Identified risks:
{risks}

Credit score:
{credit_score}

Generate a clear and simple report for a non-finance business owner.

The report must contain:

1. Financial health summary
2. Key performance indicators explained simply
3. Main risks and why they matter
4. Cost optimisation suggestions
5. Working capital improvement suggestions
6. Short creditworthiness assessment
7. 3 practical next steps

Keep the language simple and business friendly.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return _extract_text(response)


def translate_to_hindi(english_report: str):

    prompt = f"""
Translate the following financial report into simple Hindi
suitable for small business owners in India.

Report:
{english_report}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return _extract_text(response)
