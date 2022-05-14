from django.contrib import admin
from .models import Estudiante, Materia, Evaluacion

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Evaluacion)