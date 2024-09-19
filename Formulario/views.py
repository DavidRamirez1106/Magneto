from django.shortcuts import render, redirect
from . models import Register
from . forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login





from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User  # Usar el modelo de usuario de Django (si estás usando `Register`, verifica que el modelo esté correctamente configurado)

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Obtenemos los datos del formulario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Intentar autenticar al usuario
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Usuario autenticado correctamente, iniciar sesión y redirigir a home
                login(request, user)  # Autenticar sesión en Django
                return redirect('home')
            else:
                # Si no se pudo autenticar, agregar un error al formulario
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method=='POST':

        #Obtención de los datos en el formulario
        form= RegisterForm(request.POST)
        if form.is_valid():
            print("enviados")
            #Almacenamiento en la base de datos  
            form.save()
            #Permiso para ingresar a home (login automático)
            request.session['usuario_autenticado'] = True 
            origin_country = form.cleaned_data.get('origin_country')
            request.session['user_src']= origin_country
            return redirect('home')
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error en {field}: {error}")
            form.add_error(None, "Nombre de usuario ocupado")
    else:
        form=RegisterForm()
    return render(request, 'register.html', {'form':form})

def home(request):
    return render(request, 'home.html')

def formulario(request):
    return render(request, 'formulario.html')

def logout_view(request):
    # Eliminar las variables de sesión relacionadas con la autenticación
    try:
        del request.session['usuario_autenticado']
        del request.session['user_id']
        del request.session['user_src']
    except KeyError:
        pass

    # Redirigir al usuario a la página de inicio de sesión o cualquier otra página
    return redirect('login')