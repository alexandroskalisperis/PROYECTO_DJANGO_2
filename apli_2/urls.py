from django.urls import path
from .views import pagina_principal, ciencia_y_tecnologia

urlpatterns = [
    path("pagina_principal/", pagina_principal),   
    path("ciencia_y_tecnologia/", ciencia_y_tecnologia),
    
    
    
]