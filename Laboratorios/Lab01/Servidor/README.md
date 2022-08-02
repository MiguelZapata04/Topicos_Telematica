# Lab01 - Sockets 

El mini-servidor fue realizado en python y cuenta con las siguintes funcionalidades:

- Permite el procesamiento de peticiones tipo GET 
- Luego de haber procesado la peticion del usuario, este procede a enviar la respuesta correspondiente 

## Librerias usadas 

- socket
- threading 
- os

## Funcionamiento

Para conectarse a este servidor se debe hacer uso de un browser (cliente). Despues de conectarse al servidor se pueden comenzar a realizar peticiones tipo GET ya que para efectos de este laboratorio es el unico metodo que se contemplo. 

### Como realizar una peticion al servidor

![Image text](https://github.com/MiguelZapata04/Topicos_Telematica/blob/master/Laboratorios/Lab01/Captura.png)

Como se puede obersvar en la imagen la direccion "127.0.0.1" es la direccion del servidor al que nos estamos conectando que en este caso es el servidor minimalista. El numero "80" seria el puerto por el que esta escuchando el servidor y finalmente la ruta "video/planeta.mp4" es la ubicacion donde se encuentra el recurso que queremos solicitarle al servidor. Posteriormente el servidor procesa la peticion y retorna la respuesta correspondiente al cliente (browser) para que este pueda renderisarla. 

