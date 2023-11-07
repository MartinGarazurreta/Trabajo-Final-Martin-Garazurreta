from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from motos.models import Moto
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaDeMotos(ListView):
    model = Moto
    context_object_name = 'listado_de_motos'
    template_name = 'motos/Motos.html'

class CrearMotos(LoginRequiredMixin, CreateView):
    model = Moto
    template_name = 'motos/crear_motos.html'
    fields = ['marca', 'modelo', 'fecha_creacion']
    success_url = reverse_lazy('motos')

class ActualizarMoto(LoginRequiredMixin, UpdateView):
    model = Moto
    template_name = 'motos/actualizar_moto.html'
    fields = ['marca', 'modelo', 'fecha_creacion']
    success_url = reverse_lazy('motos')
class DetalleMoto(DetailView):
    model = Moto
    template_name = 'motos/detalle_moto.html'
class EliminarMoto(LoginRequiredMixin, DeleteView):
    model = Moto
    template_name = 'motos/eliminar_moto.html'
    success_url = reverse_lazy('motos')
    