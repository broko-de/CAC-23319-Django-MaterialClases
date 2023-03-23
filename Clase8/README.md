# Comandos vistos en clases 

Dirigirse a la carpeta **paquete_distribuible**:

```bash
cd paquete_distribuible
python setup.py sdist
```

Luego se tendrá que crear un entorno virtual y activarlo, recuerden salir del directorio **paquete_distribuible**
```bash
cd ../
python -m venv mi_entorno
source /mi_entorno/Script/activate #para windows
```
y por último podremos instalar el paquete distribuible que generamos con el siguiente comando si es que te encuentras en el directorio de Clase8
```bash
pip install paquete_distribuible/sdist/nombre_archivo.tar.gz #colocar el nombre correcto del archivo tar.gz generado
```
