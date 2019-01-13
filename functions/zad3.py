def test_policz(napis, otwarcie="<", zamkniecie=">"):
    i=0
    sum=0
    for a in napis:
        if a!=otwarcie and a!=zamkniecie:
            sum=sum+(1*i)
        if a==otwarcie:
            i+=1
        if a==zamkniecie and i>0:
            i-=1
    return sum
def test_policz_znaki_w_pustym():
    assert policz_znaki("") == 0
def test_policz2():
    assert policz_znaki("ala ma kota")==0
def test_policz_koniec():
    assert test_policz("<a><<a>a>")==4
print(test_policz("a<a<a>a>>"))