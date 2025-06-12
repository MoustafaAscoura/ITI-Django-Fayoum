from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the home page.")
    return render(request, 'Home/index.html')

def about(request):
    return HttpResponse("<h1>This is about me.</h1>")

def contact(request):
    return HttpResponse("<h1>This is Contact Us page.</h1>")
