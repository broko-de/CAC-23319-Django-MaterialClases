from recursos_humanos.personal.empleados import Empleado


class Nomina:
    def __init__(self):
        self._lista_empleados = []

    def agregar_empleado(self, empleado):
        if not isinstance(empleado, Empleado):
            raise Exception('Se requiere una instancia de empleados')    
        self._lista_empleados.append(empleado)


    def print(self):
        for empleado in self._lista_empleados:
            if isinstance(empleado, Empleado):
                print(f"{empleado.nombre_completo} \t ${empleado.salario}")
                # ROMPE ENCAPSULAMIENTO print(f"{empleado._Empleado__nombre} \t ${empleado.salario}")
            else:
                print(f"En la nómina hay un no empleado: {empleado}")
