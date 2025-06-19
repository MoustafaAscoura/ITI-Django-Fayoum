from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordMixin
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        exclude = ('id', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', "groups", "user_permissions")

class UserEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profile_picture']
