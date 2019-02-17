import json
import requests
resp=requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")
#sprawdza czy status = 200
resp.raise_for_status()

#with open("waluty.json", "w") as file:
#    json.dump(resp,file)
kursy=resp.json()[0]['rates']
#type employees.json | python
for i in kursy:
    if i['currency'] == "euro":
        print(i)

for k in kursy:
    if k["code"]==waluta:
        printf(f"za {za_ile}")