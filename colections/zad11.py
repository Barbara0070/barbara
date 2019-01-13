liczby=set()
parzyste=set(range(0,101,2))
print(parzyste)
while(True):
    print("podaj liczbe q to koniec")
    a=input()
    if a=='q':
        break
    a=int(a)
    liczby.add(a)
    print(liczby)
iloczyn=parzyste&liczby
print("unikalne liczby", liczby.__len__())
print("parzyste w zakresie", iloczyn.__len__())
