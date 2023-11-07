from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class MiFormilarioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #help_texts = {'username': '','email': '', 'password1': '', 'password2': '',}
        help_texts = {key: '' for key in fields}
        