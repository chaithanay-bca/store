from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product

# ✅ Register CustomUser model properly
admin.site.register(CustomUser, UserAdmin)

# ✅ Register Product model properly
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


