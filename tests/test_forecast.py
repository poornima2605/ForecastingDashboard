from forecasting.forecast import forecast_fuel_usage

import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))


def test_forecast_output_type():
    df = pd.DataFrame({
        'timestamp': pd.date_range(start='2024-01-01', periods=60),
        'fuel_consumption': [10 + i*0.5 for i in range(60)]
    })
    result = forecast_fuel_usage(df)
    assert isinstance(result, str)  # Should return a base64 string
