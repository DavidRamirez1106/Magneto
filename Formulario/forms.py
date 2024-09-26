from django import forms
from .models import Register, DatosPersonales
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = ['nombres', 'apellidos', 'fecha_nacimiento', 'ciudad_nacimiento', 
                  'telefono', 'ciudad_residencia', 'titulo', 'anio_obtencion',
                  'experiencia_laboral', 'estado_civil', 'identificacion', 
                  'numero_identificacion', 'sexo', 'genero']
