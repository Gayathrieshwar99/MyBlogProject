from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # CORRECT!

        
class UserRegisterForm(UserCreationForm): # Inherit from UserCreationForm
    email = forms.EmailField() # Add email field

    class Meta(UserCreationForm.Meta): # Inherit Meta from UserCreationForm
        model = User
        fields = UserCreationForm.Meta.fields + ('username','email','password', 'password2') # Add email to fields