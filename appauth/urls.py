from django.urls import path
from . import views

app_name = "appauth"

urlpatterns = [
    path("login", views.applogin, name="login"),
    path("register", views.register, name="register"),
    path("captcha", views.send_email_captcha, name="send_captcha"),
    path("logout", views.applogout, name="logout"),
]