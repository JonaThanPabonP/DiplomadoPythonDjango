from django.db import models
from datetime import datetime

# Create your models here.

class Paciente(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()


class Doctor(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    

class Cita_medica(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=500)
    fecha = models.DateField(default=datetime.now)
    paciente_id = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    diagnostico = models.CharField(max_length=1000, null=True)