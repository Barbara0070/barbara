import requests
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
nothing="12345"
resp = requests.get(url.format(nothing))
print(dir(resp))
nothing=int(resp.text.split()[-1])
#http://www.pythonchallenge.com/pc/def/peak.html 

