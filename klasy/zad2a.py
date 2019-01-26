class Dog:
    species='Canis Familar'
    def __init__(self,name, age):
        self.name=name
        self.age=age
        self.spec=Dog.species
rex=Dog("Rex", 10)
azor=Dog("axor", 115)
puszek=Dog("puszek",101)
def najstarszy(*args):
    winner=args[0]
    for a in args:
        if a.age>winner.age:
            winner=a
    return winner
print(najstarszy(rex, azor,puszek).age)
