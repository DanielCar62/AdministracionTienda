from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    email = models.EmailField()

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