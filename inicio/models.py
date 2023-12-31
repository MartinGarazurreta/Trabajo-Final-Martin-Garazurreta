from django.db import models
from ckeditor.fields import RichTextField

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = RichTextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'
    
class Camion(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'
    
class Vans(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio}'