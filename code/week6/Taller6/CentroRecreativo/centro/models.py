from django.db import models

# Create your models here.
class Deportista(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(default="")


class Deporte(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    

class Inscripcion(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    horas_practicar = models.PositiveIntegerField
    sitio_entrenamiento = models.CharField(max_length=500)
    deportista_id = models.ForeignKey('Deportista', on_delete=models.CASCADE)
    deporte_id = models.ForeignKey('Deporte', on_delete=models.CASCADE)