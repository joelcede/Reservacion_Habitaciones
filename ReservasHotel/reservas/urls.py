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

]

