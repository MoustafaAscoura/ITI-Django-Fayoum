import random

from django.db import models

governorates = {
    'cairo': 'Cairo Governorate',
    'giza': 'Giza Governorate',
    'alexandria': 'Alexandria Governorate',
    'fayoum': 'Fayoum Governorate',
    'aswan': 'Aswan Governorate',
}

class Warehouse(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False, choices=list(governorates.items()))

    description = models.TextField(null=False, blank=False)
    capacity = models.IntegerField(null=False, blank=False)
    manager = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)

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
