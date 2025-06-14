from django.db import models

governorates = {
    'cairo': 'Cairo Governorate',
    'giza': 'Giza Governorate',
    'alexandria': 'Alexandria Governorate',
    'fayoum': 'Fayoum Governorate',
    'aswan': 'Aswan Governorate',
}

class WarehouseShippingCost(models.Model):
    governorate_name = models.CharField(max_length=100, null=False, blank=False, choices=list(governorates.items()),
                                        unique=True)
    shipping_cost = models.DecimalField(decimal_places=2, max_digits=10)


class Warehouse(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False, choices=list(governorates.items()))

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
        shipping = WarehouseShippingCost.objects.get(governorate_name=self.location)
        return shipping.shipping_cost or 0
