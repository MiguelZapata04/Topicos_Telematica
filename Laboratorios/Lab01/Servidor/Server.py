import socket 
import threading
import Manejo_request

mi_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def main():
    print("Comienzo de la ejecucion del servidor")
    print("Direccion IP del servidor: ", "127.0.0.1")
    print("Puerto: ",80)
    servidor()

def servidor():
    mi_socket.bind(("127.0.0.1",80))
    mi_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mi_socket.listen(10)
    while True:
        cliente, dir_cliente = mi_socket.accept()
        hilo_para_cliente = threading.Thread(target=Manejo_request.conexion_cliente,args=(cliente,dir_cliente))
        hilo_para_cliente.start()

if __name__ == '__main__':
    main()