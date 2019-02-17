import json
import getpass

while True:
#    slownik={}

    with open("employees.json") as fp:
        slownik= json.load(fp)
    print("co chcesz zrobic? (d-dodaj) (w-wypisz)")
    x=input()

    if x=='d':
        haslo = input("podaj haslo")

        print("imie:")
        imie=input()
        print("Nazwisko:")
        nazwisko=input()
        print("rok udrodzenia")
        rok=int(input())
        print("pensja")
        pensja=float(input())
        slownik[nazwisko]=[imie, rok,pensja]
    if x=='w':
        for i in slownik:
            print(f"imie ={slownik[i][0]} , nazwisko {slownik[i][0]}, rok= {slownik[i][0]}, pensja {slownik[i][0]}")

    with open("employees.json", "w") as fp:
        json.dump(slownik, fp)

