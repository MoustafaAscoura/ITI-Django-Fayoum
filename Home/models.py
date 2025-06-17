import random

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.conf import settings

governorates = {
    'cairo': 'Cairo Governorate',
    'giza': 'Giza Governorate',
    'alexandria': 'Alexandria Governorate',
    'fayoum': 'Fayoum Governorate',
    'aswan': 'Aswan Governorate',
}

class Warehouse(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, validators=[MinLengthValidator(4)])
    location = models.CharField(max_length=100, null=False, blank=False, choices=list(governorates.items()))

    description = models.TextField(null=False, blank=False, validators=[MaxLengthValidator(1000)])
    capacity = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(100000)])
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    @property
    def full_location(self):
        short_location = self.location
        full_location = governorates[short_location]
        return full_location

    @property
    def shipping_cost(self):
        return random.randint(10,100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'location'], name='unique_name_and_location_constraint'),
        ]
