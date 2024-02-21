from django.urls import path
from .views import Mi_tiempo

mi_vista = Mi_tiempo()

urlpatterns = [
    path("constelacion/", mi_vista.constelacion, name="constelacion"),
    
]