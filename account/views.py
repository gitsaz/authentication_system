from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    PasswordChangeForm
)
from .mixin import RedirectAuthenticatedUserMixin

#view start from hare

#home page view
@method_decorator(never_cache, name='dispatch')
class HomeView(LoginRequiredMixin, generic.TemplateView):
    login_url = 'login'
    template_name = "account/index.html"


#login page view
@method_decorator(never_cache, name='dispatch')
class LoginView(RedirectAuthenticatedUserMixin, generic.View):
    def get(self, *args, **kwargs):
        form = UserLoginForm()
        context ={
            "form":form
        }
        return render(self.request, 'account/login.html', context)
    
    def post(self, *args, **kwargs):
        form = UserLoginForm(self.request.POST)
        
        if form.is_valid():
            user = authenticate(
                self.request,
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )
            if user:
                login(self.request,user)
                return redirect('home')
            else:
                messages.warning(self.request,"Wrong Credential!")
                return redirect('login')
        context = {
            "form":form
        }
            
        return render(self.request, "account/login.html", context)


# logout view
class LogoutView(generic.View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')


# registration view
@method_decorator(never_cache, name="dispatch")
class RegistrationView(generic.CreateView):
    template_name = 'account/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, "Registration Successful!")
        return super().form_valid(form)
    
    
# password change view
@method_decorator(never_cache, name='dispatch')
class ChangePassword(LoginRequiredMixin, generic.FormView):
    template_name = 'account/password_change.html'
    form_class = PasswordChangeForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('login')
    
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        user.set_password(form.cleaned_data.get('new_password'))
        user.save()
        messages.success(self.request, "Password Changed Successfully!")
        return super().form_valid(form)
    
    
    
class UserPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
    