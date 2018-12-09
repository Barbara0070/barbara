#print(dir(random))
#print(help(random))
#lista=[1,10]
#from radom import choice
#choice(lista)
from random import randint
skarbx = randint(1,10)
skarby = randint(1,10)
x = randint(1,10)
y = randint(1,10)
skarbx=1
skarby=1
x=2
y=2
xblisko = abs(skarbx - x)
yblisko = abs(skarby - y)
krok = 0
krok_all = 0
odlegloscx = abs(skarbx - x)
odlegloscy = abs(skarby - y)
if odlegloscx > odlegloscy:
    odleglosc = odlegloscx
else:
    odleglosc = odlegloscy
minkrok = odleglosc
odlegloscxy=odlegloscx+odlegloscy
while True:
    blizej = False
    if x == skarbx and y == skarby:
        print(f"wygrales po {krok_all} krokach")
        break
    if x < 1 or x>10 or y<1 or y>10:
        print('przegrales')
        break
    if krok > minkrok * 2:
        skarbx = 5
        skarby = 5
        print('skarb sie przniosl')
        if x==skarbx and y==skarbx:
            print('i wygrales')
            break
        krok = 0
        odlegloscx = abs(skarbx - x)
        odlegloscy = abs(skarby - y)
        if odlegloscx > odlegloscy:
            odleglosc = odlegloscx
        else:
            odleglosc = odlegloscy
        minkrok = odleglosc
        print(odleglosc)
        odlegloscxy=odlegloscx+odlegloscy
        continue
    print(f"Twoja pozycja to x:{x} y:{y} Podaj kierunek ruchu(gora/dol/prawo/lewo/prawogora/prawodol itp)")
    komenda = input()
    if komenda == 'gora':
        y -= 1
    if komenda == 'dol':
        y += 1
    if komenda == 'prawo':
        x += 1
    if komenda == 'lewo':
        x -= 1
    if komenda == 'prawogora':
        x += 1
        y -= 1
    if komenda == 'prawodol':
        x += 1
        y += 1
    if komenda == 'lewogora':
        x -= 1
        y -= 1
    if komenda == 'lewodol':
        x -= 1
        y += 1
    krok_all += 1
    krok = krok + 1
    if x==skarbx and y==skarby:
        continue
    nowaodlegloscx = abs(skarbx - x)
    nowaodlegloscy = abs(skarby - y)
    if nowaodlegloscx > nowaodlegloscy:
       nowaodleglosc = nowaodlegloscx
    else:
       nowaodleglosc = nowaodlegloscy
#   if nowaodleglosc==1 and (x==1 or x==10 or y==1 or y==10):
#       if ((x==1 or x==10) and (y!=1 or y!=10)) or ((y==1 or y==10) and (x!=1 or x!=10)):
#           print("specjalne miejsce")
#           odlegloscx = nowaodlegloscx
#           odlegloscy = nowaodlegloscy
#           odleglosc = nowaodleglosc
#           continue
#   if nowaodleglosc < odleglosc:
#       print('jestes blizej jeden')
#   if nowaodleglosc == odleglosc:
#       print('bez zmian jeden')
#   if nowaodleglosc > odleglosc:
#       print('jestes dalej jeden')
    odlegloscx = nowaodlegloscx
    odlegloscy = nowaodlegloscy
    odleglosc = nowaodleglosc
    nowaodlegloscxy = odlegloscx+odlegloscy
    print(nowaodlegloscxy)
    if nowaodlegloscxy>odlegloscxy:
        print("dalej")
    if nowaodlegloscxy<odlegloscxy:
        print("blizej")
    odlegloscxy=nowaodlegloscxy

