import sys
try:
    f_name=sys.argv[1]
except IndexError:
    prunt("nie podalkes pliku")
    exit()
try:
    with open(f_name, encoding="utf-8") as f:
        for i, line in enumerate(f,start=1):
            print(f"{i}: {line}", end="")