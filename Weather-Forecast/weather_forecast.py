import requests

def get_weather(api_key, zip_code=None, country_code='in', city_name=None):
    url = f"http://api.openweathermap.org/data/2.5/weather"

    params = {
            'appid': api_key,
            'units': 'metric'
            }
    
    if city_name:   
        params['q'] = city_name
        
    else : 
        params['zip'] = f"{zip_code},{country_code}"

    response = requests.get(url,params=params)

    if response.status_code == 200 :
        data = response.json()
        
        print(f"\nWeather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']["speed"]} m/s")

    else :
        data = response.json()
        print(data)
        print(f"Error: {data['message']}")

api_key = "0c78d22b26bc564b0ba34638e431ba8f"
choice = int(input("If you search weather by city enter 1 or otherwise enter 2:- "))

if choice==1:
    city_name =input("Enter the city name: ")
    get_weather(api_key,city_name=city_name)
else:
    zip_code = input("Enter your ZIP code (e.g., 382845): ")
    country_code = input("Enter your country code (default is 'in'): ")
    get_weather(api_key,zip_code,country_code)


