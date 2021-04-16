from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
def home(request):
    principal_categories = ["temporada", "hombre", "mujer"]
    products =  Product.objects.all()
    context = {
        'products': products,
        'p_categories': principal_categories,
    }
    return render(request, 'home/home.html', context)