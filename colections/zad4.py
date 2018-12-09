lista=[]
for i in range(101):
    if i%3==0 or i%5==0:
        lista.append(i)
print("liczby podzielne przez 3 i 5")
for liczba in lista:
    print(liczba)
print(f"w przedziale jest{len(lista)} liczb")