from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *

class CreateStudentForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']  # List only the fields you want to show

class TranscriptRequestForm(forms.ModelForm):
    class Meta:
        model = TranscriptRequest
        fields = ['student','institution', 'doc_type', 'request_date', 'delivery_email', 'purpose']
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date'}),
            'doc_type': forms.Select(choices=TranscriptRequest.DOC_TYPE_CHOICES),
            'purpose': forms.Textarea(attrs={'rows': 4}),
        }
