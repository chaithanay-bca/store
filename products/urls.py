from django.contrib import admin
from django.urls import path
from .views import user_login, user_logout, home  # Removed product-related imports

urlpatterns = [
    path('', home, name='home'),  # ✅ Homepage
    path('login/', user_login, name='login'),  # ✅ Login View
    path('logout/', user_logout, name='logout'),  # ✅ Logout View
    path('admin/', admin.site.urls),  # ✅ Admin Panel
]
