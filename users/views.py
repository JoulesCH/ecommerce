from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            request.session['username'] = username
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'users/login.html', {'error': 'Datos inválidos'})
    try:
        user = request.session['username']
    except:
        return render(request, 'users/login.html')
    else:
        return redirect('home')

@login_required
def logout_view(request):
    logout(request)
    #del request.session['username']
    return redirect('login')

def suscribe(request):
    return render(request, 'users/suscribe.html')
    