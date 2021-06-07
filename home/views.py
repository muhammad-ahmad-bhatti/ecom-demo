from django.shortcuts import render
from .models import Destination
# Create your views here.


def home(request):
    products = Destination.objects.all()
    return render(request, 'home.html', {'products': products})

