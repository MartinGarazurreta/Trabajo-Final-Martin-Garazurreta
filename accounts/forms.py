from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
        
class EdicionFormulario(UserChangeForm):
    password = None
    email = forms.EmailField(label='Camibiar email', required=False)
    first_name = forms.CharField(label='Cambiar nombre', required=False)
    last_name = forms.CharField(label='cambiar apellido', required=False)
    biografia = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    
    class Meta:
            model = User
            fields = ['email', 'first_name', 'last_name', 'biografia', 'avatar']
        
    
        