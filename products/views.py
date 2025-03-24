from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from products.models import Product  # Ensure Product model exists
from .models import CustomUser  # Ensure CustomUser model exists

# ✅ Home Page View
@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# ✅ User Registration View
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        user = CustomUser.objects.create(username=username, password=make_password(password))
        user.save()
        login(request, user)
        return redirect("home")
    
    return render(request, "register.html")

# ✅ User Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    
    return render(request, "login.html")

# ✅ User Logout View
def user_logout(request):
    logout(request)
    return redirect("home")

# ✅ Password Reset View
def reset_password(request):
    if request.method == "POST":
        username = request.POST["username"]
        user = CustomUser.objects.filter(username=username).first()
        
        if user:
            new_password = request.POST["new_password"]
            user.password = make_password(new_password)
            user.save()
            messages.success(request, "Password reset successful!")
            return redirect("login")
        else:
            messages.error(request, "Username not found")
    
    return render(request, "reset_password.html")

# ✅ Product List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# ✅ Product Filtering View
@login_required
def filter_products(request, category):
    if category == "All":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=category)
    
    return render(request, "home.html", {"products": products})

# ✅ Add to Cart (Session-Based)
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get("cart", [])
    
    if product_id not in cart:
        cart.append(product_id)
        request.session["cart"] = cart
    
    messages.success(request, f"{product.name} added to cart!")
    return redirect("home")

# ✅ View Cart
@login_required
def view_cart(request):
    cart = request.session.get("cart", [])
    products = Product.objects.filter(id__in=cart)
    return render(request, "cart.html", {"products": products})
