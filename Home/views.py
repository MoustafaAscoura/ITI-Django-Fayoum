from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView

from .models import Warehouse

def index(request):
    warehouse_location = request.GET.get('warehouse_location') or 'Cairo'
    return render(request, 'Home/index.html', context={"warehouse_location": warehouse_location})


def about(request):
    return render(request, 'Home/about.html')


def contact(request):
    return render(request, 'Home/contact.html')

# function based views
# def warehouses(request):
#     warehouses = Warehouse.objects.all()
#     return render(request, 'Home/warehouses.html', context={"warehouses": warehouses})

#
# def warehouse_details(request, pk):
#     try:
#         warehouse = Warehouse.objects.get(id=pk)
#     except:
#         return render(request, 'errors/404.html', status=404)
#
#     return render(request, 'Home/warehouse_details.html', context={"warehouse": warehouse})


def create_warehouse(request):
    if request.method == "GET":
        return render(request, 'Home/create_warehouse.html')

    elif request.method == "POST":
        new_warehouse = Warehouse(
            name=request.POST['name'],
            location=request.POST['location'],
            capacity=request.POST['capacity'],
            manager_id=request.user.id
        )
        new_warehouse.save()
        return redirect("/warehouses")


# Class based views
class GetAllWarehouses(ListView):
    model = Warehouse
    template_name = "Home/warehouses.html"
    context_object_name = "warehouses"

class GetOneWarehouse(DetailView):
    model = Warehouse
    template_name = "Home/warehouse_details.html"
    context_object_name = "warehouse"
    # pk_url_kwarg = "pk"

# FORMS ?
class CreateWarehouse(CreateView):
    model = Warehouse
    template_name = "Home/create_warehouse.html"
    success_url = "/warehouses"

    def post(self, request, *args, **kwargs):
        new_warehouse = Warehouse(
            name=request.POST['name'],
            location=request.POST['location'],
            capacity=request.POST['capacity'],
            manager_id=request.user.id
        )
        new_warehouse.save()
        return redirect("/warehouses")
