"""
Un concepto importante en POO es el de las 
clases abstractas. Son clases en las que se 
pueden definir tanto métodos como propiedades, 
pero que no pueden ser instanciadas directamente.
 Solamente se pueden usar para construir subclases
  (como si fueran moldes). Permitiendo así tener 
una única implementación de los métodos compartidos, 
evitando la duplicación de código
*No pueden ser instanciadas
*No es obligatorio que tengan una implementación de todos 
los métodos necesarios
*Las clases derivadas de las clases abstractas deben 
implementar necesariamente todos los métodos abstractos 
Para poder crear clases abstractas en Python es necesario 
importar la clase ABC y el decorador abstractmethod 
del módulo abc (Abstract Base Classes). 

Se explica encapsulamiento que es el ocultamiento de propiedades de una clase
    para que no se puedan modificar desde afuera de la misma. Sino que el
    propio objeto lo haga. self.__nombre o bien self._nombre
    Esto es solo a modo de convencion, internamente python
"""
from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self,nombre,apellido,dni,email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__email = email
        self._edad = 18 #protegido
        self.__proyectos = []

    #el decorator property manejo un metodo como una propiedad. Agrega el encapsulamiento
    #para atributo privados
    @property
    def nombre(self):
        return self.__nombre
    
    #Asociamos el getter con su setter Nombre_funcion.setter para indicar que la funcion 
    #sera un setter y en este caso modificar el valor de la propiedad
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def nombre(self,nuevo_apellido):
        self.__apellido = nuevo_apellido
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,nuevo_dni):
        self.__dni = nuevo_dni

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,nuevo_email):
        self.__email = nuevo_email

    @property
    def nombre_completo(self):
        return f'{self.__apellido}, {self.__nombre}'
    
    @property
    def proyectos(self):
        return self.__proyectos
    
    def agregar_proyecto(self, proyecto):
        proyecto.estudiante = self
        self.__proyectos.append(proyecto)

    def remover_proyecto(self, proyecto):
        proyecto.estudiante = None
        self.__proyectos.remove(proyecto)

    @abstractmethod
    def registrarse():
        pass
    

class Estudiante(Persona):

    def __init__(self, nombre, apellido, dni, email,matricula):
        super().__init__(nombre, apellido, dni, email)
        self.__matricula = matricula
        self.__baja = 0

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,nuevo_matricula):
        self.__matricula = nuevo_matricula
    
    @property
    def baja(self):
        return self.__baja
    
    def registrarse(self):
        return f'{self.nombre_completo} se registro como estudiante'
    
    def soft_delete(self):
        self.__baja = 1

class Docente(Persona):

    def __init__(self, nombre, apellido, dni, email,legajo):
        super().__init__(nombre, apellido, dni, email)
        self.__legajo = legajo
        self.__cursos = []

    @property
    def legajo(self):
        return self.__legajo
    
    @legajo.setter
    def legajo(self,nuevo_legajo):
        self.__legajo = nuevo_legajo
    
    def agregar_curso(self, curso):
        curso.docente = self
        self.__cursos.append(curso)

    def remover_curso(self, curso):
        curso.docente = None
        self.__cursos.remove(curso)

    def registrarse(self):
        return f'{self.nombre_completo} se registro como docente'
    
# ERROR INSTANCIAR CLASE ABSTRACTA
# persona_uno = Persona('Mario','Gomez',23444111,'mario@gomez.com')
# print(persona_uno.nombre_completo)

docente = Docente('Mario','Gomez',23444111,'mario@gomez.com','DT-23344')
print(docente._edad)