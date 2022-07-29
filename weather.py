#temp = 50

#if temp > 80 or temp < 60:
  #  print(" stay inside!")


#else :
 #   print("enjoy the outdoors!")

#print('have a good day')


import requests

api_key = 'b9a6630ad755ef9c5da0db994918d545'
city = 'Orlando'

url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
request = requests.get(url)
json = request.json()
#print(json)


description = json.get("weather")[0].get("description")

temp_min = json.get("main").get("temp_min")
temp_max = json.get("main").get("temp_max")

print("the low for today is", temp_min)
print("the high for today is", temp_max)
print("todays forecast is", description)