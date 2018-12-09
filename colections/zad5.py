#dane=[int(d) for d in dane]
#print("imie:",imie, sep="", end="")
print('    ', end='')
for i in range(10):
    print(i,'  ', end='')
print()
j=0
for i in range(10):
    j=i
    print(j,"  ", end='')
    for j in range(10):
        print(j*i, " ", end='')
        if j*i<10:
            print(" ", end='')
    print('')
#dlugosc print(x:5)