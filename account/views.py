from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserLoginForm
from .mixin import RedirectAuthenticatedUserMixin

#view start from hare
#home page view
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "account/index.html"


#login page view
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
class RegistrationView(generic.TemplateView):
    template_name = 'account/registration.html'