from django.db import models

# Create your models here.

class Paciente(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} -- ({self.fecha_de_nacimiento})"

    def getName(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Doctor(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
    def getName(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Cita_medica(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=500)
    fecha = models.DateField(null=True)
    paciente_id = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.fecha} - {self.paciente_id.getName()} - {self.doctor_id.getName()}"
