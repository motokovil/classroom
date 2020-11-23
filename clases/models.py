from django.db import models
# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    activa = models.BooleanField(default=True)
    created = models.DateTimeField(auto_created=True, auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre