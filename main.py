from API_climatica_pt_02 import *

if __name__ == "__main__":
    city = input("Nome da cidade: ")
    get_weather_API(city)
    print(f"Temperatura atual: {get_weather_temp(city)}º")
    print(f"Clima atual: {get_weather_main(city)}")