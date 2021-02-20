from django.shortcuts import render
from django.http import HttpResponse
from templates import users
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views
from reservas.models import Habitaciones

# Create your views here.

class Reservas_View(auth_views.LoginView):
    template_name = 'init.html'

def informacion(request):
    projects = Habitaciones.objects.all()
    return render(request,'informacion.html', {'projects':projects})

class Portafolio_View(auth_views.LoginView):
    template_name = 'portafolio.html'

class Contacto_View(auth_views.LoginView):
    template_name = 'contacto.html'

class Personal_View(auth_views.LoginView):
    template_name = 'personal.html'