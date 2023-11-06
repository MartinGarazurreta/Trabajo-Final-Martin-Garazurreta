from django.urls import path
from inicio.views import inicio, autos, crear_auto, camiones, crear_camion, vans, crear_vans, eliminar_auto, actualizar_auto, detalle_auto
urlpatterns = [
    path('', inicio, name='inicio'),
    path('autos/', autos, name='autos'),
    path('autos/crear/', crear_auto, name='crear_auto'),
    path('autos/<int:auto_id>/eliminar/', eliminar_auto, name='eliminar_auto'),
    path('autos/<int:auto_id>/actualizar/', actualizar_auto, name='actualizar_auto'),
    path('autos/<int:auto_id>/', detalle_auto, name='detalle_auto'),
    path('camion/', camiones, name='camion'),
    path('camion/crear/', crear_camion, name='crear_camion'),
    path('vans/', vans, name='vans'),
    path('vans/crear/', crear_vans, name='crear_vans'),
]
