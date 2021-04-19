from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from shoppingcarts.models import Cart
# Create your views here.
def login_view(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                request.session['username'] = username
                return redirect('home')
            else:
                next_url = request.POST.get('next')
                print(next_url)
                if next_url:
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
        return redirect('login')
    try:
        user = request.session['username']
    except:
        return render(request, 'users/signup.html')
    else:
        return redirect('home')
    