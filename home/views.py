from django.shortcuts import render
from .models import Destination
from django.views.generic import ListView, DetailView


# Create your views here.


# def home(request):
#     products = Destination.objects.all()
#     return render(request, 'home.html', {'products': products})
#
#
# def details(request, num=0):
#     pro = Destination.objects.get(pk=num)
#     return render(request, 'details.html', {'pro': pro})


class Home(ListView):
    template_name = 'home.html'
    model = Destination
    context_object_name = 'products'


class Details(DetailView):
    template_name = 'details.html'
    model = Destination
    context_object_name = 'pro'
