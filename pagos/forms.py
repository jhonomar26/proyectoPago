# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from .models import Usuario, Ingreso 
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError



class RegistroForm(forms.Form):
    # Campos para el modelo de Usuarios de Django
    username = forms.CharField(max_length=50, label="Nombre de usuario")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(
        widget=forms.PasswordInput, label="Confirmar contraseña"
    )
    # Campos para el modelo Usuarios
    email = forms.EmailField(max_length=254, label="Correo electrónico")



class CustomInicioSesionForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ["username", "password"]

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['descripcion', 'monto', 'fechaIngreso', 'categoria']  # Lista de campos del modelo que quieres incluir en el formulario
