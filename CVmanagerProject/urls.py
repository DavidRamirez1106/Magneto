from django.contrib import admin
from django.urls import path
from Formulario import views as Formulario_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Formulario_views.custom_login, name='login'),
    path('home/', Formulario_views.home, name='home'),  
    path('register/', Formulario_views.register, name='register'),
    path('formulario/', Formulario_views.formulario, name='formulario'),  # Ruta para el formulario
    path('logout/', Formulario_views.logout_view, name='logout'),
]
