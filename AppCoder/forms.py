from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar


class ProductoFormulario(forms.Form):

    nombre=forms.CharField()
    marca=forms.CharField()
    precio=forms.DecimalField(max_digits=10, decimal_places=2)

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

class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contaseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contaseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"] 


class AvatarFormulario(forms.ModelForm):
     
     class Meta:
         model = Avatar
         fields = ["imagen"]