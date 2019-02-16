Import math
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y)
        return NotImplemented

    def __sub__(self,other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x, self.y-other.y)
        return NotImplemented
    def __mul__(self,other):
        if isinstance(other, int):
            return Vector(self.x*other, self.y*other)
        if isinstance(other, Vector):
            return Vector(self.x*other.x, self.y*other.y)
        return NotImplemented
    def __sub__(self,other):
        if isinstance(other, Vector):
            return Vector(self.x-other.x, self.y-other.y)
        return NotImplemented

    def __lt__(self,other):
        if isinstance(other, Vector):
            if self.x*self.y<other.x*other.y:
                return True
            return False
        return NotImplemented
    def length(self):
        return ((self.x)**2)+(self.y)**2)**(1/2)
    def __gt__(self,other):
        if isinstance(other, Vector):
            if (self.x)**2)+(self.y)**2):
                return True
            return False
        return NotImplemented







vector_1=Vector(1,1)
vector_2=Vector(2,5)
print(f"{vector_1.x} {vector_1.x} \n{vector_2.x} {vector_2.y}")
print((vector_1+vector_2).y)
print((vector_1*3).y)
print((vector_1>vector_2))
print((vector_1<vector_2))
