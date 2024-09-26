from django.db import models
from django.contrib.auth.models import User  # Importar el modelo de usuario

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)

class DatosPersonales(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    ciudad_nacimiento = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    ciudad_residencia = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    anio_obtencion = models.IntegerField()
    experiencia_laboral = models.BooleanField(default=False)
    estado_civil = models.CharField(max_length=20)
    identificacion = models.CharField(max_length=20, choices=[('cedula', 'Cédula'), ('pasaporte', 'Pasaporte')])
    numero_identificacion = models.CharField(max_length=20)
    sexo = models.CharField(max_length=10, choices=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('otro', 'Otro')])
    genero = models.CharField(max_length=30, choices=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('otro', 'Otro'), ('no_decir', 'Prefiero no decir')])
