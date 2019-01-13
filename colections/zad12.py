tablica=[2,231,124,121,15,123,124,153,6734,321,61236,123,4,5,1]
min=0
b=0
for b in range(len(tablica)):
    min=b
    for a in range(b,len(tablica)):
        if tablica[a]<tablica[min]:
            min=a

    tablica[b], tablica[min] = tablica[min], tablica[b]
    print(tablica)