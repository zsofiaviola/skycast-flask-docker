# Weather App 🌤️

A simple Flask-based Weather App that displays **current weather** and a **5-day forecast** using the OpenWeatherMap API.

## Features
- 🌡️ Current temperature, humidity, wind speed, and pressure
- 🌤️ Weather description with icons
- 📅 5-day forecast
- 📱 Responsive UI
- 🔑 Environment variables for API key security

## Installation (Python)
```bash
# Clone the repository
git clone https://github.com/yourusername/weather-app.git
cd weather-app

# Install dependencies
pip install -r requirements.txt

# Create environment file and add your API key
cp .env.example .env
# Edit .env and set WEATHER_API_KEY=your_api_key_here

# Run the app
python app.py
