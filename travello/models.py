from django.db import models

# Create your models here.
class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=32)
    descripcionCiudad = models.TextField(max_length=128)
    imagenCiudad = models.ImageField()
    precioTour = models.IntegerField()
    ofertaTour = models.BooleanField(default=False)
    