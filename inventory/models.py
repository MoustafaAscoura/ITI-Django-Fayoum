from django.db import models
from django.db.models import OneToOneRel

from Home.models import Warehouse


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ='Categories'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to="products/%y/%m/%d", default="/products/default.png")
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name
