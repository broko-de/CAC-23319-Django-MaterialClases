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
"""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def emitir_sonido(self):
        print('El animal emite sonido: ',end='\n')
        