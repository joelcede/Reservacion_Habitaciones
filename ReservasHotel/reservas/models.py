from django.db import models

# Create your models here.
class Habitaciones(models.Model):
    imagen = models.ImageField(upload_to='ImagenHabitaciones', default='reservas/photos/h4.jpg')
    titulo = models.CharField(max_length=25)
    despr1 = models.CharField(max_length=25)
    despr2 = models.CharField(max_length=25)
    despr3 = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Habitacio"
        verbose_name_plural = "Habitaciones"
    
    def __str__(self):
        return self.titulo