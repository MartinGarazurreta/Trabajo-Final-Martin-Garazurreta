from django.urls import path
from inicio.views import inicio, autos, crear_auto
urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', autos, name='autos'),
    path('paletas/crear/', crear_auto, name='crear_auto'),
]
