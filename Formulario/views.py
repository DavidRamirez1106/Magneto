from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm, DatosPersonalesForm
from .models import Register, DatosPersonales
from django.contrib.auth.hashers import make_password

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Usar set_password
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form.add_error(None, "Error al registrar el usuario.")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def formulario(request):
    if request.method == 'POST':
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            datos = form.save(commit=False)
            datos.usuario = request.user  # Asocia los datos personales con el usuario autenticado
            datos.save()
            return redirect('home')  # Redirige a 'home' después de guardar
    else:
        form = DatosPersonalesForm()
    return render(request, 'formulario.html', {'form': form})

def logout_view(request):
    try:
        del request.session['usuario_autenticado']
        del request.session['user_id']
        del request.session['user_src']
    except KeyError:
        pass
    return redirect('login')
