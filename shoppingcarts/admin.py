from django.contrib import admin
from shoppingcarts.models import Cart

@admin.register(Cart)
class FlatPageAdmin(admin.ModelAdmin):
    #fields = (('ide', 'name'), 'price')
    pass
# Register your models here.
