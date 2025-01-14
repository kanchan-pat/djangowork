from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)

    def __str__(self):
        return self.name

