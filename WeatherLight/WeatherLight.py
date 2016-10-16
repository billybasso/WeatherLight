from phue import Bridge
import time
import forecastio

b = Bridge("192.168.0.107")

b.connect()

b.get_api()

b.set_light(3, 'on', True)
b.set_light(3, 'sat', 255)
b.set_light(3, 'bri', 255)
b.set_light(2, 'on', True)
b.set_light(2, 'sat', 255)
b.set_light(2, 'bri', 255)

counter = 0

api_key = "14240dd5d3bf601df4eb9fee104134cc"
lat = 41.909506
lng = -87.685113

forecast = forecastio.load_forecast(api_key, lat, lng,time=None, units="us")
current = forecast.currently()
currentTemp = current.temperature
condition = current.icon

#icons
icon_clear_day = "clear-day"
icon_rain = "rain"
icon_snow = "snow"
icon_sleet = "sleet"
icon_wind = "wind"
icon_fog = "fog"
icon_cloudy = "cloudy"
icon_partly_cloudy_day = "partly-cloudy-day"

# for min1 in byHour.data:
#     print(min1.temperature)
print(current.icon)

red = 2000 #100+ sleet
orange = 10000 #80-100 clear-day
yellow = 20000 #70-80 partly-cloudy
green = 30000 #60-70 cloudy
blueGreen = 40000 #50-60 fog wind
blue = 45000 #30-50 rain
purple = 50000 #30- snow


if (condition == icon_clear_day):
    b.set_light(2, 'hue', orange)
elif (condition == icon_partly_cloudy_day):
    b.set_light(2, 'hue', yellow)
elif (condition == icon_cloudy):
    b.set_light(2, 'hue', green)
elif (condition == icon_fog or condition == icon_wind):
    b.set_light(2, 'hue', blueGreen)
elif (condition == icon_rain):
    b.set_light(2, 'hue', blue)
elif (condition == icon_sleet):
    b.set_light(2, 'hue', red)
else:
    b.set_light(2, 'hue', purple)


if (currentTemp > 100):
    b.set_light(3, 'hue', red)
elif (currentTemp > 80 and currentTemp < 100):
    b.set_light(3, 'hue', orange)
elif (currentTemp > 70 and currentTemp < 80):
    b.set_light(3, 'hue', yellow)
elif (currentTemp > 60 and currentTemp < 70):
    b.set_light(3, 'hue', green)
elif (currentTemp > 50 and currentTemp < 60):
    b.set_light(3, 'hue', blueGreen)
elif (currentTemp > 30 and currentTemp < 50):
    b.set_light(3, 'hue', blue)
else:
    b.set_light(3, 'hue', purple)

if (currentTemp < 0):
    while(counter < 1000) :
        if(counter % 2 == 0):
            b.set_light(3, 'bri', 0, transitiontime=0.01)
        else :
            b.set_light(3, 'bri', 255, transitiontime=0.01)
        counter += 1
        print(counter)
        time.sleep(0.05)

