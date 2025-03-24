from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# ✅ Correct Custom User Model
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Add custom fields here if needed
    pass

# ✅ Product Model
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids'),
    ]
    
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name  # ✅ Fix: Return only the name as a string
