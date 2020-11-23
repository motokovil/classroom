from django.db import models
from clases.models import Clase

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    edad = models.IntegerField(null=True)
    clase = models.ManyToManyField(Clase, related_name='estudiante')
    created = models.DateTimeField(auto_created=True, auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.nombre