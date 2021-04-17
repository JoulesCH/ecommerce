from django.db import models
from users import models

# Create your models here.
class Carrito(models.Model):
    ide = models.AutoField(primary_key = True)
