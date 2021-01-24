from travel.models import Destination
from MyFirstDJangoProject.settings import BASE_DIR
from django.shortcuts import render
import os

# Create your views here.

def getDestinations():
    return Destination.objects.all()


def home(request):
    return render(request, os.path.join(BASE_DIR, 'travel/templates/index.html'), {'dests': getDestinations()})


def tours(request):
    return render(request, os.path.join(BASE_DIR, 'travel/templates/tours.html'), {'dests':getDestinations()})


def blog(request):
    return render(request, os.path.join(BASE_DIR, 'travel/templates/blog.html'), {'dests':getDestinations()})


def contacts(request):
    return render(request, os.path.join(BASE_DIR, 'travel/templates/contacts.html'), {'dests':getDestinations()})


def offers(request):
    return render(request, os.path.join(BASE_DIR, 'travel/templates/offers.html'), {'dests':getDestinations()})