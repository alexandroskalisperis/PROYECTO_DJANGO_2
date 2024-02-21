from django.shortcuts import render
from django.views import View
import AVMWeather as weather
import requests
from datetime import datetime


# Create your views here.


class Mi_tiempo(View):
    def __init__(self):
        self.titulo = "el tiempo"
        self.hora = datetime.now()
        

    def tiempo(self, request):
        self.parte_1 = "https://maps.google.com/maps?q="
        self.parte_2 = ""
        self.parte_3 = "&t=&z=13&ie=UTF8&iwloc=&output=embed"
        self.todas_las_partes = self.parte_1+self.parte_2+self.parte_3

        
        return render(
            request,
            "tiempo.html",
            {
                "titulo": self.titulo,
                "todas_las_partes": self.todas_las_partes,
                "hora": self.hora,            
                
            }
        )
    

    def direccion(self, request):
        try:
            self.direccion_tiempo = request.POST["direccion"]
            self.parte_1 = "https://maps.google.com/maps?q="
            self.parte_2 = self.direccion_tiempo.replace(" ","+")
            self.parte_3 = "&t=&z=13&ie=UTF8&iwloc=&output=embed"
            self.todas_las_partes = self.parte_1+self.parte_2+self.parte_3

            BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
            API_KEY = "9063a03c462228779eaa47dc95ff32d5"
            CITY = self.direccion_tiempo
            url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
            self.response = requests.get(url).json()

        
            self.temperatura_1 = self.response["main"]["temp"]  
            self.sensacion = self.response["main"]["feels_like"]
            self.cuenta_1 = self.temperatura_1 - 273.5
            self.grados_centigrados = round(self.cuenta_1, 2)

            
            self.cuenta_2 = self.sensacion - 273.5
            self.sensacion_termica = round(self.cuenta_2, 2)
        except KeyError:
            self.direccion_tiempo = """la direccion ingresada 
            presenta alguna falla, trate de ser mas especifico."""
            self.grados_centigrados = ""
            self.sensacion_termica = ""
        
        return render(
            request,
            "tiempo.html",
            {
                "titulo": self.titulo,
                "respuesta": self.response,
                "todas_las_partes": self.todas_las_partes,
                "direccion": self.direccion_tiempo,
                "grados": self.grados_centigrados,
                "sensacion": self.sensacion_termica,
                "hora": self.hora,
            }
        ) 
    

    def clima(self, request):
        try:
            self.respuesta = self.response
            self.clima_datos = self.respuesta["weather"]
            self.clima_datos_interno = self.clima_datos[0]
            self.codigo_imagen = self.clima_datos_interno["icon"]
            
            self.latitud = round(self.respuesta["coord"]["lat"],2)
            self.longitud = round(self.respuesta["coord"]["lon"],2)

            if self.respuesta:
                return render(
                    request,
                    "clima.html", 
                    {
                        "titulo": self.titulo,
                        "respuesta": self.response,
                        "codigo_imagen": self.codigo_imagen,
                        "latitud": self.latitud,
                        "longitud": self.longitud,
                        
                    }
                )
            
        except AttributeError or KeyError:
            self.mensaje_error = "no existen datos disponibles"
            return render(
                request,
                "clima.html",
                {
                    "titulo": self.titulo,
                    "mensaje_error": self.mensaje_error,
                }
            )
        
            

    def temperatura(self, request):
        try:
            self.respuesta = self.response

            if self.respuesta:
                self.latitud = round(self.respuesta["coord"]["lat"],2)
                self.longitud = round(self.respuesta["coord"]["lon"],2)
                return render(
                    request,
                    "temperatura.html",
                    {
                        "titulo": self.titulo,
                        "respuesta": self.response,
                        "grados": self.grados_centigrados,
                        "sensacion": self.sensacion_termica,
                        "latitud": self.latitud,
                        "longitud": self.longitud,
                        
                    }
                )
        except AttributeError or KeyError:
            self.mensaje_error = "no existen datos disponibles"
            return render(
                request,
                "temperatura.html",
                {
                    "titulo": self.titulo,
                    "mensaje_error": self.mensaje_error, 
                }
            )

    def humedad(self, request):
        try:
            self.respuesta = self.response

            if self.respuesta:
                self.latitud = round(self.respuesta["coord"]["lat"],2)
                self.longitud = round(self.respuesta["coord"]["lon"],2)
                self.humedad_enlace = self.respuesta["main"]["humidity"]
                self.presion_atmosferica = self.respuesta["main"]["pressure"]
                
                return render(
                    request,
                    "humedad.html",
                    {
                        "titulo": self.titulo,
                        "respuesta": self.response,
                        "grados": self.grados_centigrados,
                        "sensacion": self.sensacion_termica,
                        "latitud": self.latitud,
                        "longitud": self.longitud,
                        "humedad": self.humedad_enlace,
                        "presion_atmosferica": self.presion_atmosferica,             
                    }
                )
        except AttributeError or KeyError:
            self.mensaje_error = "no existen datos disponibles"
            return render(
                request,
                "humedad.html",
                {
                    "titulo": self.titulo,
                    "mensaje_error": self.mensaje_error, 
                }
            )
    
    def visibilidad(self, request):
        try:
            self.respuesta = self.response

            if self.respuesta:
                self.latitud = round(self.respuesta["coord"]["lat"],2)
                self.longitud = round(self.respuesta["coord"]["lon"],2)
                self.vista = self.respuesta["visibility"]
                
                return render(
                    request,
                    "visibilidad.html",
                    {
                        "titulo": self.titulo,
                        "respuesta": self.response,
                        "latitud": self.latitud,
                        "longitud": self.longitud,
                        "vista": self.vista,
                        
                                     
                    }
                )
        except AttributeError or KeyError:
            self.mensaje_error = "no existen datos disponibles"
            return render(
                request,
                "visibilidad.html",
                {
                    "titulo": self.titulo,
                    "mensaje_error": self.mensaje_error, 
                }
            )
        

    

    def viento(self, request):
        try:
            self.respuesta = self.response

            if self.respuesta:
                self.latitud = round(self.respuesta["coord"]["lat"],2)
                self.longitud = round(self.respuesta["coord"]["lon"],2)
                self.vista = self.respuesta["visibility"]
                self.viento_1 = self.respuesta["wind"]
                
                return render(
                    request,
                    "viento.html",
                    {
                        "titulo": self.titulo,
                        "respuesta": self.response,
                        "latitud": self.latitud,
                        "longitud": self.longitud,
                        "vista": self.vista,
                        "viento_1": self.viento_1,
                        
                                     
                    }
                )
        except AttributeError or KeyError:
            self.mensaje_error = "no existen datos disponibles"
            return render(
                request,
                "viento.html",
                {
                    "titulo": self.titulo,
                    "mensaje_error": self.mensaje_error, 
                }
            )
        
    
    def coordenadas(self, request):
        try:
            self.respuesta = self.response

            if self.respuesta:
                self.latitud = round(self.respuesta["coord"]["lat"],2)
                self.longitud = round(self.respuesta["coord"]["lon"],2)
                self.sunrise = self.respuesta["sys"]["sunrise"]
                self.sunset = self.respuesta['sys']["sunset"]
                self.fecha_hora_amanecer = datetime.fromtimestamp(self.sunrise)
                self.fecha_hora_puesta_sol = datetime.fromtimestamp(self.sunset)
              
                return render(
                    request,
                    "coordenadas.html",
                    {
                        "titulo": self.titulo,
                        "respuesta": self.response,
                        "latitud": self.latitud,
                        "longitud": self.longitud,
                        "fecha_hora_amanecer": self.fecha_hora_amanecer,
                        "fecha_hora_puesta_sol": self.fecha_hora_puesta_sol,
                                     
                    }
                )
        except AttributeError or KeyError:
            self.mensaje_error = "no existen datos disponibles"
            return render(
                request,
                "coordenadas.html",
                {
                    "titulo": self.titulo,
                    "mensaje_error": self.mensaje_error, 
                }
            )
        
        return render(
            request,
            "coordenadas.html",
            {
                "titulo": self.titulo,
            }
        )