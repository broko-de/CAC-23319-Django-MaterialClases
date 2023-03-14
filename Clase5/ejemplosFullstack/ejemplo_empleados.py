"""
Se explica ejemplo de clase abstracta ABC - Son clases en las que se 
    pueden definir tanto métodos como propiedades, 
    pero que no pueden ser instanciadas directamente.
    Solamente se pueden usar para construir subclases
    (como si fueran moldes). Permitiendo así tener 
    una única implementación de los métodos compartidos, 
    evitando la duplicación de código
    *No pueden ser instanciadas
    *No es obligatorio que tengan una implementación de todos 
    los métodos necesarios
    *Las clases derivadas de las clases abstractas deben 
    implementar necesariamente todos los métodos abstractos 
    Para poder crear clases abstractas en Python es necesario 
    importar la clase ABC y el decorador abstractmethod 
    del módulo abc (Abstract Base Classes).

Se explica encapsulamiento que es el ocultamiento de propiedades de una clase
    para que no se puedan modificar desde afuera de la misma. Sino que el
    propio objeto lo haga. self.__nombre o bien self._nombre
    Esto es solo a modo de convencion, internamente python

Se explica decorador @property, se agrega encapsulamiento a propiedades privadas 
    por medio de un metodo publico.

Es explica decorador @abstractmethod
"""
from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    #el decorator property manejo un metodo como una propiedad. Agrega el encapsulamiento
    #para atributo privados
    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property
    @abstractmethod
    def salario(self):
        pass

"""
Se explica herencia de una clase abstracta y como la implementan
super() permite llamar a metodos de la superclase

Polimorfismo
"""
class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, horas_trabajadas, valor_hora):
        super().__init__(nombre, apellido)
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def salario(self):
        return self.__horas_trabajadas * self.__valor_hora

#Name mangling
empleado = EmpleadoPorHora('fede','liquin',233,22)
print(empleado._EmpleadoPorHora__valor_hora)

class EmpleadoPasante(Empleado):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    # Si no le defino la propiedad abstracta no puedo instanciar un EmpleadoPasante
    # @property
    # def salario(self):
    #     return 0




class Nomina:
    def __init__(self):
        self.__lista_empleados = []

    def agregar_empleado(self, empleado):
        self.__lista_empleados.append(empleado)

    def print(self):
        for empleado in self.__lista_empleados:
            if isinstance(empleado, Empleado):
                print(f"{empleado.nombre_completo} \t ${empleado.salario}")
                # ROMPE ENCAPSULAMIENTO print(f"{empleado._Empleado__nombre} \t ${empleado.salario}")
            else:
                print(f"En la nómina hay un no empleado: {empleado}")


nomina_empleados = Nomina()
nomina_empleados.__lista_empleados = [1,32]
print(nomina_empleados.__lista_empleados)

nomina_empleados.agregar_empleado(EmpleadoFullTime('Mario', 'Lobo', 6000))
nomina_empleados.agregar_empleado(EmpleadoFullTime('Daniel', 'Juarez', 6500))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Gutavo', 'Balvorin', 200, 50))
franco_sosa = EmpleadoPorHora('Franco','Sosa',150,100)
nomina_empleados.agregar_empleado(franco_sosa)
nomina_empleados.agregar_empleado(EmpleadoPorHora('Santi', 'Caseres', 100, 150))
# Un empleado no se puede instanciar porque es una clase abstracta
# nomina_empleados.agregar_empleado(Empleado('Diego', 'Armando', 10))
# Si tiene la implementación de salario si se puede instanciar, sino no.
# nomina_empleados.agregar_empleado(EmpleadoPasante('Diego', 'Godin'))

nomina_empleados.print()


#Herencia múltiple
class Estudiante():
    def __init__(self, legajo):
        self.__legajo = legajo

    @property
    def legajo(self):
        return self.__legajo

    def __str__(self):
        return f"Legajo: {self.__legajo}"

class EstudiantePasante(Empleado, Estudiante):
    def __init__(self, nombre, apellido, legajo):
        Empleado.__init__(self, nombre, apellido)
        Estudiante.__init__(self, legajo)

    # Tengo que implementar la propiedad salario porque hereda de empleado
    @property
    def salario(self):
        return 0

    def __str__(self):
        return f"{self.nombre_completo}. Legajo: {self.legajo}"


mis_estudiantes = []
mis_estudiantes.append(Estudiante(999))
mis_estudiantes.append(5)
mis_estudiantes.append(EstudiantePasante("Panchito", "Maidana", 5))


for estudiante in mis_estudiantes:
    if isinstance(estudiante, Estudiante):
        print(estudiante)
    else:
        print(f"El valor {estudiante} no es un estudiante")


