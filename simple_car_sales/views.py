from django.shortcuts import render

from bands.models import Bands
from cars.models import Cars

def home(request,band_slug =None):
    
    cars = Cars.objects.all()
    if band_slug is not None:
        band = Bands.objects.get(slug = band_slug)
        cars = Cars.objects.filter(band=band)
    bands = Bands.objects.all()
    return render(request,'index.html',{'bands':bands,"cars":cars})