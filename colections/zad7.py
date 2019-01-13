print('podaj napis')
napis=input()
count=0
litery=['a','e', 'i', 'o', 'u', 'y']
SAMOGLOSKI="aeiouy"
#litery="aeiouy"

for a in range(len(napis)):
    print(a)
    if SAMOGLOSKI.__contains__(napis(a)):
        count+=1
        print(count)
#assert warunek koniec