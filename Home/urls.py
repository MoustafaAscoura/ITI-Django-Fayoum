from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('warehouses/', views.GetAllWarehouses.as_view(), name="warehouses"),
    path('warehouses/details/<int:pk>', views.GetOneWarehouse.as_view(), name="warehouse_details"),
    path('warehouses/add', views.CreateWarehouse.as_view(), name="create_warehouse"),

    path('purchase_orders/', views.about, name="purchase_orders"),
    path('sales_orders/', views.about, name="sales_orders"),
    path('customers/', views.about, name="customers"),
]
