from django.shortcuts import render
from .models import Cita_medica

# Create your views here.

def numero_de_citas(request):
    citas = Cita_medica.objects.all()

    context = {
        "numero_citas": len(citas)
    }
    return render(request, 'numero_citas_medicas.html', context)