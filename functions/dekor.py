def pobierz():
    print("pobralem dane")
def loguj(func):
    """
    dekorator
    :param func:
    :return:
    """
    def wrapper(*args,**kwargs):
#       print("to sie wykona przed")
        func(*args,*kwargs)
#        print("to sie wykona po")
        return f"Wynik: {func(*args,**kwargs)}"
    return wrapper
@loguj
def potega(podstawa,wykladnik):
    wynik=podstawa**wykladnik
    print(wynik)
    return wynik
#print("bez dekoratora")
#pobierz()
#print ("z dekoratorem")
#loguj(pobierz())
#print(potega(2,4))
loguj(potega(2,4))
potega(2,4)