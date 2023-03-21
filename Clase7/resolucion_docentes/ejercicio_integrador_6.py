import ejercicio_integrador_excepciones


class Persona():
    def __init__(self, nombre='', edad=0, dni=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        # De esta forma estaría seteando directamente las variables "privadas"
        # pero al no usar las properties me perdería las validaciones
        # self.__nombre=nombre
        # self.__edad=edad
        # self.__dni=dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, nuevo_valor):
        self.__nombre = nuevo_valor

    def __validar_dni(self, numero):
        try:
            dni = int(numero)
        except ValueError:
            mensaje = f"Creación de Persona con DNI incorrecto: {dni}"
            print(mensaje)
            raise ejercicio_integrador_excepciones.PersonaDatoInvalidoError(mensaje)

        if len(str(dni)) < 7:
            mensaje = f"Creación de Persona con DNI incorrecto: {dni}"
            print(mensaje)
            raise ejercicio_integrador_excepciones.PersonaDatoInvalidoError(mensaje)

    @dni.setter
    def dni(self, nuevo_valor):
        self.__validar_dni(nuevo_valor)
        self.__dni = int(nuevo_valor)

    @edad.setter
    def edad(self, nuevo_valor):
        if nuevo_valor < 0:
            mensaje = f"Creación de Persona con Edad incorrecta: {nuevo_valor}"
            print(mensaje)
            raise ejercicio_integrador_excepciones.PersonaDatoInvalidoError(mensaje)
        else:
            self.__edad = nuevo_valor

    def mostrar(self):
        return f"Nombre: {self.nombre},Edad: {str(self.edad)},DNI: {self.dni}"

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Prueba de utilización de código
pepe = Persona()
print(pepe.mostrar())
juan = Persona("Alejandro", 39, "299500188")
print(juan.mostrar())
# juan.nombre = "Alberto"
# print(juan.mostrar())
# if juan.es_mayor_de_edad:
#     print(f"Juan es mayor de Edad")
# else:
#     print("Juan es menor")
# pedro = Persona("Pedro", 2, 23)
