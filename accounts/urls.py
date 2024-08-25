from django.urls import path
from . import views

urlpatterns = [
    path('do_login', views.do_login, name="do_login"),
    path('register', views.register, name="register"),
    path('logout', views.do_logout, name="logout"),
]
