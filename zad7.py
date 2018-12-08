x=int(input("podaj liczbe: "))
info=f"""
podzielna przez : {x%2==0}
podzielna przez 3 i wieksza od 10 albo jest 7: {(x%3==0 and x>10) or x==7}
"""
print(f" abc {info}")