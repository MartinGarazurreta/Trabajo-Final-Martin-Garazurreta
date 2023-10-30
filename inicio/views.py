from django.shortcuts import render, redirect
from inicio.models import Auto
from inicio.forms import CrearAutoFormulario
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
            paleta = Auto(marca=marca.lower(), descripcion=descripcion, anio=anio)
            paleta.save()
            
            return redirect('autos')
        else: 
            return render(request, 'inicio/crear_auto.html', {'formulario': formulario})
    formulario = CrearAutoFormulario()    
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})