from django.contrib.auth.models import User
from django.db import models

class Customer(User):
    id_carrito = models.CharField(max_length = 200, default ='8788776')