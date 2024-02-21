from django.shortcuts import render
from django.views import View
from datetime import datetime
from apli_1.models import Cliente, Mensaje, Estado, Estado_2

# Create your views here.

# PROGRAMACION ORIENTADA A OBJETOS==================================
class Mi_vista(View):
    def __init__(self):
        self.titulo_pagina = "Kaligram"
        self.tiempo = datetime.now()
        self.cliente_id = None
        self.cliente_nombre = None
        self.cliente_all = Cliente.objects.all()
        self.mensaje_all = Mensaje.objects.order_by("-fecha_mensaje")
        self.textarea = None
        self.like_1 = None
        self.estado = None
        self.estado_2 = None
        self.guardar_mensaje = None
    # TODAS LAS VISTAS DENTRO DE LA CLASE =====================================
    def kaligram(self,request): 
        self.cliente_id = request.session["cliente_id"]
        self.cliente_nombre = request.session["cliente_nombre"]
        self.mensaje_all = Mensaje.objects.order_by("-fecha_mensaje")
        return render(
            request,
            "kaligram.html",
            {
                "titulo_pagina": self.titulo_pagina,
                "tiempo": self.tiempo,    
                "cliente_id": self.cliente_id,
                "cliente_nombre": self.cliente_nombre,
                "mensajes": self.mensaje_all,
                
            }
        )
    def mensajeria(self, request):
        if request.method == "POST":
            self.textarea = request.POST["textarea"]
            self.cliente_nombre = request.session["cliente_nombre"]
            
            self.guardar_mensaje = Mensaje(
                mensaje_cliente = self.textarea,
                nombre_cliente = Cliente.objects.get(nombre = self.cliente_nombre),
            )
            self.guardar_mensaje.save() 
            self.estado = Estado.objects.create(
                cliente_estado = None,
                mensaje_foraneo = Mensaje.objects.get(mensaje_cliente = self.textarea),
                estado = None
            )
            self.estado.save()
            self.estado_2 = Estado_2.objects.create(
                cliente_estado2 = None,
                mensaje_foraneo_2 = Mensaje.objects.get(mensaje_cliente = self.textarea),
                estado2 = None
            )
            self.estado_2.save()
            
            
            self.mensaje_all = Mensaje.objects.order_by("-fecha_mensaje")
            return render(
                request,
                "kaligram.html", 
                {
                    "titulo_pagina": self.titulo_pagina,
                    "tiempo": self.tiempo, 
                    "cliente_id": self.cliente_id, 
                    "mensajes": self.mensaje_all,
                    "textarea": self.textarea,
                    "cliente_nombre": self.cliente_nombre,
                    "guardar_mensaje": self.guardar_mensaje,
                }
            ) 
        
    def like(self, request):
        self.textarea_2 = request.POST["textarea_2"]
        self.mensaje_id = request.POST["mensaje_id"]
        self.mensaje = Mensaje.objects.get(id = self.mensaje_id)
        self.estado = Estado.objects.get(mensaje_foraneo = self.mensaje_id)
        self.estado_2 = Estado_2.objects.get(mensaje_foraneo_2 = self.mensaje_id)

        if not Estado.objects.filter(cliente_estado=self.cliente_nombre,mensaje_foraneo=self.mensaje,estado=True) or Estado.objects.filter(cliente_estado=self.cliente_nombre,mensaje_foraneo=self.mensaje,estado=False):
            self.estado.estado = True
            self.estado.cliente_estado = self.cliente_nombre
            self.estado.save()
            if not Estado_2.objects.filter(cliente_estado2=self.cliente_nombre,mensaje_foraneo_2=self.mensaje,estado2=True):
                self.estado_2.estado2 = False
                self.estado_2.cliente_estado2 = self.cliente_nombre
                self.estado_2.save()
            else:
                if Estado_2.objects.filter(cliente_estado2=self.cliente_nombre,mensaje_foraneo_2=self.mensaje,estado2=True):
                    self.estado_2.estado2 = False
                    self.estado_2.cliente_estado2 = self.cliente_nombre
                    self.estado_2.save()
                    self.mensaje.perro2_dislike -= 1
                    self.mensaje.save()
            self.mensaje.perro1_like += 1
            self.mensaje.save()
            
            
        elif Estado.objects.filter(cliente_estado=self.cliente_nombre,mensaje_foraneo=self.mensaje,estado=True):
            self.estado.estado = False
            self.estado.cliente_estado = self.cliente_nombre
            self.estado.save()

            self.mensaje.perro1_like -= 1
            self.mensaje.save()
            
                

        self.mensaje_all = Mensaje.objects.order_by("-fecha_mensaje")
        return render(
            request,
            "kaligram.html",
            {
                "titulo_pagina": self.titulo_pagina,
                "tiempo": self.tiempo, 
                "cliente_id": self.cliente_id, 
                "mensajes": self.mensaje_all,
                "textarea": self.textarea,
                "cliente_nombre": self.cliente_nombre,
                "guardar_mensaje": self.guardar_mensaje,
                
            }
        )
    
    def dislike(self, request):
        self.textarea_2 = request.POST["textarea_2"]
        self.mensaje_id = request.POST["mensaje_id"]
        self.mensaje = Mensaje.objects.get(id = self.mensaje_id)
        self.estado_2 = Estado_2.objects.get(mensaje_foraneo_2 = self.mensaje_id)
        self.estado = Estado.objects.get(mensaje_foraneo=self.mensaje_id)

        if not Estado_2.objects.filter(cliente_estado2=self.cliente_nombre,mensaje_foraneo_2=self.mensaje,estado2=True) or Estado_2.objects.filter(cliente_estado2=self.cliente_nombre,mensaje_foraneo_2=self.mensaje,estado2=False):
            self.estado_2.cliente_estado2 = self.cliente_nombre
            self.estado_2.estado2 = True
            self.estado_2.save()
            self.mensaje.perro2_dislike += 1
            self.mensaje.save()
            if Estado.objects.filter(cliente_estado=self.cliente_nombre,mensaje_foraneo=self.mensaje,estado=True):
                self.estado.estado = False
                self.estado.cliente_estado = self.cliente_nombre
                self.estado.save()
                self.mensaje.perro1_like -= 1
                self.mensaje.save()
            else:
                if not Estado.objects.filter(cliente_estado=self.cliente_nombre,mensaje_foraneo=self.mensaje,estado=True):
                    pass
        else:
            if Estado_2.objects.filter(cliente_estado2=self.cliente_nombre,mensaje_foraneo_2=self.mensaje,estado2=True):
                self.estado_2.cliente_estado2 = self.cliente_nombre
                self.estado_2.estado2 = False
                self.estado_2.save()
                self.mensaje.perro2_dislike -= 1
                self.mensaje.save()  
       
        self.mensaje_all = Mensaje.objects.order_by("-fecha_mensaje")
        return render(
            request,
            "kaligram.html",
            {
                "titulo_pagina": self.titulo_pagina,
                "tiempo": self.tiempo, 
                "cliente_id": self.cliente_id, 
                "mensajes": self.mensaje_all,
                "textarea": self.textarea,
                "cliente_nombre": self.cliente_nombre,
                "guardar_mensaje": self.guardar_mensaje,
                
            }
        )    



    
    def boring(self, request):
        self.textarea_2 = request.POST["textarea_2"]
        self.mensaje_id = request.POST["mensaje_id"]
        self.mensaje = Mensaje.objects.get(id = self.mensaje_id)
        
        self.mensaje.perro3_aburrido += 1
        self.mensaje.save()
                

        self.mensaje_all = Mensaje.objects.order_by("-fecha_mensaje")
        return render(
            request,
            "kaligram.html",
            {
                "titulo_pagina": self.titulo_pagina,
                "tiempo": self.tiempo, 
                "cliente_id": self.cliente_id, 
                "mensajes": self.mensaje_all,
                "textarea": self.textarea,
                "cliente_nombre": self.cliente_nombre,
                "guardar_mensaje": self.guardar_mensaje,
                
            }
        )


   