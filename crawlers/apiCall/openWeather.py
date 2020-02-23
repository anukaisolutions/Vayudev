import requests
key = "29d82cbfe71ac2746d1af20dffd66b23"
lat = str(30.723)
lon = str(76.789)

url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="+key
url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&APPID="+key

response = requests.get(url)

id1 = response.json().get("weather")[0].get("id")
main = response.json().get("weather")[0].get("main")
description = response.json().get("weather")[0].get("description")
icon = response.json().get("weather")[0].get("icon")

temp = response.json().get("main").get("temp")
pressure = response.json().get("main").get("pressure")
humidity = response.json().get("main").get("humidity")
temp_min = response.json().get("main").get("temp_min")
temp_max = response.json().get("main").get("temp_max")

visibility = response.json().get("visibility")
speed = response.json().get("wind").get("speed")
deg = response.json().get("wind").get("deg")

clouds = response.json().get("clouds").get("all")
dt = response.json().get("dt")
typ = response.json().get("sys").get("type")
id = response.json().get("sys").get("id")
message = response.json().get("sys").get("message")
country = response.json().get("sys").get("country")
sunrise = response.json().get("sys").get("sunrise")
sunset = response.json().get("sys").get("sunset")
idn = response.json().get("id")
name = response.json().get("name")

print(lat)
print(lon)
print(id1)
print(main)
print(description)
print(icon)
print(temp)
print(pressure)
print(humidity)
print(temp_min)
print(temp_max)
print(visibility)
print(speed)
print(deg)
print(clouds)
print(dt)
print(typ)
print(id)
print(message)
print(country)
print(sunrise)
print(sunset)
print(idn)
print(name)

# print(url)