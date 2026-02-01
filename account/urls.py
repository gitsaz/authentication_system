from django.urls import path

from .views import(
    home,
    login
)

urlpatterns = [
    path("",home.as_view(), name="home"),
    path("login/",login.as_view(), name="login")
]
