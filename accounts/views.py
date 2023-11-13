from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import MiFormilarioDeCreacion, EdicionFormulario
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.models import DatosExtra

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST) 
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra) 
            
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            return redirect('inicio')
        else:
            return render(request, 'accounts/login.html', {'formulario_de_login': formulario})
    formulario = AuthenticationForm()
    return render(request, 'accounts/login.html', {'formulario_de_login': formulario})

def registro(request):
    formulario = MiFormilarioDeCreacion()
    
    if request.method == 'POST':
        print("ES POST")
        formulario = MiFormilarioDeCreacion(request.POST)
        if formulario.is_valid():
            print("Es Valido")
            formulario.save()

            return redirect('login')

    
    
    return render(request, 'accounts/registro.html', {'formulario_de_registro': formulario})

def editar_perfil(request):
    
    datos_extra = request.user.datosextra
        
    formulario = EdicionFormulario(initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar},instance=request.user)
    
    if request.method == 'POST':
        formulario = EdicionFormulario(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar
                
            datos_extra .save()
            formulario.save()
            
            return redirect('edtitar_perfil')
    
    return render(request, 'accounts/editar_perfil.html', {'formulario':formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'accounts/cambiar_password.html'
    success_url = reverse_lazy('editar_perfil')
