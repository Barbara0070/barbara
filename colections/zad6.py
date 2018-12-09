dane=input("podaj liczby po spacji")
dane=dane.split()
dane=[int(d) for d in dane]
print(dane)
min=dane[0]
max=dane[0]
indxmax=0
indxmin=0
for i in range(len(dane)):
    if dane[i]<min:
        indxmin=i
        min=dane[i]
    if dane[i]>max:
        indxmax=i
        max=dane[i]
tymczasowa=min
dane[indxmin]=max
dane[indxmax]=tymczasowa
print(dane)
#liczby[0],liczby[2] =liczby[2], liczby[0]