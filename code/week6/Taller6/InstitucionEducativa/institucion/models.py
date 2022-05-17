from django.db import models

# Create your models here.
class Estudiante(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True)

class Materia(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Evaluacion(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    tematica = models.CharField(max_length=500)
    fecha = models.DateField(null=True)
    estudiante_id = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    materia_id = models.ForeignKey('Materia', on_delete=models.CASCADE)