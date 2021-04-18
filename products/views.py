from django.shortcuts import render, redirect
from products.models import Product,CartProduct
from django.contrib.auth.models import User
from shoppingcarts.models import Cart
# Create your views here.

def add(request, ide):
    context = {}
    try:
        #Si el usuario está loggeado
        user = request.session['username']
    except:
        #Sino está loggead cachea el carrito
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
    else:
        #Si el usuario está loggeado guarda en la base de datos
        try:
            context['product'] =  Product.objects.get(ide = ide)
        except:
            context['error'] =  'No fue posible encontrar el producto especificado'
        else:
            if context['product'].stock == 0:
                context['error'] =  'No hay más productos disponibles'
            else:
                user = User.objects.get(pk = request.user.pk)
                cart = Cart.objects.get(user = user)
                #Sumamos uno a la cuenta de productso
                cart.no_productos +=1
                #Modificamos el subtotal
                cart.subtotal+= context['product'].price
                
                cart.save()
                #Agregamos el producto
                cart_product = CartProduct(cart = user.cart, product = context['product'])
                cart_product.save()

        return render(request, 'products/add.html', context)
    
def remove(request, ide):
    context = {}
    try:
        #Si el usuario está loggeado
        user = request.session['username']
    except:
        #Sino está loggead cachea el carrito
        try:
            context['product'] =  Product.objects.get(ide = ide)
        except:
            context['error'] =  'No fue posible encontrar el producto especificado'
        else:
            if True:
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
    else:
        #Si el usuario está loggeado guarda en la base de datos
        try:
            context['product'] =  Product.objects.get(ide = ide)
        except:
            context['error'] =  'No fue posible encontrar el producto especificado'
        else:
            if True:
                user = User.objects.get(pk = request.user.pk)
                cart = Cart.objects.get(user = user)
                #Sumamos uno a la cuenta de productso
                cart.no_productos -=1
                #Modificamos el subtotal
                cart.subtotal-= context['product'].price
                
                cart.save()
                #Agregamos el producto
                cartproducts = CartProduct.objects.filter(cart = user.cart, product = context['product'])
                cartproducts[0].delete()

        return redirect('cart')