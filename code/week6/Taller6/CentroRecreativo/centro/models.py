from django.db import models

# Create your models here.
class Deportista(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class PlanesDeportivos(models.Model):
    uniqueId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    max_horas = models.PositiveIntegerField(null=True)
    min_horas = models.PositiveIntegerField(null=True)
    valor_facturacion = models.PositiveIntegerField(null=True)

    def __str__(self):
        return "{}: {}".format(self.nombre, self.valor_facturacion)

class DeportistaUsage(models.Model):
    deportista = models.ForeignKey("Deportista", on_delete=models.CASCADE)
    hora_ingreso = models.DateTimeField()
    hora_salida = models.DateTimeField()

    def __str__(self):
        return "{}: {} - {}".format(self.deportista, self.hora_ingreso.strftime("%Y-%m-%d %H:%M:%S"), self.hora_salida.strftime("%Y-%m-%d %H:%M:%S"))
