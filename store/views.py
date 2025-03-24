from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from products.models import Product  # ✅ Corrected import

# ✅ Home Page View
def home(request):
    return render(request,'store/home.html')  # Ensure this template exists

# ✅ User Login View
def user_login(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')  # ✅ Ensure correct path
def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout

# ✅ User Logout View
def user_logout(request):
    logout(request)
    return redirect('home')

# ✅ User Register View
def user_register(request):
    return render(request, 'register.html')  # ✅ Ensure correct path

# ✅ Product List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
def home(request):
    return render(request, 'home.html')

def user_login(request):
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')

def user_logout(request):
    return render(request, 'logout.html')