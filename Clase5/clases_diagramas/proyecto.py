from persona import Estudiante,Docente

class Proyecto:

    def __init__(self,nombre,nombre_slug,anio,descripcion,url,portada,estudiante):
        self.__nombre = nombre
        self.__nombre_slug = nombre_slug
        self.__anio = anio
        self.__descripcion = descripcion
        self.__url = url
        self.__portada = portada
        self.__estudiante = estudiante

    def __str__(self) -> str:
        return f'Proyecto: {self.__nombre} - Estudiante: {self.__estudiante.nombre_completo}'
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def nombre_slug(self):
        return self.__nombre_slug
    
    @nombre_slug.setter
    def nombre_slug(self,nuevo_nombre_slug):
        self.__nombre_slug = nuevo_nombre_slug

    @property
    def anio(self):
        return self.__anio
    
    @anio.setter
    def anio(self,nuevo_anio):
        self.__anio = nuevo_anio

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,nuevo_descripcion):
        self.__descripcion = nuevo_descripcion

    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self,nuevo_url):
        self.__url = nuevo_url

    @property
    def portada(self):
        return self.__portada
    
    @portada.setter
    def portada(self,nuevo_portada):
        self.__portada = nuevo_portada

    @property
    def estudiante(self):
        return self.__estudiante
    
    @estudiante.setter
    def estudiante(self,nuevo_estudiante):
        self.__estudiante = nuevo_estudiante