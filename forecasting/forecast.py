import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for Flask apps

from statsmodels.tsa.holtwinters import ExponentialSmoothing
from prophet import Prophet

import io
import base64

def forecast_fuel_usage(df):
    # Ensure datetime index with daily frequency
    df.set_index('timestamp', inplace=True)
    df = df.asfreq('D')
    ts = df['fuel_consumption']

    # --- Holt-Winters Forecast Model---
    hw_model = ExponentialSmoothing(ts, trend='add', seasonal='add', seasonal_periods=7)
    hw_fit = hw_model.fit()
    hw_forecast = hw_fit.forecast(30)

    # --- Prophet Forecast ---
    prophet_df = df.reset_index().rename(columns={'timestamp': 'ds', 'fuel_consumption': 'y'})
    prophet_model = Prophet(daily_seasonality=True)
    prophet_model.fit(prophet_df)
    future = prophet_model.make_future_dataframe(periods=30)
    prophet_forecast = prophet_model.predict(future)
    prophet_forecast = prophet_forecast.set_index('ds')['yhat']

    # Plot actual and forecast
    plt.figure(figsize=(10, 4))
    plt.plot(ts, label='Actual', color='black')
    plt.plot(hw_forecast, label='Holt-Winters Forecast', color='red')
    plt.plot(prophet_forecast[-30:], label='Prophet Forecast', color='blue', linestyle='--')
    plt.title("Fuel Consumption Forecast: Holt-Winters vs Prophet")
    plt.legend()

    # Save plot to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return plot_base64
