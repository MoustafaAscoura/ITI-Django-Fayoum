from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the home page.")
    warehouse_location = request.GET.get('warehouse_location') or 'Cairo'
    return render(request, 'Home/index.html', context={"warehouse_location": warehouse_location})

def about(request):
    # return HttpResponse("<h1>This is about me.</h1>")
    return render(request, 'Home/about.html')

def contact(request):
    # return HttpResponse("<h1>This is Contact Us page.</h1>")
    return render(request, 'Home/contact.html')
