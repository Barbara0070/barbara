print("podaj napis")
napis=input()
count=0
wnawiasie=False
for a in range(len(napis)):
    if wnawiasie==True and napis[a]!=">":
        count+=1
    if napis[a]=="<":
        wnawiasie=True
    if napis[a]==">":
        wnawiasie=False

#elif continue break
print(count)
