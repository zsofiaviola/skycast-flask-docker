# SkyCast ⛅

**SkyCast** is a Flask-based, Dockerized weather application  
that displays the **current weather** and a **5-day forecast** using the OpenWeatherMap API.

---

## ✨ Features

- 🌡 **Current temperature**, humidity, wind speed, and pressure  
- 🌤 **Weather description** with icons  
- 📅 **5-day forecast**  
- 📱 **Responsive UI**  
- 🔑 **Environment variables** for secure API key storage  

---

## 🛠 Technologies Used

- [Flask](https://flask.palletsprojects.com/) – backend framework  
- [Docker](https://www.docker.com/) – containerization  
- [OpenWeatherMap API](https://openweathermap.org/api) – weather data  
- HTML, CSS, JavaScript – frontend  

---

## 📦 Installation (Python)

```bash
# Clone the repository
git clone https://github.com/zsofiaviola/skycast-flask-docker.git
cd skycast-flask-docker

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit the .env file and set your API key
# WEATHER_API_KEY=your_api_key_here

# Run the app
python app.py
```
--- 
## 🐳 Installation (Docker)
```bash
# Clone the repository
git clone https://github.com/zsofiaviola/skycast-flask-docker.git
cd skycast-flask-docker

# Create .env file from example
cp .env.example .env

# Edit the .env file and set your API key
# WEATHER_API_KEY=your_api_key_here

# Build the Docker image
docker build -t skycast .

# Run the container
docker run --env-file .env -p 5000:5000 skycast
```

📌 Notes
The .env file is ignored by Git (.gitignore) so your API key will not be uploaded to GitHub.

Make sure you have a valid API key from OpenWeatherMap.

The app runs on http://localhost:5000 by default.
