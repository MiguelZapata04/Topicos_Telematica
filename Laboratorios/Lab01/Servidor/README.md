# Lab01 - Sockets 

**Tabla de contenido**

- [Introduccion](#introducción)
    - [Objetivo](#objetivo)
    - [Prerrequisitos](#prerrequisitos)
    - [Herramientas utilizadas](#herramientas-utilizadas)
    - [Librerías usadas](#librerias-usadas)
- [Caracteristicas de funcionamiento](#caracteristicas-del-funcionamiento)
    - [Direccion IP y Puerto](#direccion-ip-y-puerto)
    - [Ejemplo de como realizar una peticion al servidor](#ejemplo-de-como-realizar-una-peticion-al-servidor)
    - [¿Que tipo de recursos se pueden solicitar al servidor?](#¿que-tipo-de-recursos-se-pueden-solicitar-al-servidor)
    - [URL de los recursos a los cuales puede acceder](#url-de-los-recursos-a-los-cuales-puede-acceder)
- [Referencias](#referencias)
    
---
## **Introducción**
En internet dos o más procesos se puede comunicar entre si de diferentes maneras. Para implementar un sistema distribuido uno de los mecanismos de comunicación más usados son los sockets, los cuales crean una clase de canal para la trasmisión de mensajes entre los procesos.

### **Objetivo**

Implementar un Mini-servidor web minimalista, que implemente únicamente el método
GET (versión 0.9 del protocolo HTTP). Debe recibir peticiones HTTP y procesarlas. El
procesamiento de la petición debe permitir el localizar el recurso solicitado en el
sistema de archivos local al mini-servidor. 

### **Prerrequisitos**

Para poderse conectar con el servidor se necesita el uso de un browser (ej: Chrome)

### **Herramientas utilizadas**

El lenguaje que se utilizo para el desarrollo de este laboratorio fue python.

### **Librerías usadas**

- socket
- threading 
- os

---
## **Caracteristicas del funcionamiento**

- El mini-servidor es concurrente y permite que máximo 10 clientes se conecten al tiempo. 
- Solo puede procesar peticiones de tipo GET. 
- Cuando el cliente se conecta y realiza una petición, el servidor la procesa. Luego de procesarla envía la respuesta correspondiente y cierra la conexión. 
- Para iniciar el servidor se debe realizar el siguiente proceso:

    -  En la línea de comandos se debe ejecutar el archivo server.py. Este sería el archivo principal y permitiría que el servidor pueda comenzar su ejecución. 

    - El archivo se ejecuta de la siguiente forma:

        ```
        python server.py
        ```

### **Direccion IP y Puerto** 
**AWS maquina:**
La dirección IP del servidor es: 44.194.128.228
El puerto por el cual esta escuchando es el: 80

Nota: La maquina se encuentra apagada, a la hora de calificación es necesario prenderla. Por tal razon, es necesario que me comunique para poderla prender 

**Maquina local:**
La direccion IP del servidor seria: 127.0.0.1
El puerto por el cual escucha es el: 80

Nota: El codigo que se monto en este github es para usarlo en la maquina local. 

### **Ejemplo de como realizar una peticion al servidor**

![Image text](https://github.com/MiguelZapata04/Topicos_Telematica/blob/master/Laboratorios/Lab01/Captura.png)

Como se puede obersvar en la imagen la dirección "127.0.0.1" es la dirección del servidor al que nos estamos conectando que en este caso es el servidor minimalista. El numero "80" seria el puerto por el que esta escuchando el servidor y finalmente la ruta "video/planeta.mp4" es la ubicación donde se encuentra el recurso que queremos solicitarle al servidor. Posteriormente el servidor procesa la petición y retorna la respuesta correspondiente al cliente (browser) para que este pueda renderisarla. 

### **¿Que tipo de recursos se pueden solicitar al servidor?**

- imagenes
- Videos 
- pdf
- html / htm
- Programas 

### **URL de los recursos a los cuales puede acceder**

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

---

## **Referencias** 
- Python, R. (2022, febrero 21). Socket programming in Python (guide). Realpython.com; Real Python. https://realpython.com/python-sockets/
- Python, R. (2019, marzo 25). An intro to threading in Python. Realpython.com; Real Python. https://realpython.com/intro-to-python-threading/
- OS module in python with examples. (2016, noviembre 21). GeeksforGeeks. https://www.geeksforgeeks.org/os-module-python-examples/
