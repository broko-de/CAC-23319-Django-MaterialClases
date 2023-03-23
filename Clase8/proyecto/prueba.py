from recursos_humanos.nomina import Nomina
from recursos_humanos.personal.empleados import EmpleadoFullTime

nomina = Nomina()
nomina.print()

empleado = EmpleadoFullTime('Mario','Lobo',123333)
nomina.agregar_empleado(empleado)
nomina.print()
