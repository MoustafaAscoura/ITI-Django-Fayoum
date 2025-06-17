from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

from inventory.models import Product


@login_required
def inventory_page(request):
    page = int(request.GET.get('page') or 1)
    limit = int(request.GET.get('limit') or 10)
    sort_by = request.GET.get('sort') or "id"
    if request.GET.get('dir') == "desc":
        sort_by = "-" + sort_by
    query = request.GET.get('query')
    if query:
        products = Product.objects.order_by(sort_by).filter(
            Q(name__icontains=query) | Q(categories__name__icontains=query))[(page - 1) * limit: page * limit]
    else:
        products = Product.objects.order_by(sort_by).all()[(page - 1) * limit: page * limit]

    return render(request, "inventory/products.html", {'products': products})


class InventoryPage(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'inventory/products.html'

    def get_queryset(self):
        page = int(self.request.GET.get('page') or 1)
        limit = int(self.request.GET.get('limit') or 10)

        products = self.model.objects.order_by("id").all()[(page - 1) * limit: page * limit]
        return products
