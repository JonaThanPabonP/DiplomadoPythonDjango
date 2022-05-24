from django.shortcuts import render
from .models import Deportista, DeportistaUsage, PlanesDeportivos

# Create your views here.

def deportista(request):
    deportistas = Deportista.objects.all()

    context = {
        "deportistas": deportistas
    }

    return render(request, 'deportitas_list.html', context=context)

def facturacion(request, id):
    deportista = Deportista.objects.get(uniqueId=id)
    numero_horas = 0
    pago = 0
    plan_del_deportista = ''
    deportista_usages = DeportistaUsage.objects.filter(
        deportista=deportista
    ).all()

    for du in deportista_usages:
        # todo: get the number hour with a method
        numero_horas = numero_horas + (du.hora_salida - du.hora_ingreso).total_seconds()/3600

    planes = PlanesDeportivos.objects.all()

    for plan in planes:
        if numero_horas >= plan.min_horas and numero_horas < plan.max_horas:
            plan_del_deportista = plan.nombre
            pago = numero_horas * plan.valor_facturacion



    context = {
        "nombre": deportista.nombre,
        "horas": numero_horas,
        "plan_del_deportista": plan_del_deportista,
        "pago": pago
    }

    return render(request, 'facturacion.html', context=context)