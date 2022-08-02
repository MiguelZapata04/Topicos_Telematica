def realizar_header(nombre_archivo):
    if(nombre_archivo.endswith('.jpg')):
        tipo_archivo='image/jpg'
    elif(nombre_archivo.endswith('.jpeg')):
        tipo_archivo='image/jpeg'
    elif(nombre_archivo.endswith('.css')):
        tipo_archivo='text/css'
    elif(nombre_archivo.endswith('.pdf')):
        tipo_archivo='aplication/pdf'
    elif(nombre_archivo.endswith('.html')):
        tipo_archivo='text/html'
    elif(nombre_archivo.endswith('.msi')):
        tipo_archivo='application/oct-stream'
    elif(nombre_archivo.endswith('.mp4')):
        tipo_archivo='video/mp4'
    elif(nombre_archivo.endswith('.htm')):
        tipo_archivo='text/html'
    else:
        header='HTTP/1.1 404 File Not Found'.encode()
        return header        
    
    header = 'HTTP/1.1 200 OK\n'
    header += 'Content-Type: '+ str(tipo_archivo) + "\r\n\r\n"
    response = header.encode('utf-8')
    return response