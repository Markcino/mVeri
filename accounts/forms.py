from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CreateStudentForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']  # List only the fields you want to show
