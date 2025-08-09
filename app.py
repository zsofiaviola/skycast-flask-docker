from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Get the OpenWeatherMap API key from environment variables
API_KEY = os.getenv("WEATHER_API_KEY")

@app.route("/")
def home():
    """
    Render the home page (index.html).
    """
    return render_template("index.html")

@app.route("/weather")
def weather():
    """
    Endpoint to fetch current weather and 5-day forecast for a given city.
    Returns data in JSON format.
    """
    # Get the city from query parameters
    city = request.args.get("city")

    # Check if API key is available
    if not API_KEY:
        return jsonify({"error": "API key not found"})

    # API request for current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    # Handle invalid city or API errors
    if res.get("cod") != 200:
        return jsonify({"error": res.get("message", "City not found")})

    # Extract relevant current weather data
    current_data = {
        "city": res["name"],
        "country": res["sys"]["country"],
        "temp": res["main"]["temp"],
        "feels_like": res["main"]["feels_like"],
        "description": res["weather"][0]["description"].title(),
        "humidity": res["main"]["humidity"],
        "pressure": res["main"]["pressure"],
        "wind": res["wind"]["speed"],
        "icon": res["weather"][0]["icon"]
    }

    # API request for 5-day weather forecast
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    forecast_res = requests.get(forecast_url).json()

    forecast_list = []  # Store forecast data
    seen_dates = set()  # Track which days we've already added

    # Loop through forecast data and select only one entry per day (12:00)
    for item in forecast_res["list"]:
        date_obj = datetime.fromtimestamp(item["dt"])
        date_str = date_obj.strftime("%A")  # Day name

        if date_str not in seen_dates and date_obj.hour == 12:
            forecast_list.append({
                "day": date_str,
                "temp": item["main"]["temp"],
                "description": item["weather"][0]["description"].title(),
                "humidity": item["main"]["humidity"],
                "pressure": item["main"]["pressure"],
                "wind": item["wind"]["speed"],
                "icon": item["weather"][0]["icon"]
            })
            seen_dates.add(date_str)

    # Add forecast to current weather data
    current_data["forecast"] = forecast_list

    # Return combined current weather + forecast data
    return jsonify(current_data)

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 so it is accessible in Docker
    app.run(host="0.0.0.0", port=5000)
