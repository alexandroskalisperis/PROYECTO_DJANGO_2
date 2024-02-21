from django.urls import path
from .views import login, registrate, chequear_registro, usuario, chequear_usuario

urlpatterns = [
    path("", login),
    path("registrate/", registrate),
    path("chequear_registro/", chequear_registro),
    path("usuario/", usuario),
    path("chequear_usuario/", chequear_usuario),
    
   
    
]
# 