import pandas as pd
from forecast import forecast_fuel_usage


def test_forecast_output_type():
    df = pd.DataFrame({
        'timestamp': pd.date_range(start='2024-01-01', periods=60),
        'fuel_consumption': [10 + i*0.5 for i in range(60)]
    })
    result = forecast_fuel_usage(df)
    assert isinstance(result, str)  # Should return a base64 string
