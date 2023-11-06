from django.urls import path 
from motos.views import ListaDeMotos, CrearMotos, ActualizarMoto, EliminarMoto, DetalleMoto

urlpatterns = [
    path('motos/', ListaDeMotos.as_view(), name='motos'),
    path('motos/crear/', CrearMotos.as_view(), name='crear_motos'),
    path('motos/<int:pk>/', DetalleMoto.as_view, name='detalle_moto'),
    path('motos/<int:pk>/actualizar/', ActualizarMoto.as_view(), name='actualizar_moto'),
    path('motos/<int:pk>/eliminar/', EliminarMoto.as_view(), name='eliminar_moto'),
]

