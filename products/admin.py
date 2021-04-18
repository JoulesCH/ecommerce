from django.contrib import admin
from products.models import Product, CartProduct
# Register your models here.
@admin.register(Product)
class FlatPageAdmin(admin.ModelAdmin):
    #fields = (('ide', 'name'), 'price')
    pass

@admin.register(CartProduct)
class FlatPageAdmin(admin.ModelAdmin):
    #fields = (('ide', 'name'), 'price')
    pass