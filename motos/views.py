from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from motos.models import Moto
from django.urls import reverse_lazy

class ListaDeMotos(ListView):
    model = Moto
    context_object_name = 'listado_de_motos'
    template_name = 'motos/Motos.html'

class CrearMotos(CreateView):
    model = Moto
    template_name = 'motos/crear_motos.html'
    fields = ['marca', 'modelo', 'fecha_creacion']
    success_url = reverse_lazy('Motos')

