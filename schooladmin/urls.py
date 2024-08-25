from django.urls import path
from . import views

urlpatterns = [
    path('school_admin_dashboard', views.school_admin_dashboard,
         name="school-admin-dashboard"),
]