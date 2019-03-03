from django.db import models

# Create your models here.
BODY_TYPE_CHOICES= (
    ("sedan", "sedan"),
    ("combi", "combi"),
    ("hatchback", "hatchback"),
)
Engine_types=(
    ("electric", "electric"),
    ("steam", "steam"),
    ("jet", "jet"),
)
class Engine(models.Model):
    type =models.CharField(max_length=50, choices=Engine_types)
    power = models.IntegerField()
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.type} and {self.power}"
class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES, null=True, blank=True)
    engine=models.ForeignKey(Engine, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    is_ready= models.BooleanField(default=False)





def __str__(self):
    return f"{self.brand} and {self.model}"

#manage.py migrate, showmigrations makemigrations, shell createsuperuser


#from cars.models import Car

#django suit
#mercedesy = [("w211",1999),
#for m in mercedesy:
#    Car.objects.create(brand="mercedes", model=m[0], year=m[1])

#images pip install pillow


#bootstrap

# django admin coocbook
#two scpoes of django
#pactpub