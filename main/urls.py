from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.user_register, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_user, name="logout"),
]