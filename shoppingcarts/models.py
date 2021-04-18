from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    ide = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    promo = models.IntegerField( default = 0)
    subtotal = models.FloatField(default = 0)
    estado = models.CharField(max_length = 20, default = 'waiting' )
    no_productos = models.IntegerField( default = 0)