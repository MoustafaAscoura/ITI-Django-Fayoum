from django.urls import path

from . import views

# Route - Path  --> "/home" "/cart"
# Rule -> If user go to path, then go to function
# View function
# Router

urlpatterns = [
    path('', views.index, name='index'), # Rule
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
