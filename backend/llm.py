import os
import json
from openai import OpenAI

_client = None


def get_client():
    """
    Create OpenAI client only when needed.
    If API key is missing, return None instead of crashing.
    """
    global _client

    if _client is not None:
        return _client

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    _client = OpenAI(api_key=api_key)
    return _client


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

    client = get_client()

    # ✅ Safe fallback when API key is not configured
    if client is None:
        return (
            "AI report is temporarily unavailable because the AI service "
            "is not configured. Financial metrics and risk analysis were "
            "generated successfully."
        )

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

    client = get_client()

    # ✅ Safe fallback when API key is not configured
    if client is None:
        return (
            "एआई सेवा कॉन्फ़िगर नहीं की गई है। इसलिए हिंदी रिपोर्ट उपलब्ध नहीं है।"
        )

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
