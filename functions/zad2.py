def test_wiecej(napis, liczba):
    zbior=[]
    slownik={}
    for a in napis:
        slownik[a]=slownik.get(a, 0)+1
    for litera in slownik:
        if slownik[litera]>2:
            zbior.append(litera)
    return zbior
print(test_wiecej("aaaaaawdwdwdwdwrewqymmmmmm",4))
#for a in napis slownik[a]=slownik.get(a,0)+1