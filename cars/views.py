from django.shortcuts import render
from django.views.generic import DetailView

from . import models

# Create your views here.

class CarsDetails(DetailView):
    model = models.Cars
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'c'
