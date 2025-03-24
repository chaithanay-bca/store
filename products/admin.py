from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # ✅ Removed Product import

# ✅ Register CustomUser properly
admin.site.register(CustomUser, UserAdmin)
