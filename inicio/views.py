from django.shortcuts import render, redirect
from inicio.models import Auto
from inicio.forms import CrearAutoFormulario
from inicio.models import Camion
from inicio.forms import CrearCamionFormulario
from inicio.models import Vans
from inicio.forms import CrearVansFormulario

def inicio(request):


    return render(request, "inicio/inicio.html", {})
def autos(request):
    
      
    
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        listado_de_autos = Auto.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_de_autos = Auto.objects.all() 
   
    return render(request, 'inicio/autos.html', {'listado_de_autos': listado_de_autos})
def crear_auto(request):
   
    #print('===============')
    #print('GET')
    #print(request.GET)
    #print('================')
    #print('POST')
    #print(request.POST)
    #if request.method == 'POST':
     #   marca = request.POST.get('marca')
     #   descripcion = request.POST.get('descripcion')
     #   anio = request.POST.get('anio')
     #   auto = Paleta(marca=marca, descripcion=descripcion, anio=anio)
     #   auto.save()
     
     
    if request.method == 'POST':
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            auto = Auto(marca=marca.lower(), descripcion=descripcion, anio=anio)
            auto.save()
            
            return redirect('autos')
        else: 
            return render(request, 'inicio/crear_auto.html', {'formulario': formulario})
    formulario = CrearAutoFormulario()    
    return render(request, 'inicio/crear_autos.html', {'formulario': formulario})

def crear_camion(request):
    if request.method == 'POST':
       
        formulario = CrearCamionFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            camion = Camion(marca=marca.lower(), descripcion=descripcion, anio=anio)
            camion.save()
            
            return redirect('camion')
        else: 
            return render(request, 'inicio/crear_camiones.html', {'formulario': formulario})
    formulario = CrearCamionFormulario()    
    return render(request, 'inicio/crear_camiones.html', {'formulario': formulario})

def crear_vans(request):
    if request.method == 'POST':
       
        formulario = CrearVansFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            vans = Vans(marca=marca.lower(), descripcion=descripcion, anio=anio)
            vans.save()
            
            return redirect('autos')
        else: 
            return render(request, 'inicio/crear_vans.html', {'formulario': formulario})
    formulario = CrearVansFormulario()    
    return render(request, 'inicio/crear_vans.html', {'formulario': formulario})