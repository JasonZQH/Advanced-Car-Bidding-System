# Create your views here.
from django.shortcuts import render
from .models import Users, Car



def car_info(request):
    cars = Car.objects.all()
    print(cars) 
    return render(request, 'home.html', {'cars': cars})



