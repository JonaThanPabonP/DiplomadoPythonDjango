from django.urls import path
from centro import views
from django.views.generic import TemplateView

app_name = "centro"

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('eventos', TemplateView.as_view(template_name="eventos.html"), name="eventos"),
    path('deportistas', views.deportista, name="deportistas"),
    path('facturacion/<int:id>', views.facturacion, name="facturacion"),
]