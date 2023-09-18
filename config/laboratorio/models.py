from django.db import models
import datetime


# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    ciudad = models.CharField(max_length=50,default='Santiago', blank=False, null=False)
    pais = models.CharField(max_length=50, default='Chile', blank=False, null=False)

    def __str__(self) -> str:
        return self.nombre
    

class DirectorGeneral(models.Model):
    laboratorio = models.OneToOneField(Laboratorio,blank=False, null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    especialidad = models.CharField(max_length=50,default='Sin especialidad', blank=False, null=False)

    def __str__(self) -> str:
        return self.nombre
    

YEAR_CHOICES = [(year, year) for year in range(2015, datetime.datetime.now().year + 1)]

class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    laboratorio = models.ForeignKey(Laboratorio, blank=False, null=False, on_delete=models.CASCADE)
    f_fabricacion = models.PositiveIntegerField(choices=YEAR_CHOICES)
    p_costo = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.nombre} {self.laboratorio} {self.f_fabricacion}'
    
    

