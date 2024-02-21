"""================== DJANGO PASO A PASO =====================

1) Crear una carpeta en el escritorio
2) Desde la terminal de VS pegamos la ruta a la carpeta:
                _ django-admin startproject proyecto1
                _ python manage.py runserver
3) Dentro de la carpeta proyecto1:
                _ python manage.py startapp aplicacion1
                
4) Dentro de settings.py agragamos nuestra nueva 
        aplicacion:

                _ INSTALLED_APPS = [
                        ....
                        ....
                        'aplicacion1',
                ]

5) Dentro de settings configuramos el resto, 
        como la base de datos, 
        la conexion a internet, 
        los static files lo dejamos como esta, 
        y los archivos media.

        _ Abrimos POSTGRE SQL y creamos la base de datos con el mismo nombre 
          que le configuramos en el setting.
        _ Creamos los modelos en el archivo models.py
        _ desde consola makemigrations/ migrate.  
==================================================================================================

6) Creamos un superusuario:
                _ python manage.py createsuperuser
                
7) Ejecutamos el servidor:
                _ python manage.py runserver

8) Nuestra direccion va a estar en: (ingresando nuestra clave)

                _   http://127.0.0.1:8000/admin/

====================================================================

"""

"""CREANDO LA BASE DE DATOS POSTGRE-SQL

_ django-admin startproject proyecto1
_ cd proyecto1
_ python manage.py startapp app1

_ ABRIMOS POSTGRESQL Y CREAMOS UNA BASE DE DATOS 

_ DESDE SETTINGS CONECTAMOS LA BASE DE DATOS INGRESANDO LOS DATOS DE LA MISMA:

        DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': "BBDD1",
                'USER':'postgres',
                'PASSWORD':'DIOSES1979',
                'HOST':'127.0.0.1',
                'DATABASE_PORT':'5432',
        }
        }

_ DESDE MODELS CREAMOS LOS MODELOS 

_ DESDE CONSOLA:
        _ python manage.py makemigrations
        _ python manage.py migrate

_ DESDE POSTGRESQL REALIZAMOS UN REFRESH Y VEMOS QUE SE CREARON LAS TABLAS"""

"""============================================================================================= """

"""PARA INGRESAR DATOS DENTRO DE LA BASE DE DATOS

_ DESDE CONSOLA (TERMINAL):
        _ python manage.py shell
        _ from app1.models import cliente
        
        _ cliente1= cliente.objects.create(nombre="ale", direccion="bursaco", email="ale@yahoo.com.ar")

_ DESDE POSTGRESQL HACEMOS REFRESH
 NOS DIRIGIMOS A LAS TABLAS Y PULSAMOS BOTON DERECHO 
  VIEW/EDIT DATA    ALL ROWS 
 Y VEMOS COMO NOS AGREGO LA INFORMACION.   """

"""=============================================================================================== """

"""PARA SALIR DEL SHELL PERO MANTENERME CONECTADO A LA BASE DE DATOS:
        _ exit()
        
   PARA CERRAR LA CONEXION DE NUESTRO PROYECTO:
        _ close() """

"""=================================================================================================== """

"""PARA CAMBIAR ALGUN DATOS YA EXISTENTE DENTRO DE BBDD:
_ art1.nombre="silla"
_ art1.save()

_ art1.precio= 45
_ art1.save()

        directamente seleccionamos la variable que contiene el nombre punto el campo 
        que queremos cambiar igual y el cambio y enter, luego el nombre otra vez de la 
        variable y save.
        luego desde POSTGRE actualizamos con F5 O REFRESH. """

"""======================================================================================================= """

"""PANEL DE ADMINISTRACION DE DJANGO:

_ DESDE LA TERMINAL
        _ python manage.py createsuperuser (completo todos los campos)

_ DESDE LA WEB
        _ localhost:8000/admin/ 
        _ introducimos el usuario y clave
============================================================================================================ 
                                        ADMIN.PY

_ DESDE DJANGO (ADMIN.PY):
        _ LIST_DISPLAY= contiene los nombres de los campos de consulta que se veran en el panel
        _ SEARCH_FIELDS= nos abre un ENTRY DE BUSQUEDA y los parametros incluidos son los motores de busqueda.
        _ LIST_FILTER= crea un campo de filtrado segun las caracteristicas de los parametros.
        _ ADMIN.SITE.REGISTER= de esta forma se registra y se conecta con el ADMINISTRADOR, el primer parametro
          debe ser la CLASE PROVENIENTE DE MODELS.PY y el segundo es la CLASE CREADA EN ADMIN.PY 





                class cliente_admin(admin.ModelAdmin):
                        list_display=("nombre","direccion","telefono","email")
                        search_fields=("nombre","direccion", "telefono", "email") 
                        list_filter=("nombre",)
                admin.site.register(cliente, cliente_admin) 

_ CON SOLO GUARDAR LOS CAMBIOS YA SE CARGA EN EL PANEL DE ADMINISTRACION.
"""
"""=========================================================================================================================="""
"""========================= API FORMS CREACION Y VALIDACION DE FORMULARIOS =================================================

_ En el mismo directorio que tenemos el archivo views.py 
  creamos un archivo llamado FORMS.PY
_ DESDE FORMS.PY :
        _ importamos desde django la propiedad FORMS:
                _ FROM DJANGO IMPORT FORMS

        _ creamos una clase con los campos que creara django en el formulario:        
                class formulario_contacto(forms.Form):
                        asunto=forms.CharField()
                        email=forms.EmailField()
                        mensaje=forms.CharField() 
        
===============================================================================================================
===============================================================================================================

_ CONFIGURAMOS LA URLS GENERAL:
        _ incorporamos el include 
        _ creamos una nueva URLS.PY en la carpeta de la APLICACION.
        
_ CREAMOS NUESTRA PRIMERA VISTA EN LA APP
        _ esta vista sera creada con:

        def padre(request):
                return render(
                        request,
                        "padre.html",
                )
_ CREAMOS UNA CARPETA TEMPLATE:
        _ dentro creamos un archivo padre.html el cual fue incluido en la 
        vista (esta seria su parte visible)

_ EN LA URLS.PY DE LA APP:
        _ incluimos la nueva vista.

        from django.urls import path
        from apli_1.views import padre

        urlpatterns = [
        path('padre/', padre ),
        ]  
========================================================================================================
=================================== STATIC =============================================================

_ EN LA CARPETA DE LA APP CREAMOS UNA SUB-CARPETA STATIC:
        _ la configuracion debe quedar asi:

        APLI_1/STATIC/APLI_1/ESTILOS.CSS

        _ son tres carpetas una dentro de la otra
          y por ultimo el archivo estilos.css y estilos.js

        _ (recordar que en el setting la configuracion del STATIC 
           debe quedar igual sin modificaciones)

_ CREAMOS UN SUBDIRECTORIO PARA LAS IMAGENES:

        _ APLI_1/STATIC/APLI_1/IMAGES/FOTOGRAFIA.JPG 
        _ DENTRO DE LOS ESTILOS:
                _ body {
                        background: url("images/fotografia.jpg")
                }    
========================================================================================================
============================= CREANDO LA VISTA PADRE ===================================================

_ ESTA VISTA DEBE SER CREADA DE TAL FORMA QUE SEA 
  HEREDADA POR LAS DEMAS .

_ EN EL PADRE.HTML:
        _ definimos los BLOCK (TITLE, LINK, SCRIPT, ETC).
                _ los hijos van a heredar toda la configuracion de estilos 
                  del padre pero podemos crear un {% BLOCK LINK %} y un {% BLOCK SCRIPT %}
                  para que cada pagina hijo creada como una aplicacion diferente pueda 
                  tener sus propios estilos en particular.
                  
        _ definimos la estructura general que sera heredada.  """

"""==========================================================================================================
==================================== CREACION DE MODELOS ====================================================
from django.db import models

class Place(models.Model):
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    place = models.OneToOneField(Place, primary_key=True)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher)
    authors = models.ManyToManyField(Author)


    
==================================================================================================================================
                ======================= RELATIONSHIPS FIELDS ==================
===================================================================================================================================







===============================================================================================================================                """