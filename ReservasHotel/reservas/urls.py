from django.urls import path
from reservas import views

urlpatterns = [
    path(
        route='',
        view=views.Reservas_View.as_view(),
        name='init'
    )

]

