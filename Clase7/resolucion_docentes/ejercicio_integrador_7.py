class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    def mostrar(self):
        print(
            f"Cuenta-> Titular:{self.titular.mostrar()}, Cantidad:{str(self.cantidad)}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad
