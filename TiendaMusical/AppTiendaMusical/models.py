from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proveedor(models.Model):

    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    email = models.EmailField()
    empresa = models.CharField(max_length=50)
    telefono = models.IntegerField()

class Instrumento(models.Model):

    nombre = models.CharField(max_length=50)
    modelo = models.IntegerField()
    marca = models.CharField(max_length=50)

class Amplificador(models.Model):

    modelo = models.IntegerField()
    marca = models.CharField(max_length=50)

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)