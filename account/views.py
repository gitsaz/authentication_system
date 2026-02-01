from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

from .forms import UserLoginForm

#view start from hare
#home page view
class home(PermissionRequiredMixin, generic.TemplateView):
    template_name = "account/index.html"


#login page view
class login(generic.View):
    def get(self, *args, **kwargs):
        form = UserLoginForm()
        context ={
            "form":form
        }
        return render(self.request, 'account/login.html', context)
    
    def post(self, *args, **kwargs):
        pass