from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # ✅ Recommended for newer Django versions
    name = 'products'  # ✅ App name



    
    