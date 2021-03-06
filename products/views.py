from django.shortcuts import render, redirect
from products.models import Product,CartProduct, ProductSpec, Size, Color
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

                if request.method == "POST": #Anclado al if de abajo
                    try:
                        cantidad = request.POST['quantity']
                        color = request.POST['color']
                        size = request.POST['size']
                    except:
                        request.session['error'] = 'Selecciona todas las opciones'
                        return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        size = Size.objects.filter(valor = size)[0]
                        color = Color.objects.filter(nombre = color)[0]
                        product = ProductSpec.objects.get(product = context['product'], size = size, color = color)
                        if product.stock == 0:
                            request.session['error'] = f'No hay más stock de {size}-{color.nombre}'
                            return redirect(request.META.get('HTTP_REFERER'))

                user = User.objects.get(pk = request.user.pk)
                cart = Cart.objects.get(user = user)
                #Sumamos uno a la cuenta de productso
                cart.no_productos +=1
                #Modificamos el subtotal
                cart.subtotal+= context['product'].price
                
                cart.save()
                #Agregamos el producto
                cart_product = CartProduct(cart = user.cart, product = context['product'])

                if request.method == "POST":
                    cart_product.quantity = cantidad
                    cart_product.talla = size
                    cart_product.color = color
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
        user = User.objects.get(pk = request.user.pk)
        
        #Aquitamos el producto
        try:
            cartproduct = CartProduct.objects.get(ide = ide)
        except:
            return redirect('cart')
        else:
            product  = Product.objects.get(ide = cartproduct.product.ide)

            cart = Cart.objects.get(user = user)
            #Sumamos uno a la cuenta de productso
            cart.no_productos -=1
            #Modificamos el subtotal
            cart.subtotal-= product.price
                    
            cart.save()
            cartproduct.delete()

            return redirect('cart')

def select_option(request,ide):
    if request.method == 'POST':
        try:
            cartproduct = CartProduct.objects.get(ide = ide)
        except:
            return redirect('cart')
        else:
            if 'size' in request.POST.keys():
                cartproduct.quantity = 1
                cartproduct.talla = request.POST['size']
            elif 'color' in request.POST.keys():
                cartproduct.quantity = 1
                cartproduct.color = request.POST['color']
            elif 'quantity' in request.POST.keys():
                try:
                    size = Size.objects.filter(valor =cartproduct.talla)[0]
                    color = Color.objects.filter(nombre =cartproduct.color)[0]
                except:
                    request.session['error'] = {'id':cartproduct.ide, 'texto': 'Escoge talla y color'}
                else:
                    product_spec = ProductSpec.objects.get(product = cartproduct.product, size = size, color = color)
                    if product_spec.stock >= int(request.POST['quantity']):
                        cartproduct.quantity = int(request.POST['quantity'])
                    else:
                        request.session['error'] = {'id':cartproduct.ide, 'Cantidad':request.POST['quantity']}
            cartproduct.save()
        return redirect('cart')
    else:
        return redirect('cart')

def product(request,ide):
    try:
        product = Product.objects.get(ide = ide)
    except:
        return render(request, 'products/product.html',{'error':'Artículo no encontrado'})
    else:
        if 'error' in request.session:
            error = request.session['error']
            del request.session['error']
            return render(request, 'products/product.html', {'product':product, 'error_':error})
        return render(request, 'products/product.html', {'product':product})