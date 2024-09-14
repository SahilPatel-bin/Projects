# Weather Forecast

This Python code fetches weather data from the OpenWeatherMap API, either by city name or by ZIP code and country code. It uses the requests library to make HTTP requests to the API and 
returns the current weather details in metric units (Celsius).

Workflow:
1) User chooses between city name or ZIP code to search for weather.
2) The program constructs a URL with the API key and makes an API call.
3) It retrieves and displays weather information (temperature, condition, humidity, wind speed) or an error message if the request fails.
