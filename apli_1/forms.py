from django import forms
from .models import Cliente

class Cliente_form(forms.Form):
    nombre_cliente = forms.CharField(max_length=50, label="nombre")
    apellido_cliente = forms.CharField(max_length=50, label="apellido")
    telefono_cliente = forms.CharField(max_length=50, label="telefono")
    email_cliente = forms.EmailField(label="email")
    clave_cliente = forms.CharField(max_length=50, label="clave")
    imagen_cliente = forms.ImageField(label="imagen")




class Usuario_form(forms.Form):
    nombre_usuario = forms.CharField(label="nombre")
    clave_usuario = forms.CharField(max_length=50, label="clave")