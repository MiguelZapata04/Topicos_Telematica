# **Lab05-1**

### **Información general**  
> Info de la materia: ST0263 Tópicos especiales en telemática  
> Estudiante: Miguel Ángel Zapata Jimenez, mazapataj@eafit.edu.co  
> Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co  
  
## **1. Breve descripción de la actividad**  
Se realizara la creacion de un cluster AWS EMR en Amazon, que permitira el desarrollo de las siguientes actividades de este laboratorio. A tráves, de esta actividad se desarrollaran habilidades en la construcción y destrucción de un cluster en AWS.  
  
### **1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)**  
  
---  
  
## **2. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**  
  
### **Detalles técnicos**  
  
**Plataforma de nube usada:** AWS (Amazon Web Services)  
**Sistema operativo:**  Amazon Linux 2 AMI  
**Servicio web utilizado:** EMR (Elastic MapReduce)  
**Puerto para HUE:** 8888  
**Puerto para JupyterHub:** 9443  
**Puerto para Zeppelin:** 8890    
  
### **Como se ejecuta:**  
  
* Realizar lo que se explica en la seccion [Lanzar cluster](#como-se-ejecuta-y-compila)
  
### **2.1. Creación cluster**  
  
* Se busca el servicio EMR  
![image text](img/step1-sw/Buscar_emr.png)  
  
* Se selecciona la opción crear cluster  
![image text](img/step1-sw/Seleccionar_crear_cluster.png)  
  
#### **Step 1: SoftWare**  
  
* Lo primero que se debe realizar es la configuración de las versiones de los componentes que se usaran en el cluster  
![image text](img/step1-sw/Version_componentes.png)  
  
* Despues se realiza la integración de los catalogos para GLUE, donde se seleccionan las opciones para la visualización de las tablas en Spark y Hive  
![image text](img/step1-sw/Conf_catalogo_glue.png)  
  
* A continuación, se procede a configurar el bucket para almacenar los datos de los notebooks  
![image text](img/step1-sw/conf_bucket_almacenar_datos_notebooks.png)  
  
* Antes de continuar se debe realizar la configuración correcta de la persistencia del bucket  
![image text](img/step1-sw/conf_persistencia_buckets.png)  
  
#### **Step 2: HardWare**  
  
* En esta paso se debe cambiar el tamaño del hw de los nodos para que estos se puedan ejecutar  
![image text](img/step2-hw/cambiar_hw_menor_no_deja_correr.png)  
  
* Luego se asigna el almacenamiento para cada nodo  
![image text](img/step2-hw/Alm_nodos.png)  
  
#### **Step 3: Configuración general del cluster**  

* Se cambia el nombre del cluster y se dejan las demas opciones por defecto  
![image text](img/stetp3-conf_general/Opciones_Generales.png)  
  
#### **Step 4: Seguridad**  

* Se realiza la asignación de la clave .pem  
![image text](img/step4-seguridad/Asignacion_clave.png)  
  
* Se crea el cluster y luego se debe esperar a que este se ejecute  
![image text](img/step4-seguridad/proceso_creacion.png)  
  
* Se verifica que el cluster se inicio de manera correcta  
![image text](img/step4-seguridad/verificacion_cluster_exitoso.png)  
  
#### **Configuración de los puertos de entrada**  
  
* Se configuran los puertos para el master  
![image text](img/step4-seguridad/ssh_para_master.png)  
  
### **2.2. Configuración del bucket**  
  
* Se busca el servicio S3 (servicio nfs que proporciona AWS)  
![image text](img/bucket/Busca_servicio_bucket.png)  
  
* Configuración del bucket y creación
![image text](img/bucket/conf_bucket.png)  
  
* Se verifica que el bucket quedo creado de manera exitosa  
![image text](img/bucket/bucket_creado.png)  
  
* Se visualizan las aplicaciones de interfaz de usuario disponibles  
![image text](img/bucket/aplicacion_dispo.png)  
  
* En la opcion de bloqueo de acceso publico (block public access), se deben agregar los puertos correspondientes a cada uno de las interfaces de usuario que se usaran  
![image text](img/bucket/puertos_apps_conf.png)  
  
* Despues se editan las politicas de seguridad del master como se muestra a continuación  
![image text](img/bucket/Reglas_entrada.png)  
  
### **2.3. Acceso a las interfaces de usuario**  

#### **HUE**  
  
* Creación de usuario  
![image text](img/hue/accediendo_a_hue.png)  
  
* Ingreso a la plataforma de adminstración  
![image text](img/hue/ingreso_hue.png)  
  
* Interfaz de administración de hdfs  
![image text](img/hue/hdfs_administrador_es_temporal.png)  
  
* Interfaz de administración de S3. En S3 los datos son persistentes y no se perderan asi se destruya el cluster  
![image text](img/hue/persistente_s3_bucket_admin.png)  
  
#### **Jupyter Hub**  

* Ingreso a la plataforma. En este caso, jupyter maneja un usuario y contraseña por defecto.  
![image text](img/jupyter/acceso_jupiterhub.png)  
  
* Prueba de notebook pyspark el cual se almacenara en S3   
![image text](img/jupyter/prueba_notebook.png)  
  
* Como se ven los notebooks que tenemos creados en jupyter  
![image text](img/jupyter/vew_notebook.png)  
  
#### **Zeppelin**  
  
Notebooks que soportan varios lenguajes nativamente.
  
* Acceso a la plataforma  
![image text](img/zeppelin/acceso_zepelin.png)  
  
* Interacción con la creacion de un notebook nuevo  
![image text](img/zeppelin/zepelin_interact.png)  
  
Podemos verificar en el administrador de S3 de HUE que claramente los notebooks se guardan y son persistentes. A continuación, se puede observar como quedan guardados.  
![image text](img/bucket/verificar_notebooks_no_se_pierden.png)

---
  
## **3. Descripción del ambiente de ejecucion: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**  
  
### **Como se ejecuta y compila**  
  
1. Se accede de la siguiente manera luego de que el cluster se encuentre en ejecucion: Se dirije a la carpeta donde esta la clave .pem y se abre la terminal en ese ubicacion. Luego se ejecuta el siguiente comando para ingresar:  
![image text](img/step4-seguridad/comando_para_ingresar.png)  
![image text](img/step4-seguridad/ingreso_cluster.png)  
  
### **Como ingresar a las interfaces de usuario**  
  
Se accede a tráves del browser y las siguientes urls:
  
**URL´S:**  
* **HUE:** http://ec2-44-200-25-176.compute-1.amazonaws.com:8888/  
* **JupyterHub:** https://ec2-44-200-25-176.compute-1.amazonaws.com:9443/  
* **Zeppelin:** http://ec2-44-200-25-176.compute-1.amazonaws.com:8890/  
  
---
## **5. Referencias**  

* [https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-1-aws-emr.txt](https://github.com/st0263eafit/st0263-2022-2/blob/main/bigdata/lab5-1-aws-emr.txt)  
* [https://www.youtube.com/watch?v=MyXSwxN5Zdk](https://www.youtube.com/watch?v=MyXSwxN5Zdk)  
* [https://www.youtube.com/watch?v=3sao-qJG34Y](https://www.youtube.com/watch?v=3sao-qJG34Y)
