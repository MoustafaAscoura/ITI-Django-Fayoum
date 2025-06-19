from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import UserForm, UserEditForm
from accounts.models import CustomUser


class SignUpView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "registration/signup.html"
    success_url = "/accounts/login"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False

        # send email to user

        user.save()
        return super(SignUpView, self).form_valid(form)


class UpdateProfileView(UpdateView):
    model = CustomUser
    template_name = "registration/edit_profile.html"
    form_class = UserEditForm
    success_url = "/accounts/profile"

    def get_object(self):
        return self.request.user

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"

# class ProfileView(LoginRequiredMixin, DetailView):
#     model = CustomUser
#     template_name = "registration/profile.html"
#
#     def get_object(self):
#         user = CustomUser.objects.get(id=self.request.user.id)
#         user = self.request.user
#         return user


