import os

path = 'c:\\Users\\kurs\\workspace'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.py' in file and not "policz.py" in file:
            files.append(os.path.join(r, file))
suma=0
for f in files:
    linijki=0
    print(f)
    with open(f) as plik:
        for line in plik:
            linijki+=1
    print(f"{f}\t :{linijki}")
    suma+=linijki
print(suma)
