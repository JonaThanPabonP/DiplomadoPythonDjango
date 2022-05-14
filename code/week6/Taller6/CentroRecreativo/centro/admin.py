from django.contrib import admin
from .models import Deporte, Deportista, Inscripcion

# Register your models here.
admin.site.register(Deportista)
admin.site.register(Deporte)
admin.site.register(Inscripcion)