from django.shortcuts import render
from .models import Cita_medica, Doctor, Paciente


# Create your views here.

def home(request):
    return render(request, 'home.html')

def pacientes(request):
    p = Paciente.objects.all()
    context = {
        "lista_pacientes": p,
        "numero_pacientes": len(p),
    }
    return render(request, 'pacientes.html', context)

def citas(request):
    c_m = Cita_medica.objects.all()

    context = {
        "lista_citas": c_m,
        "numero_citas": len(c_m),
    }
    return render(request, 'citas.html', context)

def medicos(request):
    d = Doctor.objects.all()

    context = {
        "lista_medicos": d,
        "numero_medicos": len(d),
    }
    return render(request, 'medicos.html', context)