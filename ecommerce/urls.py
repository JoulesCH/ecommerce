"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ecommerce import views as home_view

from products import views as product_views
from users import views as user_views
from shoppingcarts import views as cart_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view.home, name = 'home'),
    path('user/login/', user_views.login_view, name ='login'),
    path('logout/', user_views.logout_view, name ='logout'),
    path('add/<int:ide>', product_views.add, name ='add_cart' ),
    path('user/signup/',  user_views.signup, name = 'signup'),

    path('pruebas/', home_view.prueba, name = 'prueba'),
    path('cart/', cart_views.cart, name = 'cart'),
    path('remove/<int:ide>', product_views.remove, name = 'remove_cart'),
    path('payment/', cart_views.payment, name = 'payment'),
    path('cart/option/<int:ide>', product_views.select_option, name = 'option'),
    path('product/<int:ide>', product_views.product,name = 'product'),
    path('add_address', user_views.add_address, name = 'add_address')
]
