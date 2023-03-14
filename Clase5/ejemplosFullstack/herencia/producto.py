"""
La herencia es la capacidad que tiene una clase 
de heredar los atributos y métodos de otra, 
ya preexistente, algo que nos permite reutilizar 
código.
las superclases son “moldes de moldes”.
A partir de la clase superior puedo construir 
clases hijas, clases derivadas, cada una con 
características comunes que comparten atributos 
con la clase padre, pero que también pueden tener
 atributos propios.
"""
class Producto():

    def __init__(self,codigo,nombre,descripcion,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    
    def __str__(self):
        return f'Producto Codigo: {self.codigo} \nNombre: {self.nombre} \nDescripcion: {self.descripcion} \nPrecio: ${self.precio}\n'

