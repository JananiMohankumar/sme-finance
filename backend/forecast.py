import pandas as pd

def forecast_revenue(df, periods=3):
    # needs: date, amount, type

    if "date" not in df.columns:
        return {
            "enabled": False,
            "message": "No date column found. Forecast skipped."
        }

    try:
        df["date"] = pd.to_datetime(df["date"])

        revenue_df = df[df["type"].str.lower() == "revenue"]

        if revenue_df.empty:
            return {
                "enabled": False,
                "message": "No revenue rows found."
            }

        monthly = revenue_df.groupby(
            pd.Grouper(key="date", freq="M")
        )["amount"].sum().reset_index()

        # very simple forecast (average of last 3 months)
        last_values = monthly["amount"].tail(3)

        if len(last_values) == 0:
            return {
                "enabled": False,
                "message": "Not enough data for forecasting."
            }

        avg = float(last_values.mean())

        forecast = []
        last_date = monthly["date"].iloc[-1]

        for i in range(periods):
            last_date = last_date + pd.offsets.MonthEnd(1)
            forecast.append({
                "month": last_date.strftime("%Y-%m"),
                "forecast_revenue": round(avg, 2)
            })

        return {
            "enabled": True,
            "forecast": forecast
        }

    except Exception as e:
        return {
            "enabled": False,
            "message": str(e)
        }
