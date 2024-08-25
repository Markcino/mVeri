from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *

class CreateStudentForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']  # List only the fields you want to show

class RequestForm(forms.Form):
    student = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    requester_email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    institution = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    request_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    doc_type = forms.ChoiceField(choices=RequestDocument.DOC_TYPE_CHOICES)
    purpose = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    

