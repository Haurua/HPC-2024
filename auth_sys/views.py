from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = "auth_sys/login.html"
    next_page = reverse_lazy("dashboard")
    redirect_authenticated_user = reverse_lazy("dashboard")


class Logout(LogoutView):
    next_page = "login"
