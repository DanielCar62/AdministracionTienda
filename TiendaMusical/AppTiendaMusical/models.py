from django.db import models

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