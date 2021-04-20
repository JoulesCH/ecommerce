from django.db import models
from django.contrib.auth.models import User
from shoppingcarts.models import Cart
# Create your models here.
class Product(models.Model):
    ide = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, null = False )
    descripcion = models.TextField(null = False )
    price = models.FloatField(null = False)
    stock = models.IntegerField(null = False)

    categories = models.CharField(max_length = 300, null = False, default = "temporada,")

    discount = models.FloatField(null = False)
    image1 = models.ImageField(upload_to = 'static/images/')
    image2 = models.ImageField(upload_to = 'static/images/', null = True)
    image3 = models.ImageField(upload_to = 'static/images/', null = True)
    image4 = models.ImageField(upload_to = 'static/images/', null = True)
    
    def get_categories(self):
        if ',' in self.categories:
            return self.categories.split(',')
        else:
            return self.categories

    def get_cart_path(self):
        return '/add/' + str(self.ide)
    def get_remove_path(self):
        return '/remove/' + str(self.ide)

    def get_specs(self):
        return self.productspec_set.all()

    def __str__(self):
        return self.name

class CartProduct(models.Model):
    ide = models.AutoField(primary_key = True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    talla = models.CharField(max_length= 5, default = "Unico")
    color = models.CharField(max_length = 20, default = "Unico") 
    
    def get_remove_path(self):
        return '/remove/' + str(self.ide) 

    def get_stock(self):
        if self.talla == 'Unico' or self.color == 'Unico':
            return 0
        else:
            talla = Size.objects.filter(valor = self.talla)[0]
            color = Color.objects.filter(nombre = self.color)[0]
            return ProductSpec.objects.get(product = self.product, size = talla, color = color).stock

class Size(models.Model):
    ide = models.AutoField(primary_key = True)
    #product = models.ManyToManyField(Product)
    valor = models.CharField(max_length = 5)

    def __str__(self):
        return str(self.valor)

class Color(models.Model):
    ide = models.AutoField(primary_key = True)
    #product = models.ManyToManyField(Product)
    nombre = models.CharField(max_length = 30)
    codigo = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.nombre) + '-' + str(self.codigo)

class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ide = models.AutoField(primary_key = True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    stock = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.product) + ' ' + str(self.color) + ' ' + str(self.size)



