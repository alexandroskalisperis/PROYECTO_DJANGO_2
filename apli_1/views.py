
from django import forms as forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import  Usuario_form, Cliente_form
from .models import Cliente, Mensaje

# Create your views here.

def login(request):
    pestana = "Padre.net"
    titulo = "Padre.net"
    subtitulo = "login"
   
    return render(
        request,
        "login.html",
        {
            "pestana": pestana,
            "titulo": titulo,
            "subtitulo": subtitulo,
            
        }
    )
# =============================== REGISTRATE ======================================
def registrate(request):
    pestana = "Padre.net"
    cliente_form = Cliente_form
    
    return render(
        request,
        "registrate.html",
        {
            "pestana": pestana,
            "cliente_form": cliente_form,
             
        }
    )

def chequear_registro(request):
    if request.method == "POST":
        nombre_cliente = request.POST["nombre_cliente"]
        apellido_cliente = request.POST["apellido_cliente"]
        telefono_cliente = request.POST["telefono_cliente"]
        email_cliente = request.POST["email_cliente"]
        clave_cliente = request.POST["clave_cliente"]
        imagen_cliente = request.FILES.get("imagen_cliente")
    
    if Cliente.objects.filter(nombre=nombre_cliente,apellido=apellido_cliente,telefono=telefono_cliente,email=email_cliente,clave=clave_cliente):
        pestana = "Padre.net"
        cliente = Cliente.objects.get(nombre__exact = request.POST["nombre_cliente"])
        if clave_cliente == cliente.clave:
            request.session["cliente_id"] = cliente.id
            request.session["cliente_nombre"] = cliente.nombre
            
        cliente_id = request.session["cliente_id"]
        cliente_nombre = request.session["cliente_nombre"]
        mensaje_error = """sugerencia:
        _por lo general la repeticion del nombre
        con otros ya existentes, ocaciona este tipo 
        de problemas.
        _modifique su clave."""
        
        return render(
            request,
            "esta_registrado.html",
            {                
                "pestana": pestana,
                "cliente_id": cliente_id,
                "cliente_nombre": cliente_nombre,
                "mensaje_error": mensaje_error,
            }
        )  
    elif Cliente.objects.filter(nombre=nombre_cliente,apellido=apellido_cliente,clave=clave_cliente):
        pestana = "Padre.net"
        cliente = Cliente.objects.get(nombre__exact = request.POST["nombre_cliente"])
        if clave_cliente == cliente.clave:
            request.session["cliente_id"] = cliente.id
            request.session["cliente_nombre"] = cliente.nombre
            
        cliente_id = request.session["cliente_id"]
        cliente_nombre = request.session["cliente_nombre"]
        
        return render(
            request,
            "esta_registrado.html",
            {                
                "pestana": pestana,
                "cliente_id": cliente_id,
                "cliente_nombre": cliente_nombre,
            }
        ) 
    elif Cliente.objects.filter(nombre=nombre_cliente,clave=clave_cliente):
        pestana = "Padre.net"
        cliente = Cliente.objects.get(nombre__exact = request.POST["nombre_cliente"])
        if clave_cliente == cliente.clave:
            request.session["cliente_id"] = cliente.id
            request.session["cliente_nombre"] = cliente.nombre
            
        cliente_id = request.session["cliente_id"]
        cliente_nombre = request.session["cliente_nombre"]
        
        return render(
            request,
            "esta_registrado.html",
            {                
                "pestana": pestana,
                "cliente_id": cliente_id,
                "cliente_nombre": cliente_nombre,
            }
        ) 
    elif Cliente.objects.filter(apellido=apellido_cliente,clave=clave_cliente):
        pestana = "Padre.net"
        return render(
            request,
            "esta_registrado.html",
            {                
                "pestana": pestana,
                
            }
        ) 
    elif Cliente.objects.filter(clave=clave_cliente):
        pestana = "Padre.net"
        return render(
            request,
            "esta_registrado.html",
            {                
                "pestana": pestana,
            }
        ) 
    elif Cliente.objects.filter(nombre=nombre_cliente,apellido=apellido_cliente):
        pestana = "Padre.net"
        return render(
            request,
            "esta_registrado.html",
            {                
                "pestana": pestana,
            }
        )
    elif Cliente.objects.filter(nombre=nombre_cliente):
        pestana = "Padre.net"
        return render(
            request,
            "esta_registrado.html",
            {                
                "pestana": pestana,
            }
        )
    
    else:   
        pestana = "Padre.net"
        crear_cliente = Cliente.objects.create(
            nombre = nombre_cliente,
            apellido = apellido_cliente,
            telefono = telefono_cliente,
            email = email_cliente,
            clave = clave_cliente,
            imagen = imagen_cliente,
        )
        cliente = Cliente.objects.get(nombre__exact = request.POST["nombre_cliente"])
        if clave_cliente == cliente.clave:
            request.session["cliente_id"] = cliente.id
            request.session["cliente_nombre"] = cliente.nombre
        cliente_id = request.session["cliente_id"]
        return render(
            request,
            "crear_cliente.html",
            {
                "pestana": pestana,
                "crear_cliente": crear_cliente,
            }
        )
# ==================================== USUARIO ======================================
def usuario(request):
    pestana = "Padre.net"
    usuario_form = Usuario_form
    return render(
        request,
        "usuario.html",
        {
            "pestana": pestana,
            "usuario_form": usuario_form,
        }
    )

def chequear_usuario(request):
    ultimo = Mensaje.objects.order_by("-fecha_mensaje")
    if request.method == "POST":
        nombre_usuario = request.POST["nombre_usuario"]
        clave_usuario = request.POST["clave_usuario"]
    
    filtro_usuario = Cliente.objects.filter(
        nombre = nombre_usuario,
        clave = clave_usuario,
    )
    
    if filtro_usuario:
        pestana = "Padre.net"
        titulo = "Padre.net"
        subtitulo = "Pagina Principal"
       
        cliente = Cliente.objects.get(nombre__exact = request.POST["nombre_usuario"])
        if clave_usuario == cliente.clave:
            request.session["cliente_id"] = cliente.id
            request.session["cliente_nombre"] = cliente.nombre
            
            
        cliente_id = request.session["cliente_id"]
        cliente_nombre = request.session["cliente_nombre"]
           
        
        return render(
            request,
            "pagina_principal.html",
            {
                "filtro_usuario": filtro_usuario,
                "pestana": pestana,
                "titulo": titulo,
                "subtitulo": subtitulo,
                "ultimo": ultimo,
                "cliente_id": cliente_id,
                "cliente_nombre": cliente_nombre,
                
            }
        )
    else: 
        pestana = "Padre.net"
        cliente_form = Cliente_form
        return render(
            request,
            "registrate.html",
            {
                "pestana": pestana,
                "cliente_form": cliente_form,
            }
        )

   

    
