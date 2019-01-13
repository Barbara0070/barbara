lista1=list(x * 0.1 for x in range(0, 10))
print(lista1)

lista2=list((x,x*x,x*x*x)for x in range(-10,11))
print(lista2)

zbior=["adwdawd", "egwegewgwegfw", "wdwdw", "w"]

slownik=dict((a,len(a)) for a in zbior)
print(slownik)