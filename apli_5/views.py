from django.shortcuts import render
from django.views import View



# Create your views here.


class Mi_tiempo(View):
    def __init__(self):
        self.titulo = "constelacion"

    
    def constelacion(self, request):
        return render(
            request,
            "constelacion.html",
            {
                "titulo": self.titulo,
            }
        )
