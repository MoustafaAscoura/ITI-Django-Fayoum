from django.urls import path
from . import views

urlpatterns = [
    path('', views.InventoryPage.as_view(), name="inventory"),
    path('function', views.inventory_page, name="inventory"),
]
