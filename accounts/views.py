from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import MiFormilarioDeCreacion 


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST) 
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra) 
            
            django_login(request, user)
            
            return redirect('inicio')
        else:
            return render(request, 'accounts/login.html', {'formulario_de_login': formulario})
    formulario = AuthenticationForm()
    return render(request, 'accounts/login.html', {'formulario_de_login': formulario})

def registro(request):
    formulario = MiFormilarioDeCreacion()
    
    if request.method == 'POST':
        formulario = MiFormilarioDeCreacion()
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
    
    
    return render(request, 'accounts/registro.html', {'formulario_de_registro': formulario})
