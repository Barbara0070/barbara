print("podaj pozycje gracza x")
x = int(input())
print("podaj pozycje y")
y = int(input())
miss=False
lewa=False
prawa=False
gora=False
dol=False
if x < 10:
    lewa = True
if x > 90:
    prawa = True
if x > 100 or x<1:
    miss = True
if y < 10:
    gora = True
if y > 90:
    dol = True
if y > 100:
    miss = True
if miss == True:
    print("pudlo")
if lewa == True and gora == True:
    print("lewy gorny")
if gora==True and lewa==False and prawa==False:
    print("gorna krawedz")
if gora==True and prawa==True:
    print("prawy gorny rog")
if lewa==True and gora==False and dol==False:
    print('lewa krawedz')
if lewa==True and dol==True:
    print('lewy dolny rog')
if dol==True and lewa==False and prawa==False:
    print('dolna krawedz')
if prawa==True and dol==True:
    print('prawy dolny')
if prawa==True and gora==False and dol==False:
    print('prawa krawedz')