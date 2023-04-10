from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout, login
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import UserCreateForm, LoginUserForm


class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('base:tasks')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

def logout_user(request):
    logout(request)
    return redirect('/')