def napisy(*args):
    """
    napisz funkcje ktora przyjmie dowolna liczbe napisow i zwroci je polaczone znakiem nowej linii

    >>> napisy("a","b")
    a
    b

    """
def wypisz(*args, **kwargs):
    for i in args:

    print(f"argumenty niekluczowe: {args[i]}")
    print(f"argumenty kluczowe: {kwargs}")