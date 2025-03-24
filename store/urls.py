from django.contrib import admin
from django.urls import path, include
from store import views  # ✅ Import views properly

urlpatterns = [
    path('', views.home, name='home'),  # ✅ Home page
    path('admin/', admin.site.urls),  # ✅ Admin page
       path('', include('products.urls')),
    path('products/', include('products.urls')),  # ✅ Include products app
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    
]
