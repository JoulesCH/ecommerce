from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
def home(request):
    principal_categories = ["temporada", "hombre", "mujer"]
    products =  Product.objects.all()
    context = {
        'products': products,
        'p_categories': principal_categories,
        'inicio':'active'
    }
    try: 
        user = request.session['username']
    except:
        pass
    else:
        context['username'] = user
        
    return render(request, 'home/home.html', context)

def prueba(request):
    print(request.user.cart.ide)
    return render(request, 'pruebas.html')
