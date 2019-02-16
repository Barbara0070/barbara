import sys
try:
    f_name=sys.argv[1]
except IndexError:
    print("nie podalkes pliku")
    exit()

with open(f_name, encoding="utf-8") as f:
    slownik={}
    for line in f:
        login, opcja, czas=line.split(";")
        czas = int(czas.replace("\n", ""))
        if login in slownik.keys():
            if opcja=="LOGIN":
                slownik[login]=slownik[login]-czas
            else:
                slownik[login]=slownik[login]+czas
        else:
            slownik[login]= czas*(-1)
        for login,time in sorted(slownik.items(), key=login):
            print(f" - {login}: {time} s")


