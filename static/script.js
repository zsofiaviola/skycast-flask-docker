// Function to fetch and display weather data
function getWeather() {
    // Get the city 
    const city = document.getElementById("city").value;

    // Send a request to the /weather endpoint with the city as a query parameter
    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            // If there's an error (e.g., city not found), display the error message
            if (data.error) {
                document.getElementById("weather-result").innerHTML = `<p>${data.error}</p>`;
                return;
            }

            // ===== CURRENT WEATHER SECTION =====
            // Populate the "Current Weather" area with data from the API
            document.getElementById("weather-result").innerHTML = `
                <h2>${data.city}, ${data.country}</h2>
                <p>Temperature: ${data.temp}°C</p>
                <p>Feels like: ${data.feels_like}°C</p>
                <p>Weather: ${data.description}</p>
                <p>Humidity: ${data.humidity}%</p>
                <p>Pressure: ${data.pressure} hPa</p>
                <p>Wind: ${data.wind} m/s</p>
                <img src="http://openweathermap.org/img/wn/${data.icon}@2x.png">
            `;

            // ===== FORECAST SECTION =====
            // Create the HTML structure for the 5-day forecast
            let forecastHTML = "<h3 class='forecast-title'>5-Day Forecast:</h3><div class='forecast-container'>";

            // Loop through each forecast item and create a forecast card
            data.forecast.forEach(item => {
                forecastHTML += `
                    <div class="forecast-card">
                        <p><b>${item.day}</b></p>
                        <img src="http://openweathermap.org/img/wn/${item.icon}@2x.png">
                        <p>${item.temp}°C</p>
                        <p>${item.description}</p>
                        <p>Humidity: ${item.humidity}%</p>
                        <p>Pressure: ${item.pressure} hPa</p>
                        <p>Wind: ${item.wind} m/s</p>
                    </div>
                `;
            });

            // Close the forecast container div
            forecastHTML += "</div>";

            // Insert the forecast HTML into the page
            document.getElementById("forecast-result").innerHTML = forecastHTML;
        });
}
