#def wypisz(*args, **kwargs):
#    print(f"argumenty niekluczowe: {args}")
#    print(f"argumenty kluczowe: {kwargs}")
#
#
#wypisz("wdadwadfawf", "wawaffgafwaf", zmienna=10)
#
#"ala ma kota".replace("ala", "kasia")
def formatuj(*napisy, **liczba):
    x="\n".join(napisy)

    print(f"{x}\n{liczba}")
    for i in liczba:
        kwota=liczba[i]
    print(kwota)
#    for key in liczba:
#        print(x=key)
    x=x.replace("$cena",str(kwota))
    print(x)
    return x



formatuj("koszt $cena PLN", "kwota $cena brutto", stala=10)


def test_formatuj():
    assert formatuj("koszt $cena PLN", "kwota $cena brutto", cena=10) == "koszt 10 PLN\nkwota 10 brutto"

