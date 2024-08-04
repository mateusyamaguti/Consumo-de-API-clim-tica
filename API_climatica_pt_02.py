import requests

# response = requests.get('https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}')

# base_url = "https://api.openweathermap.org/data/2.5/weather?"
# api_key = "c79978fb9316323ead3852f42596a5c6" 
# city = "Leme"
# complete_url = f"{base_url}appid={api_key}&q={city}"
# response = requests.get(complete_url)
# temp = response.json()['main']['temp']
# print(f"{temp - 273.15:.2f}")

def get_weather_API(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "c79978fb9316323ead3852f42596a5c6" 
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()

def get_weather_temp(city):
    response = get_weather_API(city)
    temp = response['main']['temp'] - 273.15
    return round(temp,2)

def get_weather_main(city):
    response = get_weather_API(city)
    main = response['weather'][0]['main']
    return main

# print(get_weather_API("Osasco"))
# print(get_weather_temp("Leme"))
# print(get_weather_main("Leme"))
