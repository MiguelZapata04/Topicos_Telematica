# Lab01 - Sockets 

## Objetivo

Implementar un Mini-servidor web minimalista, que implemente únicamente el método
GET (versión 0.9 del protocolo HTTP). Debe recibir peticiones HTTP y procesarlas. El
procesamiento de la petición debe permitir el localizar el recurso solicitado en el
sistema de archivos local al mini-servidor.

### Prerequisitos

Para poderse conectar con el servidor se neceita el uso de un browser (ej: Chrome)

### Herramientas utilizadas

El lenguaje que se utilzo para el desarrollo de este laboratorio fue python.

### Librerias usadas 

- socket
- threading 
- os

## Caracteristicas del funcionamiento 

- El mini-servidor es concurrente y permite que maximo 10 clientes se conecten al tiempo. 
- Solo puede procesar peticiones de tipo GET. 
- Cuando el cliente se conecta y realiza una peticion, el servidor la procesa. Luego de procesarla envia la respuesta correspondiente y cierra la conexion. 

### Direccion IP y Puerto 

La dirección IP del servidor es: 44.194.128.228
El puerto por el cual esta escuchando es el: 80

### Ejemplo de como realizar una peticion al servidor

![Image text](https://github.com/MiguelZapata04/Topicos_Telematica/blob/master/Laboratorios/Lab01/Captura.png)

Como se puede obersvar en la imagen la direccion "127.0.0.1" es la direccion del servidor al que nos estamos conectando que en este caso es el servidor minimalista. El numero "80" seria el puerto por el que esta escuchando el servidor y finalmente la ruta "video/planeta.mp4" es la ubicacion donde se encuentra el recurso que queremos solicitarle al servidor. Posteriormente el servidor procesa la peticion y retorna la respuesta correspondiente al cliente (browser) para que este pueda renderisarla. 

### ¿Que tipo de recursos se pueden solicitar al servidor?

- imagenes
- Videos 
- pdf
- html / htm
- Programas 

### URL de los recursos a los cuales puede acceder

Imagenes:
- http://44.194.128.228:80/img/car.jpeg
- http://44.194.128.228:80/img/perro.jpg
- http://44.194.128.228:80/img/Eafit.jpg

Videos:
- http://44.194.128.228:80/video/Flores.mp4
- http://44.194.128.228:80/video/Planeta.mp4

pdf:
- http://44.194.128.228:80/pdf/OWASP.pdf

text:
- http://44.194.128.228:80/text/index.html
- http://44.194.128.228:80/text/text.htm

Programa:
- http://44.194.128.228:80/Programa/putty.msi

## Referencias 
- Python, R. (2022, febrero 21). Socket programming in Python (guide). Realpython.com; Real Python. https://realpython.com/python-sockets/
- Python, R. (2019, marzo 25). An intro to threading in Python. Realpython.com; Real Python. https://realpython.com/intro-to-python-threading/
- OS module in python with examples. (2016, noviembre 21). GeeksforGeeks. https://www.geeksforgeeks.org/os-module-python-examples/
