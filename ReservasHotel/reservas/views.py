from django.shortcuts import render
from django.http import HttpResponse
from templates import users
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views

# Create your views here.

class Reservas_View(auth_views.LoginView):
    template_name = 'init.html'