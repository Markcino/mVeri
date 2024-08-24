from django.urls import path
from . import views

urlpatterns = [
    path('login', views.do_login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.do_logout, name="logout"),
]
