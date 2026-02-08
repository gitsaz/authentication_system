from django.urls import path


from django.contrib.auth.views import(
    PasswordResetCompleteView
)


from .views import(
    HomeView,
    LoginView,
    LogoutView, 
    RegistrationView,
    ChangePassword, 
    UserPasswordResetView,
    UserPasswordResetDoneView,
    UserPasswordResetConfirmView
)

urlpatterns = [
    path("",HomeView.as_view(), name="home"),
    path("login/",LoginView.as_view(), name="login"),
    path("logout/",LogoutView.as_view(), name="logout"),
    path("registration/",RegistrationView.as_view(), name="registration"),
    path("password_change", ChangePassword.as_view(), name="password_change"),
    path("password_reset/", UserPasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/",  PasswordResetCompleteView.as_view(), name="password_reset_complete")
    
    
]

