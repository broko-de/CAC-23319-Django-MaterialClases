#hago que nuestro paquete sea distribuible
from setuptools import setup

setup(
    name="recursos humanos",
    version="0.1",
    description="Paqete de ejemplo de empleados y nomina",
    author="Codo a Codo",
    author_email="cac@bue.edu.ar",
    url="https://www.buenosaires.gob.ar/educacion/codo-codo",    
    #especificos paquetes y subpaquetes
    packages=['recursos_humanos','recursos_humanos.personal'],    
    scripts=[]
)