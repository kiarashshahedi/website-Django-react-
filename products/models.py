from django.db import models
from users.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name
