from django.urls import path
from .views import Mi_vista

mi_vista = Mi_vista()

urlpatterns = [
    path("kaligram/", mi_vista.kaligram, name="kaligram"),
    path("mensajeria/", mi_vista.mensajeria, name="mensajeria"), 
    path("like/", mi_vista.like, name="like"),
    path("dislike/", mi_vista.dislike, name="dislike"),
    path("boring/", mi_vista.boring, name="boring"),
    
    
    
    
    
    
    
    
    
]