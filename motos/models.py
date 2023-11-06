from django.db import models

class Moto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=250)
    fecha_creacion = models.DateField()
    
    def __strr__(self):
        return f'{self.marca} - {self.modelo} - {self.fecha_creacion}'
