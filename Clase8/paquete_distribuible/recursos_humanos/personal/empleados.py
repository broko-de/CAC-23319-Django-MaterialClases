from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property
    @abstractmethod
    def salario(self):
        pass

class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    def __repr__(self) -> str:
        return self.nombre_completo


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, horas_trabajadas, valor_hora):
        super().__init__(nombre, apellido)
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def salario(self):
        return self.__horas_trabajadas * self.__valor_hora

    def __repr__(self) -> str:
        return self.nombre_completo


class EmpleadoPasante(Empleado):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    # Si no le defino la propiedad abstracta no puedo instanciar un EmpleadoPasante
    @property
    def salario(self):
        return 0