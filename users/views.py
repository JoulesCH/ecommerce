from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from shoppingcarts.models import Cart
from users.models import Address
# Create your views here.
def login_view(request):
    next_url = request.GET.get('next')
    if next_url:
        request.session['next'] = next_url

    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                request.session['username'] = username
                try: 
                    next_url = request.session['next']
                except:
                    return redirect('home')
                else:
                    del request.session['next']
                    return redirect(next_url)
            else:
                return render(request, 'users/login.html', {'error': 'Datos inválidos'})
                    
    try:
        user = request.session['username']
    except:
        return render(request, 'users/login.html',{'next':request.GET.get('next')})
    else:
        return redirect('home')
 
@login_required
def logout_view(request):
    logout(request)
    #del request.session['username']
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        password_conf = request.POST['password_confirmation']
        if password != password_conf:
            return render(request, 'users/signup.html', {'error': 'Las contraseñas no coinciden'})
        try: 
            user = User.objects.create_user(username = username, password=password)
        except Exception as e:
            return render(request, 'users/signup.html', {'error': str(e)})
        user.first_name = request.POST['name']
        user.save()
        cart = Cart(user = user)
        cart.save()
        request.session['username'] = username
        user = authenticate(request, username = username, password = password)
        login(request, user)
        user = request.session['username']
        try: 
            next_url = request.session['next']
        except:
            return redirect('login')
        else:
            del request.session['next']
            return redirect(next_url)
        #return redirect('login')
    try:
        user = request.session['username']
    except:
        return render(request, 'users/signup.html')
    else:
        return redirect('home')

@login_required      
def add_address(request):
    if request.method == 'POST':
        if 'where' in request.POST:
            return render(request, 'users/address.html')
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        direccion = request.POST['direccion']
        cp  = request.POST['cp']
        ciudad = request.POST['ciudad']
        numero = request.POST['numero']
        correo = request.POST['correo']
        adicional = request.POST['adicional']

        try: 
            address = Address.objects.get(user = request.user)
        except:
            address = Address(nombre = nombre, apellido = apellido, direccion = direccion, cp = cp, 
                            ciudad = ciudad, numero = numero, correo = correo, adicional = adicional,
                            user = request.user, recordar = True)
            address.save()
        else:
            address.nombre = nombre
            address.apellido = apellido
            address.direccion = direccion
            address.cp = cp
            address.ciudad = ciudad
            address.numero = numero
            address.correo = correo
            address.adicional = adicional
            address.save()

    return redirect('payment')
