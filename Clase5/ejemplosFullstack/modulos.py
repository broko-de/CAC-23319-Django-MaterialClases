from datetime import datetime
from collections import Counter
import math
import random

#COUNTER
numeros = [1,2,3,4,1,2,3,1,2,1]
print(Counter(numeros))
print(Counter("palabra"))

#FECHAS
dt=datetime.now()#Fechayhoraactual
print(dt)#Imprimefechayhoraactual
print("Año:",dt.year)#Año
print("Mes:",dt.month)#Mes
print("Dia:",dt.day)#Dia
print("Hora:",dt.hour)#Hora
print("Minuto:",dt.minute)#Minuto
print("Segundo:",dt.second)#Segundo
print("Microsegundo:",dt.microsecond)#Microsegundo
print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
print("{}/{}/{}".format(dt.day,dt.month,dt.year))

#MATH
print(math.floor(3.99))  # Redondeo a la baja (suelo)
print(math.ceil(3.01))   # Redondeo al alta (techo)
print(math.trunc(123.45))
print(math.pow(2, 3))  # Potencia con flotante 
print(math.sqrt(9))

#RANDOM
# Flotante aleatorio >= 0 y < 1.0
print(random.random())      
# Flotante aleatorio >= 1 y <10.0       
print(random.uniform(1,10))
# Entero aleatorio de 0 a 9, 10 excluído
print(random.randrange(10))
# Entero aleatorio de 0 a 100
print(random.randrange(0,101))
# Entero aleatorio de 0 a 100 cada 2 números, múltiples de 2
print(random.randrange(0,101,2))
# Entero aleatorio de 0 a 100 cada 5 números, múltiples de 5
print(random.randrange(0,101,5))

