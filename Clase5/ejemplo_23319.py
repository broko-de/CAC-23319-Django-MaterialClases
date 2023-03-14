from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido    
        self.dni = dni
        self.email = email
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

    @abstractmethod
    def registrarse(self):
        pass

        
class Estudiante(Persona): 
    def __init__(self, nombre, apellido, dni, email, matricula, baja):
        super().__init__(nombre, apellido, dni, email)
        self.matricula = matricula
        self.baja = baja

    def registrarse(self):
        print("El registro del estudiante fue exitoso")


class Docente(Persona):
    def __init__(self, nombre, apellido, dni, email, legajo):
        super().__init__(nombre, apellido, dni, email)
        self.legajo = legajo
      
    def registrarse(self):
        print("El registro del docente fue exitoso")


    
nuevo_estudiante = Estudiante("Victoria","López","287878969","vickylopez@gmail.com",111222,"0")
nuevo_estudiante.registrarse()

nuevo_docente = Docente("Lisando","López","2878888969","llopez@gmail.com",112422)
nuevo_docente.registrarse()

print(nuevo_docente)
print(nuevo_estudiante)