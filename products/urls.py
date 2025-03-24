from django.contrib import admin
from django.urls import path, include
from .views import user_login, user_logout, home, ProductListView, product_list
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home, name='home'),  # ✅ Homepage
    path('products/', ProductListView.as_view(), name='product-list'),  # ✅ Product List View (Class-based)
    path('products/list/', product_list, name='product-list-fb'),  # ✅ Function-based view for listing products
    path('admin/', admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="product_list.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path('', views.product_list, name='product_list'),
]
