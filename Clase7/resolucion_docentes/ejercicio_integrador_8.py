from ejercicio_integrador_6 import Persona
from ejercicio_integrador_7 import Cuenta
import ejercicio_integrador_excepciones


class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        print(f"Cuenta Joven -> Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%")

    def es_titular_valido(self):
        return self.titular.edad < 25 and self.titular.es_mayor_de_edad()

    def retirar(self, cantidad):
        if not self.es_titular_valido():
            mensaje = f"El titular {self.titular} no puede retirar dinero porque es inválido"
            print(mensaje)
            raise ejercicio_integrador_excepciones.CuentaJovenTitularInvalidoError(mensaje)
        elif cantidad > 0:
            super().retirar(cantidad)


# Pruebas de código
# juan = Persona("Juan", 12, 29950189)
# cuenta_juan = CuentaJoven(juan, 20.5, 10)
# cuenta_juan.ingresar(30.2)
print('****'*3)
# cuenta_juan.retirar(1)
# cuenta_juan.mostrar()
