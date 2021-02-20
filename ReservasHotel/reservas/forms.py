from django import forms
from reservas.models import Habitaciones

class HabitacionesForms(forms.ModelForm):

    class Meta:
        model = Habitaciones
        fields = ('descripcion','photo','lug1','lug2','lug3')