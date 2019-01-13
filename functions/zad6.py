x = [1, 2, 2, [3, 4, 5, [2]], 3, 3]
tymczasowa=[]
def splaszcz(lista):
    tymczasowa=[]
    for i in splaszcz(lista):
        if type(i)==list:
            splaszcz(i)
        else:
            tymczasowa.append(i)
    return tymczasowa



print(splaszcz(x))



splaszcz(x)
