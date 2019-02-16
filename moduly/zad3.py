import sys
try:
    f_name=sys.argv[1]
    f_name2=sys.argv[2]
except IndexError:
    print("nie podalkes pliku")
    exit()

with open(f_name, encoding="utf-8") as f:
    with open(f_name2, "w", encoding="utf-8") as nowy:
        zbior = set()
        for line in f:
                ile_malp=0
                for x in line:
                    if x=='@':
                        ile_malp+=1
                if not ile_malp==1:
                    continue
                line=line.lower()
                line=line.replace(" ", "")
                zbior.add(line)
        for x in sorted(zbior):
            nowy.write(x)
print(zbior)




