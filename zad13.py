x=0
y=0
c=0
while x<7:
    x=x+1
    print('podaj temperature w', x,"dzien tygodnia")
    c=float(input())
    y+=c
print('srednia temperatura to:', y/7)