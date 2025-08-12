from django.shortcuts import render

from bands.models import Bands
from cars.models import Cars

def home(request):
    bands = Bands.objects.all()
    cars = Cars.objects.all()
    return render(request,'index.html',{'bands':bands,"cars":cars})