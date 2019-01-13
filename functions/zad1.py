
liczby=[1,2,3,4]
liczby2=[4,5,6]
for i,l in enumerate(liczby):
    print(f"Index={i}, wartosc={l}")

def  czy(liczba):
    x=True
    for a in range(2,liczba):
        if liczba%a==0:
            x=False
    return(x)
print(czy(1), czy(14), czy(199))