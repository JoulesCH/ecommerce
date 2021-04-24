from django.shortcuts import render, redirect
from products.models import Product,CartProduct, ProductSpec
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from shoppingcarts.models import Cart
# Create your views here.
def cart(request):
    try:
        #Si el usuario está loggeado
        user = request.session['username']
    except:
        #Sino está loggeado leer los productos cacheados
        if 'cart' in request.session:
            cart = []
            for k in request.session.keys():
                if '*!' in k:
                    cart+= [Product.objects.get(ide = int(k.replace('*!','')))]*request.session[k]
            
            return render(request, 'carts/cart.html', {'cart':cart})
        else:
            return render (request, 'carts/cart.html',{'error': 'Carrito vacío'})
    else:
        #Si está loggeado 
        #Ver si  hay productos cacheados para agregarlos a la base de datos
        if 'cart' in request.session:
            del request.session['cart']
            return redirect('cart')
        #Se leen los datos de la base 
        products = CartProduct.objects.filter(cart = request.user.cart.ide )
        subtotal = 0

        for product in products:
            subtotal+= product.get_total()

        user = User.objects.get(pk = request.user.pk)
        Cart_ = Cart.objects.get(user = user)
        Cart_.subtotal = subtotal
        Cart_.save()
        #options = ProductSpec.objects.filter(product = product)
        if 'error' in request.session:
            error = request.session['error']
            del request.session['error']
        else:
            error= None
        if products:
            return render(request, 'carts/cart.html', {'productscart':products, 'subtotal':subtotal,'error_':error})
        else:
            return render (request, 'carts/cart.html',{'error': 'Carrito vacío'})

@login_required
def payment(request):
    #print()
    if request.method == 'POST':
        for product in CartProduct.objects.filter(cart = request.user.cart):
            if product.talla == 'Unico' or product.color == 'Unico':
                request.session['error'] = {'id':product.ide, 'texto': 'Escoge talla y color'}
                return redirect('cart')


        return render(request, 'users/address.html')
    else:
        
        return redirect('cart')
        #return render(request, 'carts/payment.html', {'error': 'Debes acceder a tu carrito primero para escoger detalles'})
