from django.contrib import admin
from django.urls import path
from Formulario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('formulario/', views.formulario, name='formulario'),
]
