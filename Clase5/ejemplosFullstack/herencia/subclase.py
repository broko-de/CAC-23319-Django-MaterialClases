from herencia.producto import Producto

class Adorno(Producto):
    pass

class Alimento(Producto):
    productor =''
    distribuidor= ''

    def __init__(self, codigo, nombre, descripcion, precio,productor,distribuidor):
        #Con super puedo acceder a los metodos de la clase superior
        super().__init__(codigo, nombre, descripcion, precio)
        self.productor = productor
        self.distribuidor = distribuidor

    def __str__(self):
        return super().__str__()+f'Productor: {self.productor} \nDistribuidor:{self.distribuidor} \n'

class Libro(Producto):

    isbn = ""
    autor = ""

    def __init__(self, codigo, nombre, descripcion, precio,isbn,autor):
        super().__init__(codigo, nombre, descripcion, precio)
        self.isbn = isbn
        self.autor = autor
    def __str__(self):
        return super().__str__()+f'ISBN: {self.isbn} \nAutor: {self.autor} \n'