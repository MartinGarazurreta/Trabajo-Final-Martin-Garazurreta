from django.urls import path
from inicio.views import inicio, autos, crear_auto, Camion, crear_camion, Vans, crear_vans
urlpatterns = [
    path('', inicio, name='inicio'),
    path('autos/', autos, name='autos'),
    path('autos/crear/', crear_auto, name='crear_auto'),
    path('camion/', Camion, name='camion'),
    path('camion/crear/', crear_camion, name='crear_camion'),
    path('vans/', Vans, name='vans'),
    path('vans/crear/', crear_vans, name='crear_vans'),
]
