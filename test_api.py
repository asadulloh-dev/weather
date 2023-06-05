import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Tashkent&appid=88b59c7fabe26846b93db19938a7d260")

data = response.json()
temp_celsium = data['main']['temp']-273.15
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
long = data['coord']['lon']
lat = data['coord']['lat']
print(temp_celsium)
print(humidity)
print(wind_speed)
print(long)
print(lat)
print(data)
