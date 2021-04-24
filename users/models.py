from django.contrib.auth.models import User
from django.db import models

class Customer(User):
    pass


class Address(models.Model):
    ide = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 70)
    apellido = models.CharField(max_length = 70)
    direccion = models.CharField(max_length = 70)
    cp = models.CharField(max_length = 20)
    ciudad = models.CharField(max_length = 70)
    numero  = models.CharField(max_length = 4)
    correo = models.CharField(max_length = 20, default = "Ninguno")
    adicional = models.TextField()
    recordar = models.BooleanField(default=False)
