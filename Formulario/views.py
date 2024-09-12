from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def formulario(request):
    return render(request, 'formulario.html')
