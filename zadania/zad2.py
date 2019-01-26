def suma(a):
    if type(a)=="dictionary":
        a=a.values()
    if type(a)=="tuple" or type(a)=="list":
        suma=0
        for liczba in a:
            try:
                x=int(x)
                suma+=liczba
            except ValueError:
                continue
        return sum(a)
print(suma([1,2,3]))