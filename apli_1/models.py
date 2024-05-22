
from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    clave = models.CharField(max_length=50)
    imagen = models.ImageField(null=True,upload_to="imagenes/")
    
    
    def __str__(self):
        return  (
            self.nombre
        )

class Mensaje(models.Model):
    mensaje_cliente = models.TextField(null=True)
    fecha_mensaje = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    nombre_cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    perro1_like = models.IntegerField(default=0, null=True)
    perro2_dislike = models.IntegerField(default=0, null=True)
    perro3_aburrido = models.IntegerField(default=0, null=True)
    imagen_cliente_1 = models.CharField(max_length=50)
    

    def __str__(self):
        return "%s %s %s" %(
            self.mensaje_cliente, " ", self.nombre_cliente,
        )

class Respuesta(models.Model):
    autor = models.CharField(max_length=50)
    cliente = models.CharField(max_length=50)
    mensaje_respuesta = models.TextField(null=True)
    fecha_respuesta = models.DateTimeField(auto_now_add=False, auto_now=True, null=True) 
    like = models.IntegerField(default=0, null=True)
    dislike = models.IntegerField(default=0, null=True)
    aburrido = models.IntegerField(default=0, null=True)

    def __str__(self):
        return "%s %s %s" %(
            self.autor, " ", self.mensaje_respuesta,
        )
    
class Estado(models.Model):
    cliente_estado = models.CharField(max_length=50, null=True)
    mensaje_foraneo = models.ForeignKey("Mensaje", on_delete=models.CASCADE)
    estado = models.BooleanField(default=False, null=True)

    def __str__(self):
        return "%s %s %s %s %s" %(
            self.cliente_estado," ", self.mensaje_foraneo," ", self.estado,
        )
    

class Estado_2(models.Model):
    cliente_estado2 = models.CharField(max_length=50, null=True)
    mensaje_foraneo_2 = models.ForeignKey("Mensaje", on_delete=models.CASCADE)
    estado2 = models.BooleanField(default=False, null=True)

    def __str__(self):
        return "%s %s %s %s %s" %(
            self.cliente_estado2," ", self.mensaje_foraneo_2," ", self.estado2,
        )
    
class Estado_3(models.Model):
    cliente_estado3 = models.CharField(max_length=50, null=True)
    mensaje_foraneo_3 = models.ForeignKey("Mensaje", on_delete=models.CASCADE)
    estado3 = models.BooleanField(default=False, null=True)

    def __str__(self):
        return "%s %s %s %s %s" %(
            self.cliente_estado3," ", self.mensaje_foraneo_3," ", self.estado3,
        )