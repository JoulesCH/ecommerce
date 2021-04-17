from django.shortcuts import render
from products.models import Product
# Create your views here.

def add(request, ide):
    context = {}
    try:
        context['product'] =  Product.objects.get(ide = ide)
    except:
        context['error'] =  'No fue posible encontrar el producto especificado'
    else:
        if context['product'].stock == 0:
            context['error'] =  'No hay más productos disponibles'
        else:
            if 'cart' in request.session:
                request.session['cart'] += 1
            else:
                request.session['cart'] = 1
            if '*!'+str(context['product'].ide) in request.session:
                request.session['*!'+str(context['product'].ide)] += 1
            else:
                request.session['*!'+str(context['product'].ide)] = 1
 

    print('*'*10,request.session['cart'],  request.session.keys())

    return render(request, 'products/add.html', context)