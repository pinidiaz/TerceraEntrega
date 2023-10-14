from django import forms

class ProductoFormulario(forms.Form):

    nombre=forms.CharField()
    marca=forms.CharField()

class ClienteFormulario(forms.Form):

    usuario=forms.CharField()
    cliente=forms.CharField()

class CerveceriaFormulario(forms.Form):

    nombre=forms.CharField()
    ciudad=forms.CharField()
    direccion=forms.CharField()

class Clientes1Formulario(forms.Form):

    usuario=forms.CharField()
    cliente=forms.CharField()   

