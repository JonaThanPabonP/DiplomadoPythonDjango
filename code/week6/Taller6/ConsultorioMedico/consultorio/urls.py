from django.contrib import admin
from django.urls import path
from consultorio import views

app_name = 'consultorio'
urlpatterns = [

    path('', views.home, name='home'),
    path('pacientes', views.pacientes, name='pacientes'),
    path('medicos', views.medicos, name='medicos'),
    path('citas', views.citas, name='citas'),
    
]