import requests

city = 'Dallas'
url = 'http://api.weatherapi.com/v1/current.json?key=652d23b6e74c412f861192513242907&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')

# print(weather_json)
print(temp)

description = weather_json.get('current').get('condition').get('text')

print(description)

print("Today's weather in", city, "is", description, "and", temp, 'degrees')