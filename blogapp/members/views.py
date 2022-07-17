from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserRegisterForm, UserEditForm, ChangePwdForm
from django.contrib.auth.views import PasswordChangeView

class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    form_class =  ChangePwdForm
    template_name = 'registration/password_change.html'
    success_url = '/'

