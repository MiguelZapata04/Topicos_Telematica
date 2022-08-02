import Manejo_header
import os

directory_root = "C:/Users/Usuario/Documents/Estudio/EAFIT/SegundoSemestre-2022/Topicos Especiales Telematica/Laboratorios/Lab01/Servidor/Server_data/"

def conexion_cliente(cliente,dir_cliente):
    print(f'Conexion proveniente de: {dir_cliente[0]}')
    conectado = True
    while conectado:
        request = cliente.recv(9999999).split(b"\r\n\r\n")
        descomponer_request = request[0].decode().split(' ')
        metodo = descomponer_request[0]
        nombre_archivo = descomponer_request[1]
        print("*************************************")
        print("Esta seria la solicitud que el usuario esta realizando: ")
        print(f'{metodo} {nombre_archivo} HTTP/1.1')
        print("*************************************")
        if (metodo == 'GET'):
            if nombre_archivo.lstrip('/') == '':
                nombre_archivo = directory_root+"index.html"
            elif not(os.path.exists(directory_root+nombre_archivo)):
                header = 'HTTP/1.1 404 Not Found\r\n\r\n'.encode()
                body_response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')  
            else: 
                contenido_archivo = open(directory_root+nombre_archivo,'rb')
                body_response = contenido_archivo.read()
                contenido_archivo.close()
                header = Manejo_header.realizar_header(nombre_archivo)

            print("Este seria la respuesta que se le envia al usuario: ")
            response = header + body_response
            print(header.decode())
            print("*************************************")
            cliente.sendall(response)
            conectado = False
        else:
            print("El valor es desconocido")
            conectado = False
    cliente.close()