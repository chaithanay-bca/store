from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product  

# ✅ Class-based Product List View
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

# ✅ Home Page
def home(request):
    products = Product.objects.all()  # Fetch products from the database
    return render(request, 'home.html', {'products': products})

# ✅ Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to homepage
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'accounts/login.html')

# ✅ Logout View
def user_logout(request):
    logout(request)
    return redirect('home')

# ✅ Register View
def user_register(request):
    return render(request, 'accounts/register.html')

# ✅ Product List View (Function-based)
def product_list(request):
    products = Product.objects.all()  # Fetch all products from DB
    return render(request, 'products/product_list.html', {'products': products})
