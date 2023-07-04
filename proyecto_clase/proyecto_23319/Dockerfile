#version de la imagen queremos crear el contenedor
FROM python:3.9

#Especificamos un directorio de trabajo, es como hacer un mkdir y cd
WORKDIR /proyecto_23319

#Copiamos el archivo requirements dentro del contenedor
COPY requirements.txt /proyecto_23319/requirements.txt

#Ejecutamos la instalación de las dependecias dentro del contenedor
RUN pip install --no-cache-dir --upgrade -r /proyecto_23319/requirements.txt

#Copiamos el resto del contenido de este directorio al workdir del contenedor
COPY . /proyecto_23319/

#Exponemos el puerto 8000 para que sea vinculable con el anfitrion
EXPOSE 8000