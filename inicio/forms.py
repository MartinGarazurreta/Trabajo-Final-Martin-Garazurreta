from django import forms 
from ckeditor.fields import RichTextFormField
class BaseAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = RichTextFormField()
    anio = forms.IntegerField()


class CrearAutoFormulario(BaseAutoFormulario):
    ...

class ActualizarAutoFormulario(BaseAutoFormulario):
    ...

class CrearCamionFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
class CrearVansFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
    