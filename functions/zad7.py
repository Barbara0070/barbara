
def przytnij(data, start, stop):
    """

    :param data:
    :param start:
    :param stop:
    :return:
    """

    out=[]
    for i in data:
        if start(i):
            out.append(i)
        if stop(i):
            break
    return out
print(przytnij(data=[1,2,3,4,5,6,7], start=lambda x: x>3, stop=lambda x: x==6))

def test_przytnij():
    assert przytnij(data=[1,2,3,4,5,6,7], start=lambda x: x>3, stop=lambda x: x==6)==[4,5,6]


def hi():
    return "hello"
def przywitaj_sie(greeting_function):
    print(greeting_function())


def sprawdz_czy(x, funkcja1, funkcja2):
    return funkcja1(x) and funkcja2(x)
def sprawdz_czy_podzielna(x):
    return x%2 ==0 and x%3 ==0
print(sprawdz_czy(12, sprawdz_czy_podzielna,lambda x: x>5))