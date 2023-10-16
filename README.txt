Para ejecutar el proyecto se debe tener instalada la última versión de Docker.
Además, se debe contar con un editor de código para ejecutar los comandos necesarios.

Una vez clonado el repositorio alojado en Github, desde el editor de código se deben ejecutar los comandos:

1- /venv/Scripts/activate.bat
2- docker build -t flaskapp .
3- docker -it -p 5000:4000 flaskapp

El puerto 5000 puede ser reemplazado si este está ocupado en su equipo.

Finalmente, para interactuar con el proyecto se debe acceder a la dirección localhost:5000/ en su navegador de preferencia.