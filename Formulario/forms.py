from django import forms
from .models import Register
from django.contrib.auth.hashers import make_password

# Formulario para el registro
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register  # Modelo del cual trae los datos
        fields = [
            'name',
            'username',
            'email',
            'password',

        ]

# Formulario de Django para el login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
