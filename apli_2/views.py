from django.shortcuts import render
from apli_1.models import Cliente


# Create your views here.
# ============================= PAGINA PRINCIPAL =============================
def pagina_principal(request):
    pestana = "Padre.net - Principal"
    titulo = "Padre.net"
    subtitulo = "Pagina Principal"
    cliente_id = request.session["cliente_id"]
    cliente_nombre = request.session["cliente_nombre"] 
    request.user = cliente_nombre
    
    
    return render(
        request,
        "pagina_principal.html",
        {
            "pestana": pestana,
            "titulo": titulo,
            "subtitulo": subtitulo,
            "cliente_id": cliente_id,
            "cliente_nombre": cliente_nombre,
            "usuario": request.user,
              
        }
    )
# ================================================================================================================
# =========================== CIENCIA Y TECNOLOGIA ===========================

def ciencia_y_tecnologia(request):
    pestana = "Padre.net - Ciencia y Tecnologia"
    titulo = "Padre.net"
    subtitulo = "Ciencia y Tecnologia"
    cliente_nombre = request.session["cliente_nombre"]
    request.user = cliente_nombre

    return render(
        request,
        "ciencia_y_tecnologia.html",
        {
            "pestana": pestana,
            "titulo": titulo,
            "subtitulo": subtitulo,
            "cliente_nombre": cliente_nombre,
        }
    )