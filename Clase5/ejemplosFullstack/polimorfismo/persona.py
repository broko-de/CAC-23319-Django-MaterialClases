"""
Los métodos son polimorfos. El polimorfismo 
quiere decir que el método que vaya a 
implementar / ejecutar a la hora de ser 
llamado en tiempo de ejecución va a establecer 
el comportamiento del objeto.

"""
class Persona:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f'Hola soy: {self.nombre}'

    def trabajar(self):
        pass