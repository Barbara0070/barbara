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
if x > 100:
    miss = True
if x <= 90 and x>=10:
    srodekx=True
if y < 10:
    gora = True
if y > 90:
    dol = True
if y > 100:
    miss = True
if y>=10 and y<=90:
    srodeky=True
if miss == True:
    prinf("pudlo")
if lewa == True and gora == True:
    print("lewy gorny")
if gora==True and lewa==False and prawa==False
    print