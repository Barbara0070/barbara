import requests
import urlib.parse
x=urlib.parse.urlparse("https://www.metaweather.com/api/location/search/?query")
resp = requests.get("https://www.metaweather.com/api/location/search/?query")
print resp