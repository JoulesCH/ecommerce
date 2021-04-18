from django.shortcuts import render, redirect
from products.models import Product
# Create your views here.
def cart(request):
    if 'cart' in request.session:
        cart = []
        for k in request.session.keys():
            if '*!' in k:
                cart+= [Product.objects.get(ide = int(k.replace('*!','')))]*request.session[k]
        total = 0
        for product in cart:
            total += product.price
        return render(request, 'carts/cart.html', {'cart':cart, 'total':total})

    return render(request, 'carts/cart.html', {'error': 'Carrito vacío'})
def payment(request):
    print(request.POST.keys())
    if request.method == 'POST':
        for key in request.POST.keys()
        return render(request, 'carts/payment.html')
    else:
        return redirect('cart')
        #return render(request, 'carts/payment.html', {'error': 'Debes acceder a tu carrito primero para escoger detalles'})