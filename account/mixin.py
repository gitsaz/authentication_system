from django.shortcuts import redirect

# if user already logged in then redirect home page
class RedirectAuthenticatedUserMixin:
    redirect_url = 'home'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)