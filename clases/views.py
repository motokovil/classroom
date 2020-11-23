from django.shortcuts import render
from .models import Clase
# Create your views here.

def ViewClase(request):
    clases = Clase.objects.all()
    disponibles = Clase.objects.filter(activa=True)
    noDisponibles = Clase.objects.filter(activa=False)
    return render(request, 'clases/clases.html', {'clases': clases, 'disponibles': disponibles, 'noDisponibles': noDisponibles})

def ViewsClase(request, clase_id):
    clase = Clase.objects.get(id=clase_id)
    estudiante = clase.estudiante.all()
    return render(request, 'clases/clase.html', {'clase': clase, 'estudiante': estudiante})