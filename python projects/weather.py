import requests
import json

api_key = "d37f78971b1063ccf34a287df290899e"
base_url = "http://api.openweathermap.org/data/2.5/forecast?"

city_name = input("Enter city name: ")
forecast_days = int(input("Enter number of forecast days (max 5): "))

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&cnt=" + str(forecast_days)

response = requests.get(complete_url)

if response.status_code == 200:
    forecast_data = response.json()
    for forecast in forecast_data["list"]:
        weather_data = forecast["main"]
        temperature = weather_data["temp"]
        pressure = weather_data["pressure"]
        humidity = weather_data["humidity"]
        description = forecast["weather"][0]["description"]
        date_time = forecast["dt_txt"]
        print("\nDate/Time:", date_time,
              "\nTemperature (in kelvin unit):", temperature,
              "\nAtmospheric pressure (in hPa unit):", pressure,
              "\nHumidity (in percentage):", humidity,
              "\nDescription:", description)
        
        # check if it will rain in the next 2 hours
        if "rain" in description.lower() and "3 hour" in date_time:
            print("\nALERT: It will rain in the next 2 hours!")
else:
    print("City not found.")
