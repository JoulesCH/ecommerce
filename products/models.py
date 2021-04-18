from django.db import models

# Create your models here.
class Product(models.Model):
    ide = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, null = False )
    descripcion = models.TextField(null = False )
    price = models.FloatField(null = False)
    stock = models.IntegerField(null = False)

    sizes = models.CharField(max_length = 50)
    colors = models.CharField(max_length = 50)
    categories = models.CharField(max_length = 300, null = False, default = "Moda,")

    discount = models.FloatField(null = False)
    image1 = models.ImageField(upload_to = 'static/images/')
    image2 = models.ImageField(upload_to = 'static/images/', null = True)
    image3 = models.ImageField(upload_to = 'static/images/', null = True)
    image4 = models.ImageField(upload_to = 'static/images/', null = True)
    
    
    def get_sizes(self):
        return self.sizes.split(',')
    def get_colors(self):
        return self.colors.split(',')
    def get_categories(self):
        return self.categories.split(',')
    def get_cart_path(self):
        return '/add/' + str(self.ide)
    def get_remove_path(self):
        return '/remove/' + str(self.ide)
    def __str__(self):
        return self.name

