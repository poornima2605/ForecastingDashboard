import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for Flask apps

from statsmodels.tsa.holtwinters import ExponentialSmoothing
import io
import base64

def forecast_fuel_usage(df):
    # Ensure datetime index with daily frequency
    df.set_index('timestamp', inplace=True)
    df = df.asfreq('D')

    # Forecasting
    ts = df['fuel_consumption']
    model = ExponentialSmoothing(ts, trend='add', seasonal='add', seasonal_periods=14)
    fit = model.fit()
    forecast = fit.forecast(30)

    # Plot actual and forecast
    fig, ax = plt.subplots(figsize=(10, 4))
    ts.plot(ax=ax, label='Actual')
    forecast.plot(ax=ax, label='Forecast', color='red')
    ax.set_title("Fuel Consumption Forecast")
    ax.legend()

    # Save plot to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)

    return plot_base64
