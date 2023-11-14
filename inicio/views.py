from django.shortcuts import render, redirect
from inicio.models import Auto
from inicio.forms import CrearAutoFormulario, ActualizarAutoFormulario
from inicio.models import Camion
from inicio.forms import CrearCamionFormulario
from inicio.models import Vans
from inicio.forms import CrearVansFormulario
from django.contrib.auth.decorators import login_required


def inicio(request):


    return render(request, "inicio/inicio.html", {})
def autos(request):
    
      
    
    marca_a_buscar = request.GET.get('marca')
    if marca_a_buscar:
        listado_de_autos = Auto.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_de_autos = Auto.objects.all() 
   
    return render(request, 'inicio/autos.html', {'listado_de_autos': listado_de_autos})

@login_required
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
            modelo = info_limpia.get('modelo')
            anio = info_limpia.get('anio')
            auto = Auto(marca=marca.lower(), modelo=modelo, anio=anio)
            auto.save()
            
            return redirect('autos')
        else: 
            return render(request, 'inicio/crear_auto.html', {'formulario': formulario})
    formulario = CrearAutoFormulario()    
    return render(request, 'inicio/crear_autos.html', {'formulario': formulario})

def camiones(request):
    listado_de_camiones = Camion.objects.all()
    
    return render(request, 'inicio/camiones.html', {'listado_de_camiones': listado_de_camiones})

@login_required
def crear_camion(request):
    if request.method == 'POST':
       
        formulario = CrearCamionFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            anio = info_limpia.get('anio')
            camion = Camion(marca=marca.lower(), modelo=modelo, anio=anio)
            camion.save()
            
            return redirect('camion')
        else: 
            return render(request, 'inicio/crear_camiones.html', {'formulario': formulario})
    formulario = CrearCamionFormulario()    
    return render(request, 'inicio/crear_camiones.html', {'formulario': formulario})

def vans(request):
    listado_de_vans = Vans.objects.all()
    
    return render(request, 'inicio/vans.html', {'listado_de_vans': listado_de_vans})

@login_required
def crear_vans(request):
    if request.method == 'POST':
       
        formulario = CrearVansFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            anio = info_limpia.get('anio')
            van = Vans(marca=marca.lower(), modelo=modelo, anio=anio)
            van.save()
            
            return redirect('vans')
        else: 
            return render(request, 'inicio/crear_vans.html', {'formulario': formulario})
    formulario = CrearVansFormulario()    
    return render(request, 'inicio/crear_vans.html', {'formulario': formulario})

@login_required
def eliminar_auto(request, auto_id):
    auto_a_eliminar = Auto.objects.get(id=auto_id)
    auto_a_eliminar.delete()
    return redirect("autos")

@login_required
def actualizar_auto(request, auto_id):
    auto_a_actualizar = Auto.objects.get(id=auto_id)
    if request.method == 'POST':
        formulario = ActualizarAutoFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
                
            auto_a_actualizar.marca = info_nueva.get('marca')
            auto_a_actualizar.modelo = info_nueva.get('modelo')  
            auto_a_actualizar.anio = info_nueva.get('anio')
            
            auto_a_actualizar.save()     
            return redirect('autos')
        return render(request, 'auto', 'inicio/actualizar_auto.html', {'formulario': formulario})  
           
    formulario = ActualizarAutoFormulario(initial={'marca': auto_a_actualizar.marca, 'descripcion': auto_a_actualizar.modelo, 'anio': auto_a_actualizar.anio})
    return render(request, 'inicio/actualizar_auto.html', {'formulario': formulario})
    
def detalle_auto(request, auto_id):
    auto_detalles = Auto.objects.get(id=auto_id)
    
    return render(request, 'inicio/detalle_auto.html', {'auto': auto_detalles})

