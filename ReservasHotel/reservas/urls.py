from django.urls import path
from reservas import views

urlpatterns = [
    path(
        route='',
        view=views.Reservas_View.as_view(),
        name='init'
    ),
    path(
        route='informacion/',
        view=views.Informacion_View.as_view(),
        name='informacion'
    ),
    path(
        route='portafolio/',
        view=views.Portafolio_View.as_view(),
        name='portafolio'
    ),
    path(
        route='contacto/',
        view=views.Contacto_View.as_view(),
        name='contacto'
    ),
    path(
        route='personal/',
        view=views.Personal_View.as_view(),
        name='personal'
    )
]

