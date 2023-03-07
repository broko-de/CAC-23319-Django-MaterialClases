#CONVECIONES
numeroUno = 23
var numero_dos = 50 #definicionde variable incorrecta
numero_tres =33
UNACONSTANTE = 100
OTRA_CONSTANTE = 200

     suma = numero_tres+3 #identacion incorrecta

class MiClase:
    pass

class otra_clase:
    pass

import os, sys #importacion forma incorrecta
import os 
import sys

# FUCIONES 
# funcion suma(a,b){ NO ES FUNCION EN PYTHON
#     return a+b
# }

""" 
    Funcion que permite sumar dos numeros
        Parameters:
            a (int): numero
            b (int): numero
        Returns:
            c (int): resultado de la suma
"""
    
def suma(a,b):
    c = a+b
    return c


suma(numero_tres,55)

#EJEMPLO DE SCOPRE
# BUILD-IN
print("Hola, mundo!")
# assert, break

#GLOBAL
x = 10  # 'x' es una variable global
mesanje = 'Hola me presento soy un mensaje Global'

def saludo():
    print(mesanje)

saludo()

#ENCLOSING

def saludo_dos():
    mensaje_dos = 'Hola estoy dentro de saludos_dos'

    def bienvenida():
        print(mensaje_dos)
    
    bienvenida() 

saludo_dos()
# print(mensaje_dos)


#LOCAL
def saludo_tres():
    mensaje_tres = 'Hola me presento soy un mensaje Local'
    print(mensaje_tres)

saludo_tres()

#TIPOS DE DATOS
mi_diccionario = {
    'nombre':'Mario',
    'apellido':'Lobo',
}

mi_tupla = (24,5)