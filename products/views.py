from django.shortcuts import render, redirect
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

    if 'subtotal_' not in request.session:
        request.session['subtotal_'] = context['product'].price
    else:
        request.session['subtotal_'] += context['product'].price

    return render(request, 'products/add.html', context)

def remove(request, ide):
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
                if request.session['cart'] == 1:
                    del request.session['cart'] 
                else:
                    request.session['cart'] -= 1

                if request.session['*!'+str(context['product'].ide)] == 1:
                    del request.session['*!'+str(context['product'].ide)]
                else:
                    request.session['*!'+str(context['product'].ide)] -= 1
                if request.session['subtotal_']  == 1:
                    del request.session['subtotal_']
                else:
                    request.session['subtotal_'] -= context['product'].price
    return redirect('cart')