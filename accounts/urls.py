from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("edit/", views.UpdateProfileView.as_view(), name="edit_profile"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
]