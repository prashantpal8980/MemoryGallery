from django import forms 
from .models import Incident
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class IncidentForm(forms.ModelForm):
    class Meta:
        model=Incident
        fields=['text','photo']
    
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']