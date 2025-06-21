from flask import Flask, request, render_template
import pandas as pd
from forecast import forecast_fuel_usage

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    forecast_plot = None
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file, parse_dates=['timestamp'])
        forecast_plot = forecast_fuel_usage(df)
    return render_template('index.html', plot=forecast_plot)

if __name__ == '__main__':
    app.run(debug=True)
