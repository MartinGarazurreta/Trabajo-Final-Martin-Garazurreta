from django import forms 

class CrearPalteaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.ChoiceField(max_length=250)
    anio = forms.IntegerField()
    