BENCHMARKS = {
    "Retail": {
        "avg_profit_margin": 12
    },
    "Manufacturing": {
        "avg_profit_margin": 15
    },
    "Services": {
        "avg_profit_margin": 18
    },
    "Agriculture": {
        "avg_profit_margin": 10
    }
}

def compare_with_benchmark(metrics, industry):

    if industry not in BENCHMARKS:
        return {
            "enabled": False,
            "message": "No benchmark available for this industry"
        }

    industry_avg = BENCHMARKS[industry]["avg_profit_margin"]
    your_margin = metrics.get("profit_margin", 0)

    return {
        "enabled": True,
        "industry_avg_profit_margin": industry_avg,
        "your_profit_margin": your_margin,
        "performance":
            "Above industry average" if your_margin >= industry_avg
            else "Below industry average"
    }
