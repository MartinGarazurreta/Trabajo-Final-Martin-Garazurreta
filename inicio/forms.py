from django import forms 
class BaseAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=250)
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
    
    