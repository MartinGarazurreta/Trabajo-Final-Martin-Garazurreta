from django.urls import path
from inicio.views import inicio, autos, crear_auto
urlpatterns = [
    path('', inicio, name='inicio'),
    path('autos/', autos, name='autos'),
    path('autos/crear/', crear_auto, name='crear_auto'),
]
