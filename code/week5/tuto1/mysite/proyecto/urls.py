
from re import template
from django.contrib import admin
from django.urls import path
from proyecto import views
from django.views.generic import TemplateView



urlpatterns = [

    path('', views.index, name="index"),
    path('colombia/', TemplateView.as_view(template_name = "colombia.html"), name="colombia"),
    path('mundo/', TemplateView.as_view(template_name = "mundo.html"), name="mundo"),
    path('propuesta/', TemplateView.as_view(template_name = "propuesta.html"), name="propuesta"),
]
