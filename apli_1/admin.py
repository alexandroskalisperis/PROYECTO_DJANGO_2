from django.contrib import admin
from .models import Cliente, Mensaje, Respuesta, Estado, Estado_2, Estado_3
# Register your models here.

class Cliente_admin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "telefono", "email", "clave","foto")
    search_fields = ("nombre", "apellido", "telefono", "email", "clave","foto")
    list_filter=("nombre","clave",)
admin.site.register(Cliente, Cliente_admin)

class Mensaje_admin(admin.ModelAdmin):
    list_display = ("mensaje_cliente", "fecha_mensaje", "nombre_cliente","perro1_like","perro2_dislike","perro3_aburrido")
    search_fields = ("mensaje_cliente", "fecha_mensaje", "nombre_cliente","perro1_like","perro2_dislike","perro3_aburrido")
    list_filter = ("mensaje_cliente", "nombre_cliente", "perro1_like","perro2_dislike","perro3_aburrido",)
admin.site.register(Mensaje, Mensaje_admin)

class Respuesta_admin(admin.ModelAdmin):
    list_display= ("autor","cliente","mensaje_respuesta","fecha_respuesta","like","dislike","aburrido")
    search_fields= ("autor","cliente","mensaje_respuesta","fecha_respuesta","like","dislike","aburrido")
    list_filter= ("autor","cliente","mensaje_respuesta","fecha_respuesta","like","dislike","aburrido",)
admin.site.register(Respuesta, Respuesta_admin)

class Estado_admin(admin.ModelAdmin):
    list_display = ("cliente_estado", "mensaje_foraneo", "estado")
    search_fields = ("cliente_estado", "mensaje_foraneo", "estado")
    list_filter = ("cliente_estado", "mensaje_foraneo", "estado",)
admin.site.register(Estado, Estado_admin)

class Estado_2_admin(admin.ModelAdmin):
    list_display = ("cliente_estado2", "mensaje_foraneo_2", "estado2")
    search_fields = ("cliente_estado2", "mensaje_foraneo_2", "estado2")
    list_filter = ("cliente_estado2", "mensaje_foraneo_2", "estado2",)
admin.site.register(Estado_2, Estado_2_admin)

class Estado_3_admin(admin.ModelAdmin):
    list_display = ("cliente_estado3", "mensaje_foraneo_3", "estado3")
    search_fields = ("cliente_estado3", "mensaje_foraneo_3", "estado3")
    list_filter = ("cliente_estado3", "mensaje_foraneo_3", "estado3",)
admin.site.register(Estado_3, Estado_3_admin)