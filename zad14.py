min = None
max = None
while True:
    print('podaj liczbe, koniec aby zakonczyc')
    komenda = input()
    if komenda == 'koniec':
        break
    if komenda == '':
        print('nie podales komendy')
        continue
    komenda = int(komenda)
    if min==None or min > komenda:
        min = komenda
    if max==None or max < komenda:
        max = komenda
print('maksymalna to ', max, "\nminimalna to ", min)
