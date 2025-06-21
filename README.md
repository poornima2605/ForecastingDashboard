# 🚀 Engine Fuel Usage Forecasting Dashboard

A lightweight web-based dashboard built with **Flask** that allows users to upload engine usage data and view **fuel consumption forecasts** using two time-series models:

- Holt-Winters Exponential Smoothing
- Facebook Prophet

This tool helps visualize and compare short-term fuel usage trends, aiding in predictive maintenance, planning, and optimization.

---

## 📊 Features

- Upload your CSV data file
- Visualize actual vs forecasted fuel consumption
- Compare predictions from:
  - Holt-Winters model
  - Prophet model
- Clean and simple interface

---

## 📁 Project Structure

     ├── app.py 
     ├── forecast.py 
     ├── templates/
     │ └── index.html 
     ├── data/
     │ └── simulated_engine_usage.csv 
     ├── README.md 


---

## 🛠 Usage

1. Clone the repo
2. Install requirements.txt
3. Run the app using:
   python app.py
4. Then open your browser and visit:
   http://127.0.0.1:5000/


Sample output:

![output](https://github.com/poornima2605/ForecastingDashboard/blob/main/data/Dashboard.png)
