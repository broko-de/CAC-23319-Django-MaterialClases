"""
La herencia múltiple es la capacidad de una subclase
 de heredar de múltiples superclases.
Esto conlleva un problema, y es que si 
varias superclases tienen los mismos atributos
 o métodos, la subclase sólo podrá heredar de
  una de ellas. clases más a la izquierda 
"""

from herenciamultiple.spideruno import SpiderUno
from herenciamultiple.spiderdos import SpiderDos

class SpiderVerse(SpiderDos,SpiderUno):

    def __init__(self):
        print('Soy el spiderman de Tom Holland')


    def hablar(self):
        print('No me quiero ir señor Stark')