
from django import forms as forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import Cliente_form, Usuario_form
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
        foto_cliente = request.POST["foto_cliente"]
        
        
    filtro_cliente = Cliente.objects.filter(
        nombre = nombre_cliente,
        apellido = apellido_cliente,
        telefono = telefono_cliente,
        email = email_cliente,
        clave = clave_cliente,
        
        
    )
    if filtro_cliente:
        pestana = "Padre.net"

        # REALICE UNA MODIFICACION EN EL CLIENTE POR USER
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
                "filtro_cliente": filtro_cliente,
                "cliente_id": cliente_id,
                "cliente_nombre": cliente_nombre,
             
                
            }
        )
        # CREAMOS AL CLIENTE Y AL USUARIO A LA VEZ
    else:   
        pestana = "Padre.net"
        crear_cliente = Cliente.objects.create(
            nombre = nombre_cliente,
            apellido = apellido_cliente,
            telefono = telefono_cliente,
            email = email_cliente,
            clave = clave_cliente,
            foto = foto_cliente,
           
            
        )
        # user = User.objects.create_user(
        #     username=nombre_cliente, 
        #     password=clave_cliente, 
        #     email=email_cliente, 
        #     first_name=nombre_cliente, 
        #     last_name=apellido_cliente
        #     )
        # user.is_staff = True
        # user.save()
        # user = auth.authenticate(username=nombre_cliente, password=clave_cliente)
        # if user is not None and user.is_active:
            
        #     mensaje_user = "usted existe"
        # else:
        #     mensaje_user = "usted no existe"
        
        
        cliente = Cliente.objects.get(nombre__exact = request.POST["nombre_cliente"])
        if clave_cliente == cliente.clave:
            request.session["cliente_id"] = cliente.id
            request.session["cliente_nombre"] = cliente.nombre
           
            
        cliente_id = request.session["cliente_id"]

        
        
        return render(
            request,
            "crear_cliente.html",
            {
                "filtro_cliente": filtro_cliente,
                "pestana": pestana,
                "crear_cliente": crear_cliente,
                # "user": user,
                # "mensaje_user": mensaje_user,
                
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

   

    
