# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    BUYER = 'buyer'
    SELLER = 'seller'
    USER_TYPES = [
        (BUYER, 'Buyer'),
        (SELLER, 'Seller'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default=BUYER)
    store_name = models.CharField(max_length=255, blank=True, null=True)  # Only applicable for sellers

    # New fields added to user profile
    first_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(blank=True, null=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    address = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    meli_card_number = models.CharField(max_length=10, unique=True, blank=True, null=True)

    # Add other fields as needed
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.family_name}"
    
    def is_seller(self):
        return self.user_type == self.SELLER
