from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView


class RegisterPageView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login-page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginPageView(LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('task-list-page')


class LogoutPageView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))
