from django.contrib import admin
from products.models import Product, CartProduct, ProductSpec, Size, Color
# Register your models here.
@admin.register(Product)
class FlatPageAdmin(admin.ModelAdmin):
    #fields = (('ide', 'name'), 'price')
    pass

@admin.register(CartProduct)
class FlatPageAdmin(admin.ModelAdmin):
    #fields = (('ide', 'name'), 'price')
    pass
@admin.register(ProductSpec)
class FlatPageAdmin(admin.ModelAdmin):
    #fields = (('ide', 'name'), 'price')
    pass
@admin.register(Size)
class FlatPageAdmin(admin.ModelAdmin):
    #fields = (('ide', 'name'), 'price')
    pass
@admin.register(Color)
class FlatPageAdmin(admin.ModelAdmin):
    #fields = (('ide', 'name'), 'price')
    pass