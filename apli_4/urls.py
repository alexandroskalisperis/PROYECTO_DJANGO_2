from django.urls import path
from .views import Mi_tiempo

mi_vista = Mi_tiempo()

urlpatterns = [
    path("tiempo/", mi_vista.tiempo, name="tiempo"),
    path("direccion/", mi_vista.direccion, name="direccion"),
    path("clima/", mi_vista.clima, name="clima"),
    path("temperatura/", mi_vista.temperatura, name="temperatura"),
    path("humedad/", mi_vista.humedad, name="humedad"),
    path("visibilidad/", mi_vista.visibilidad, name="visibilidad"),
    path("coordenadas/", mi_vista.coordenadas, name="coordenadas"),
    path("viento/", mi_vista.viento, name="viento"),
]