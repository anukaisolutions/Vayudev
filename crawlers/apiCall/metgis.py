import requests 
# Make a get request to get the latest position of the international space station from the opennotify api.
key = "mD0yVm1yvZ8fdK3dibaZKprTz1rqNm13QECG2j40W4UgMaLB8"
lat = 30.7239
lon = 76.7896
alt = 1000
ver = "sum3"
url = "https://api.metgis.com/forecast?key="+key+"&lat="+(str)(lat)+"&lon="+(str)(lon)+"&alt="+(str)(alt)+"&v="+ver+"&lang=en"

response = requests.get(url)

sunrise = response.json().get('sunrise')
dayCount = response.json().get('dayCount')
weatherIcon = response.json().get('weatherIcon')
snowfall = response.json().get('snowfall')
unitLin = response.json().get('unitLin')
maxTemp = response.json().get('maxTemp')
description = response.json().get('description')
dateRequest = response.json().get('dateRequest')
windDir = response.json().get('windDir')
sunshineDuration = response.json().get('sumshineDuration')
precipitaton = response.json().get('precipitation')
windIcon = response.json().get('windIcon')
windSpeed = response.json().get('windSpeed')
lang = response.json().get('lang')
rainfall = response.json().get('rainfall')
unitWind = response.json().get('unitWind')
forecastIssued = response.json().get('forecastIssued')
minTemp = response.json().get('minTemp')
unitTemp = response.json().get('unitTemp')
sunset = response.json().get('sunset')
relativeHumidity = response.json().get('relativeHumidity')
forecastShortText = response.json().get('forecastShortText')


print(lat)
print(lon)
print(alt)
print(sunrise)
print(dayCount)
print(weatherIcon)
print(snowfall)
print(unitLin)
print(maxTemp)
print(description)
print(dateRequest)
print(windDir)
print(sunshineDuration)
print(precipitaton)
print(windIcon)
print(windSpeed)
print(lang)
print(rainfall)
print(unitWind)
print(forecastIssued)
print(minTemp)
print(unitTemp)
print(sunset)
print(relativeHumidity)
print(forecastShortText)


# print(response.content)
# print(response.headers)