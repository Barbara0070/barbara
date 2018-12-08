miastoa=input("nazwa miasta1")
miastob=input("nazwamiasta2")
dystans=int(input("podaj dystans"))
cena=int(input("podaj cene paliwa"))
spalanie=int(input("podaj spalanie"))
info=f"""
Koszt przejazdu {miastoa}:{miastob} to {dystans/100*spalanie*cena}
"""
print(info)