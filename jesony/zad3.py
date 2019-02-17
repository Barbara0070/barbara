import requests
import sys
from collections import namedtuple

# Weather = namedtuple("weather", [location,])
#
# weather = Weather(
#     location=resp.json()['title'],
#     temperature= resp_json['the temp']
#
# )
import json
miasto=sys.argv[1]
resp=requests.get("https://www.metaweather.com/api/location/search/?query="+miasto)
id=resp.json()[0]["woeid"]
resp=requests.get("https://www.metaweather.com/api/location/"+str(id))
temp=resp.json()["consolidated_weather"][0]["the_temp"]
print(temp)