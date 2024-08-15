from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.

def home(request):
    return render(request, 'index.html')

def create_employed(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_empleado')
        apellido = request.POST.get('apellido_empleado')
        edad = request.POST.get('edad_empleado')
        genero = request.POST.get('genero_empleado')
        email = request.POST.get('email_empleado')
        salario = request.POST.get('salario_empleado')

        emp = Empleado(
            nombre_empleado=nombre,
            apellido_empleado=apellido,
            edad_empleado=edad,
            genero_empleado=genero,
            email_empleado=email,
            salario_empleado=salario
        )
        emp.save()
        return render(request, 'index.html')  # Renderiza el formulario si la solicitud no es POST
    return render(request, 'index.html')
