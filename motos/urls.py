from django.urls import path 
from motos.views import ListaDeMotos, CrearMotos

urlpatterns = [
    path('motos/', ListaDeMotos.as_view(), name='motos'),
    path('motos/crear/', CrearMotos.as_view(), name='crear_motos')
]

