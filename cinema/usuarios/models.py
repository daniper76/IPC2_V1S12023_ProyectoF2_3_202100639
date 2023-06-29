from django.db import models

# Create your models here.

class Usuario(models.Model):

    codigo=models.IntegerField()
    nombre=models.TextField(max_length=100)
    apellido=models.TextField(max_length=100)
    telefono=models.TextField(max_length=100)
    correo=models.TextField(max_length=100)
    contrasenia=models.TextField(max_length=100)
    
