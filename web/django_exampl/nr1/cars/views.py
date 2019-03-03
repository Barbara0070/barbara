from django.shortcuts import render
from cars.models import Car
cars = Car.objects.all()
# Create your views here.

def car_list(request):
    cars=Car.objects.all()
    return render(
        request=request,
        template_name="cars_list.html",
        context={'cars':cars},

    )


def car_single(request, id):
        return render(
        request=request,
        template_name="aaa.html",
        context={'id': cars},

    )
