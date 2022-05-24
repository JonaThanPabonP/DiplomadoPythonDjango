from django.contrib import admin
from .models import PlanesDeportivos, Deportista, DeportistaUsage

# Register your models here.
admin.site.register(Deportista)
admin.site.register(PlanesDeportivos)
admin.site.register(DeportistaUsage)