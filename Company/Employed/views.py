from django.shortcuts import get_object_or_404, render, redirect
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

def table(request):
    empleados = Empleado.objects.all()  # Obteniendo todos los empleados
    return render(request, 'datatable.html', {'empleados': empleados})

def delete_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    return redirect('datatable') 

def edit_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    
    if request.method == 'POST':
        empleado.nombre_empleado = request.POST.get('nombre_empleado')
        empleado.apellido_empleado = request.POST.get('apellido_empleado')
        empleado.edad_empleado = request.POST.get('edad_empleado')
        empleado.genero_empleado = request.POST.get('genero_empleado')
        empleado.email_empleado = request.POST.get('email_empleado')
        empleado.salario_empleado = request.POST.get('salario_empleado')
        empleado.save()
        return redirect('datatable') 
    
    return render(request, 'form.html', {'empleado': empleado})