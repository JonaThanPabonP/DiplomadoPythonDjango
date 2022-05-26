from django.views.generic import ListView
from django.shortcuts import render
from .models import Cita_medica, Doctor, Paciente

# Create your views here.

def numero_de_citas(request):
    citas = Cita_medica.objects.all()

    context = {
        "numero_citas": len(citas)
    }
    return render(request, 'numero_citas_medicas.html', context)


def get_doctores_list(request):
    doctores = Doctor.objects.all()

    context = {
        'doctores': doctores
    }
    return render(request, 'doctor_list.html', context)


class PacienteListView(ListView):
    model = Paciente
    context_object_name = 'paciente_list'
    template_name = 'paciente_list.html'