from django.db import models #importar libreria models

import datetime
import os


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/uploads/', filename)
# Create your models here.

class Sebe(models.Model): #crear clase   fields = ['tipo', 'nombre', 'Descripcion', 'precio'] #crear campos
    tipo = models.AutoField(primary_key=True) #crear campo precio
    nombre = models.CharField(max_length=50, verbose_name='nombre') #crear campo nombre
    descripcion = models.CharField(max_length=200 , verbose_name='descripcion') #crear campo DAESCRIPCION
    precio = models.IntegerField(verbose_name='precio') #crear campo PRECIO
    # imga = models.ImageField((""), upload_to="media", height_field=None, width_field=None, max_length=None)
    imga = models.ImageField(upload_to=filepath, null=True, blank=True)
    imgb = models.ImageField(upload_to=filepath, null=True, blank=True)
    # imgb = models.ImageField((""), upload_to="media", height_field=None, width_field=None, max_length=None)
    descuento = models.IntegerField() #crear campo edad
    # edad = models.IntegerField() #crear campo edad
    # vacuna = models.CharField(max_length=200 , verbose_name='Nombre de Vacuna') #crear campo vacuna
    # fecha = models.DateField() #crear campo fecha


