lista=[]
for i in range(4):
    print('Podaj liczbe')
    x=int(input())
    lista.append(x)
#    lista.append(int(input()));
    print(sum(lista))
print("srednia wynosi: ", sum(lista)/len(lista))
dodatnia=0
ujemna=0
for liczba in lista:
    if liczba>=0:
        dodatnia+=1
    if liczba<0:
        ujemna+=1
print(dodatnia, ujemna)

dane=input("podaj liczby po spacji")
dane=dane.split()
print(dane)
#for d in dane:
#   dane2.appendint(d)


#dane=[int(d) for d in dane]

#dane=map(int, dane)
#list(dane)