from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Huertas_Persona

# Create your views here.
def index(request):
    return render(request, 'index.html')


def agregar_persona(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        sexo = request.POST['sexo']
        persona = Huertas_Persona(nombre=nombre, apellidos=apellidos, sexo=sexo)
        persona.save()
        messages.success(request, 'La persona ha sido agregada con éxito.')
        return redirect('personas')
    return render(request, 'agregar_persona.html')

def editar_persona(request, id):
    persona = get_object_or_404(Huertas_Persona, id=id)
    if request.method == 'POST':
        persona.nombre = request.POST['nombre']
        persona.apellidos = request.POST['apellidos']
        persona.sexo = request.POST['sexo']
        persona.save()
        messages.success(request, 'La persona ha sido actualizada con éxito.')
        return redirect('personas')
    return render(request, 'editar_persona.html', {'persona': persona})

def personas(request):
    personas = Huertas_Persona.objects.all()
    return render(request, 'personas.html', {'personas': personas})

def eliminar_persona(request, id):
    persona = get_object_or_404(Huertas_PersonaPersona, id=id)
    persona.delete()
    messages.success(request, 'La persona ha sido eliminada con éxito.')
    return redirect('personas')
