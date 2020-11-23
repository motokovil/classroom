from django.shortcuts import render
from .models import Estudiante
from clases.models import Clase
# Create your views here.
def ViewEstudiante(request):
    estudiantes = Estudiante.objects.all()
    clases = Clase.objects.all()
    disponibles = Clase.objects.filter(activa=True)
    noDisponibles = Clase.objects.filter(activa=False)
    return render(request, 'estudiantes/estudiantes.html', {'estudiantes': estudiantes, 'clases': clases, 'disponibles':disponibles, 'noDisponibles': noDisponibles})

def ViewsEstudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    clases = estudiante.clase.all()
    return render(request, 'estudiantes/estudiante.html', {'estudiante': estudiante, 'clases': clases})
