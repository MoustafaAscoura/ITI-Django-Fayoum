from django.http import HttpResponse
from django.shortcuts import render
from .models import Warehouse

def index(request):
    warehouse_location = request.GET.get('warehouse_location') or 'Cairo'
    return render(request, 'Home/index.html', context={"warehouse_location": warehouse_location})

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    return render(request, 'Home/contact.html')

def dashboard(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'Home/dashboard.html', context={"warehouses": warehouses})
