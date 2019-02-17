import json

lista=[1,2,3,'a','b','c']

json_list = json.dumps(lista)

napis = '{"1":"a", "2" : "b"}'

ds_napis = json.loads(napis)

print(ds_napis)

ds_napis['3'] = "f"

print(ds_napis)


with open("napis.json", "w") as fp:
    json.dump(ds_napis, fp)

with open("napis.json") as fp:
    ob=json.load(fp)
    print(ob)
    print(type(ob))