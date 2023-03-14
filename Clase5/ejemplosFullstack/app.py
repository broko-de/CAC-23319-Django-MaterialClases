def saludo():
    print("Hola mundo #1")

saludo()

"""
__main__ es el nombre del ámbito en el que se ejecuta el código principal
__name__ me permite saber si el script esta siendo ejecutado 
del programa principal o bien si esta siendo importado
Nos permite hacer un checkeo si el programa esta siendo ejecutado
o importado.
Cuando importamos este archivo a otro, no ejectura ningun código,
mientras que si tenemos cosas en el prog principal e importamos nuestro
archivo, el otro archivo va a ejecutar todo el codigo del archivo A
que esta en el principal.
"""
# if __name__ == "__main__":
#     saludo()