#for k , v in slownik.items()
#for k in slownik:
#    print(k,slownik[k])
#    slownik.get('a')
#    slownik.get('a',0) #wez i nadpisz
#slownik = {}
#while(True):
#    print("podaj nazwe, c to koniec")
#    nazwa=input()
#    if nazwa=="c":
#        break
#    print("podaj cene")
#    cena=input()
#    slownik[nazwa]=cena
#print(slownik)
slownik={
    "ziemniaki":10,
    "chleb":15,
    "woda":20,
}
stan={
    "ziemniaki":1,
    "chleb":1,
    "woda":1
}
#try: except ValueError:
#rola=input("czy kestes k czy d")
#if rola.lower() in ['klient', k]:...
#elif rola.lower() in ['dostawca', d]:

while(True):
    print("jaki towar chcesz dodac i ile sztuk/kg (nazwa ilosc cena)")
    dododania=input()
    nazwa, ilosc, cena=dododania.split()
    ilosc=float(ilosc)
    cena=float(cena)
    print(ilosc, cena, nazwa)
    if nazwa in slownik:
        slownik[nazwa]=cena
        stan[nazwa]+=ilosc
        print(stan)
        continue
#    magazyn[nazwa] =magazyn.get(nazwa,0) + ilosc get zwraca nazwa gdy istnieje, zwraca 0 gdy nie istnieje
    else:
        slownik[nazwa]=cena
        stan[nazwa]=ilosc
#while(True):
#    print("co chcesz kupic")
#    zakup=input()
#    if zakup in slownik.keys():
#        print("ile kg")
#        ilosc=int(input())
#        if ilosc>stan[zakup]:
#            print("braki na stanie")
#        stan[zakup]-=ilosc
#        print(stan[zakup])
#        print("zaplacisz", slownik[zakup]*ilosc)