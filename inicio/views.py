from django.shortcuts import render
from inicio.models import Paleta
def inicio(request):


    return render(request, "inicio/inicio.html", {})
def paletas(request):
    
    paleta = Paleta(marca='wilson', descripcion='paleta de vela', anio=2022)
    paleta.save()
    return render(request, 'inicio/paletas.html', {'paleta': paleta})
