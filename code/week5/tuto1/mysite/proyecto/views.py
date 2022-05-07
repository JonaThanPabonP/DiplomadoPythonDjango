from django.shortcuts import render
from django.http import HttpResponse

from .models import Player, Game


# Create your views here.
def players(request):
    jugadores = Player.objects.all()
    msg = "Lista de jugadores"

    for jugador in jugadores:
        msg += "<br> {} >> {}".format(jugador.name, jugador.age)

    return HttpResponse(msg)

def games(request):
    partidos = Game.objects.all()
    msg = "Lista de partidos"

    for partido in partidos:
        msg += "<br> {} >> {}".format(partido.date, partido.location)

    return HttpResponse(msg)