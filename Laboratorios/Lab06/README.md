# **Lab06 - Spark**  
  
### **Información general**  
> Info de la materia: ST0263 Tópicos especiales en telemática  
> Estudiante: Miguel Ángel Zapata Jimenez, mazapataj@eafit.edu.co  
> Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co  
  
## **1. Breve descripción de la actividad**  
Se desarrollaro un contador de palabras usando pyspark. Ademas, se interactuo con pyspark de distintas maneras, que seran explicadas en este informe. Es importante resaltar, que gracias a las interaciones con pyspark, tambien se pudo desarrollar mejores competencias en el uso del servicio EMR y las distintas interfaces de usuario que provee. Tales como, HUE, JupyterHub y Zeppelin.   
  
---  

### **1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)**  
  
* Se logro ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master.  
* Se logro ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida)  vía ssh en el nodo master.  
* Se logro ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.  
* Se logro ejecutar el wordcount desde un archivo de python.
* Se logro replicar ejecutar y entender el notebook: Data_processing_using_PySpark.ipynb con los datos respectivos.
Tambien, se logro ejecutarlo en AWS EMR.  
  
---  
  
## **2. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**  
  
### **Detalles técnicos**  
  
**Plataforma de nube usada:** AWS (Amazon Web Services)  
**Sistema operativo:**  Amazon Linux 2 AMI  
**Servicio web utilizado:** EMR (Elastic MapReduce)  
**FrameWork de computación en cluster utilizado:** Spark
**Puerto para HUE:** 8888  
**Puerto para JupyterHub:** 9443  
**Puerto para Zeppelin:** 8890    
**Lenguaje de programación usado:** Python (3.10.7)  
**Librerias usadas:** pandas_udf, PandasUDFType, udf, StringType, DoubleType, IntegerType, pyspark

### **Adecuación del entorno de desarrollo**  
  
* Primero se debe lanzar el cluster e ingresar a el como se explica en [Lanzar servidor](#como-se-despliega-el-cluster)  
  
* Luego, se copiaran los archivos desde la máquina local al servidor EMR.  
![image text](img/Copiar_datasets1.png)  
![image text](img/Copiar_datasets2.png)  
![image text](img/Copiar_datasets3.png)  
  
* Por ultimo, se copian los archivos locales al servidor hdfs (HUE).  
![image text](img/Cop%C3%ADar_locales_a_emr.png)  
![image text](img/Cop%C3%ADar_locales_a_emr2.png)  
  
---

### **2.1. Ejecución del wordcount via linea de comandos**  

* En la linea de comandos se copia el siguiente comando `pyspark`  
![image text](img/Conexi%C3%B3n_pyspark_nodo_master_via_linea_comandos.png)  
  
* Se procede a realizar la ejecución del wordcount donde se ejecutan los siguientes comandos  
    ```python  
        files_rdd = sc.textFile("hdfs:///datasets/gutenberg-small/*.txt")
        files_rdd = sc.textFile("s3://st0263datasets/gutenberg-small/*.txt")
        wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
        wc = wc_unsort.sortBy(lambda a: -a[1])
        for tupla in wc.take(10):
            print(tupla)
        wc.saveAsTextFile("hdfs:///tmp/wcout1")
    ```  
    En la imagen se muestra como se realizaria en linea de comandos. En este caso la salida del programa se guarda en diferentes archivos  
    ![image text](img/Ejemplos_python_de_forma_interactiva_pyspark.png)  
    ![image text](img/pyspark_guardar_archivo_por_rdd.png)  

    Adicionalmente se muestra la forma en que se guarda la salida del programa en un solo archivo  
    ```python  
        files_rdd = sc.textFile("hdfs:///datasets/gutenberg-small/*.txt")
        files_rdd = sc.textFile("s3://st0263datasets/gutenberg-small/*.txt")
        wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
        wc = wc_unsort.sortBy(lambda a: -a[1])
        for tupla in wc.take(10):
            print(tupla)
        wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout2") #Esta linea es la que se cambia
    ```  
    ![image text](img/Ejemplos_python_de_forma_interactiva_pyspark2.png)  
    ![image text](img/pyspark_guardar_un_solo_archivo_salida.png)  
    ![image text](img/pyspark_guardar_un_solo_archivo_salida2.png)  

--- 
      
### **2.2 Ejecutar el wordcount desde un archivo python**  
  
* Se crea un archivo pyhton como se muestra a continuación  
![image text](img/pyspark_como_archivo_python.png)  
  
* Se ejecuta el archivo de python usando el siguiente comando `spark-submit --master yarn --deploy-mode cluster wc-pyspark.py`  
![image text](img/Correr_archivo_pyspark.png)  

* Se verifica que se creo el archivo que contiene la salida del programa  
![image text](img/verificar_archivo_pyspark.png)  
![image text](img/verificar_archivo_pyspark2.png)  
  
---
  
### **2.3 Ejecutar el wordcount desde Zeppelin notebook**  
  
* Se crea un notebook en zeppelin  
![image text](img/zeppelin_crear_notebook.png)  
![image text](img/zeppelin_crear_notebook2.png)  
  
* Se copia en el notebook las siguientes lineas  
    ```python
        %spark2.pyspark
        # WORDCOUNT COMPACTO
        #files_rdd = sc.textFile("s3://datamazapataj/datasets/gutenberg-small/*.txt")
        files_rdd = sc.textFile("hdfs:/user/hadoop/datasets/gutenberg-small/*.txt")
        wc_unsort = files_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
        wc = wc_unsort.sortBy(lambda a: -a[1])
        for tupla in wc.take(10):
            print(tupla)
        wc.coalesce(1).saveAsTextFile("hdfs:///tmp/wcout4")
    ```  
  
* Se corre y en zeppelin se muestra cual es la salida  
![image text](img/Resultado.png)  
  
* Finalmente, se verifica que el archivo se haya guardado de manera correcta  
![image text](img/verifica_que_se_guardo.png)  
![image text](img/verifica_que_se_guardo2.png)  
  
---  
  
### **2.4 Ejecutar el wordcount desde Jupyter notebook en EMR**  
  
**WordCount en una sola sección**
  
* Lo primero que se hacer es iniciar la aplicación spark y verificar que el contexto esta correcto  
![image text](img/Inicio_aplicacion_spark_y_verifricar_contexto.png)  
  
* Despues se copian las siguientes lineas en una sección del notebook, para luego ejecutarse  
![image text](img/jupyter_wc_compacto.png)  
Aqui podemos corroborar que el archivo se guardo de manera adecuada  
![image text](img/jupyter_wc_compacto2.png)  
![image text](img/jupyter_wc_compacto3.png)  
  
**WordCount paso a paso**  
  
* Primero se leera el archivo con el cual se realizara el conteo de palabras  
![image text](img/jupyter_wc_paso_a_paso.png)  
  
* Luego, se realizara un split para obtener cada letra del texto  
![image text](img/jupyter_wc_paso_a_paso2.png)  
  
* Se realiza un análisis para determinar cuantas veces aparece la letra en el texto  
![image text](img/jupyter_wc_paso_a_paso3.png)  
  
* A continuación se realizan dos operaciones para organizar las letras dependiendo de unas keys ya establecidas  
![image text](img/jupyter_wc_paso_a_paso4.png)  
![image text](img/jupyter_wc_paso_a_paso5.png)  
  
* Se guarda la salida del programa en un solo archivo  
![image text](img/jupyter_wc_paso_a_paso6.png)  
  
* Se corrobora que el archivo quedo guardado. Para esto se verifica primero en HUE y luego en el servicio S3 de AWS  
![image text](img/jupyter_wc_paso_a_paso7.png)  
![image text](img/jupyter_wc_paso_a_paso8.png)  
![image text](img/jupyter_wc_paso_a_paso9.png)  

---  

### **2.5 Replicación y ejecucion del notebook "Data_processing_using_PySpark.ipynb"**  
  
* Primero se importa la libreria SparkSesion para iniciar la aplicación spark  
![image text](img/Data_procesing_importar_sparksesion_para_iniciar_aplicacion_spark.png)  
  
* Se crea un objeto de SparkSesion  
![image text](img/Data_procesing_importar_sparksesion_para_crear_objeto_de_sesion_spark.png)  
  
* Se carga el dataframe con el cual se realizaran todas las operaciones y análisis  
![image text](img/Data_procesing_importar_sparksesion_para_cargar_archivo_csv.png)  
  
* Se dan a conocer los nombres de las columnas que tiene el dataframe  
![image text](img/Data_procesing_importar_sparksesion_para_conocer_el_nombre_columnas.png)  
  
* Se determina el número de columnas que tiene el dataframe  
![image text](img/Data_procesing_importar_sparksesion_para_conocer_numero_columnas.png)  
  
* Se determina el número de registros o filas que tiene el dataframe  
![image text](img/Data_procesing_importar_sparksesion_para_conocer_numero_de_filas_o_registros.png)  
  
* Se imprime el número de columnas y filas que tiene el dataframe  
![image text](img/Data_procesing_importar_sparksesion_para_conocer_cuantas_filas_y_columnas_tiene.png)  
  
* Se muestra la estructua o esquema que tiene el dataframe. De esta manera se determina el tipo de dato de cada columna respectivamente  
![image text](img/Data_procesing_importar_sparksesion_para_conocer_composicion_del_squema.png)  
  
* Se muestran solo la cantidad de filas que se indique  
![image text](img/Data_procesing_importar_sparksesion_para_mostrar_alguna_cantidad_determinada_de_registros.png)  
  
* Se muestra solamente las columnas que se indiquen. Ademas, solo se muestran la cantidad de registros que se indique  
![image text](img/Data_procesing_importar_sparksesion_para_filtrar_y_mostrar_una_cantidad_determinada_registros.png)  
  
* Se muestra información general del dataframe  
![image text](img/Data_procesing_importar_sparksesion_para_mostrar_info_del_conjunto_datos.png)  
  
* Luego de terminar los pasos anteriores se procede a importar los tipos de datos que se manejan en MySQL  
![image text](img/Data_procesing_importar_sparksesion_para_importar_tipos_de_datos_sql.png)  
  
* Se realiza una estimación de cuanta edad tendra en 10 años y se muestra agrgando una columna en la visualización donde cada registro se le asigna la edad que tendra en 10 años  
![image text](img/Data_procesing_importar_sparksesion_para_agregar_columna_realizando_una_estimaci%C3%B3n.png)  
  
* Se realiza una conversión de la edad que esta en entero a decimal y se muestra con una columna adicional en la visualización  
![image text](img/Data_procesing_importar_sparksesion_para_agregar_columna_mostrando_la_edad_como_decimal.png)  
  
* Se realiza un filtro por un valor determinado de una columna  
![image text](img/Data_procesing_importar_sparksesion_para_realizar_filtro.png)  
  
* Se realiza un filtro por un valor determinado de ua columna y se muestran solo algunas columnas. Las que se especifican  
![image text](img/Data_procesing_importar_sparksesion_para_realizar_filtro_y_solo_mostrar_unas_columnas_determinadas.png)  
  
* Se realiza un filtro con multiples condiciones y luego se muestra el resultado  
![image text](img/Data_procesing_importar_sparksesion_para_realizar_multiples_filtros.png)  
![image text](img/Data_procesing_importar_sparksesion_para_realizar_multiples_filtros_alternativa.png)  
  
* Se muetran los valores de una columna pero sin repetirse  
![image text](img/Data_procesing_importar_sparksesion_para_mostrar_columnas_sin_valores_repetidos.png)  
  
* Se indica cuantos valores no repetidos tiene una columna  
![image text](img/Data_procesing_importar_sparksesion_para_conocer_los_valores_que_tiene_una_columna_sin_repetidos.png)  
  
* Primero se agrupan los registros dependiendo de un valor de una determinada columna. Luego se indica cuantos registros tiene cada valor de la columna  
![image text](img/Data_procesing_importar_sparksesion_para_conocer_cuantos_registros_cumplen_con_un_valor_de_una_columna.png)  
  
* Primero se agrupan los registros dependiendo de un valor de una determinada columna. Luego se realiza un promedio de cada valor de cada columna siempre teniendo como base la columna por la cual se agrupo.  
![image text](img/Data_procesing_importar_sparksesion_agrupar_por_valores_celulares_determinar2.png)  
  
* Primero se agrupan los registros dependiendo de un valor de una determinada columna. Luego se suman los valores de cada columna teniendo como base la columna por la cual se agrupo  
![image text](img/Data_procesing_importar_sparksesion_agrupar_por_valores_celulares_determinar1.png)  
  
* Primero se agrupan los registro por una columna. Luego se encuentra el valor maximo  
![image text](img/Data_procesing_importar_sparksesion_agrupar_por_valores_celulares_determinar_max.png)  
  
* Primero se agrupan los registro por una columna. Luego se encuentra el valor minimo  
![image text](img/Data_procesing_importar_sparksesion_agrupar_por_valores_celulares_determinar_mIN.png)  
  
* Primero se agrupan los registros por una columna y luego se realiza una suma de los valores correspondientes pero con una sola columna que se le indica  
![image text](img/Data_procesing_importar_sparksesion_agrupar_col_es.png)  
  
* Se procede a importar UDF  
![image text](img/udf_importar.png)  
  
* Se crea una función de python que permite determinar el precio de una marca  
![image text](img/udf_determinar_precio_marca.png)  
  
* Se crea un udf usando python. Luego se añade una columna a el dataframe para donde se determina el precio de cada marca usando la función de python  
![image text](img/udf_crear_udf_para_determinar_precio_usando_funcion_python.png)  
  
* Usando una función lambda se determina si la persona es adulta o joven  
![image text](img/udf_usando_lambda_determinar_si_es_adulto_o_joven.png)  
  
* Se importa pandas udf  
![image text](img/panda_udf_importar.png)  
  
* Se crea una función para determinar cuantos años quedan de vida  
![image text](img/panda_udf_determinar_a%C3%B1os_faltantes.png)
  
* Observar cauntos valores duplicados hay  
![image text](img/udf_cant_registros_inlcuyendo_duplicados.png)  
  
* Quitar valores duplicados a la hora de contar cuantos registros hay  
![image text](img/udf_cant_registros_sin_duplicados.png)  
  
* Quitar una columan de un dataframe  
![image text](img/udf_remover_una_columna.png)
  
* Guardar archivo csv en un bucket  
![image text](img/udf_guardar_nuevo_csv_sin_una_columna.png)  
![image text](img/udf_guardar_nuevo_csv_sin_una_columna2.png)  
  
* Guardar archivo csv al cual se le quito una columa en el bucket  
![image text](img/udf_guardar_nuevo_csv_modificado.png)  
![image text](img/udf_guardar_nuevo_csv_modificado2.png)  
  
* Guardar archivo en formato parquet  
![image text](img/udf_guardar_nuevo_csv_en_formato_parquet.png)  
  
---

### **2.6 HIVE y SparkSQL. Gestión (DDL) y Consultas (DQL)**  
  
1. Primero hay que situarse en la sección HIVE  
![image text](img/Hive.png)  
  
2. Crear tabla hdi  
    ```SQL  
        use usernamedb;
        CREATE EXTERNAL TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
        ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
        STORED AS TEXTFILE 
        LOCATION 's3://datamazapataj/onu/hdi/'
    ```  
    ![image text](img/Crear_tabla_hdi.png)  
  
3. Mostrar las tablas que se han creado `show tables;`  

![image text](img/Mostrar_tablas.png)  
  
4. Mostrar la información de cada tabla  `describe hdi;`  

![image text](img/Describir_tabla.png)  
  
5. Mostrar el contenido de una tabla `select * from hdi;`  

![image text](img/select_todo.png)  
  
6. Mostrar ciertas columnas y realizar filtro `select country, gni from hdi where gni < 2000;`  

![image text](img/select.png)  
  
7. Crear tabla para realizar un join despues  
    ```SQL  
        use usernamedb;
        CREATE EXTERNAL TABLE EXPO (country STRING, expct FLOAT) 
        ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
        STORED AS TEXTFILE 
        LOCATION 's3://datamazapataj/datasets/onu/export/'
    ```  
    ![image text](img/tabla_expo.png)  
      
8. Realizar JOIN `SELECT h.country, gni, expct FROM HDI h JOIN EXPO e ON (h.country = e.country) WHERE gni > 2000;`  

![image text](img/join.png)  
  
9. Crear tabla que contenga un texto al cual se le realizara un conteo de palabras  
    ```SQL
        use usernamedb;
        CREATE EXTERNAL TABLE docs (line STRING) 
        STORED AS TEXTFILE 
        LOCATION 'hdfs:///user/hadoop/datasets/gutenberg-small/';
    ```  
    ![image text](img/tabla_wc.png)  
      
10. Conteo de palabras ordenado por palabra `SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w GROUP BY word ORDER BY word DESC LIMIT 10;` 

![image text](img/Ordenar_palabra.png)  
  
11. Ordenado por frecuencia `SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w GROUP BY word ORDER BY count DESC LIMIT 10;`  

![image text](img/ordenar_freceuncia_mayor_menor.png)  
  
---  
  
## **3. Descripción del ambiente de ejecución: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**  
  
## **Como se despliega el cluster**  
  
1. Se ingresa al servicio EMR que proporciona AWS  
![image text](img/Buscar_emr.png)  
  
2. Dado que ya se habian creado cluster, lo unico que se hace es clonar uno existente  
![image text](img/Clonar_cluster1.png)  
![image text](img/Clonar_cluster2.png)  
![image text](img/Clonar_cluster3.png)  
  
3. Luego se espera a que el cluster se inicie  
![image text](img/Clonar_cluster.png)  
![image text](img/Verifica_creacion.png)  
  
4. Por ultimo se ingresa via ssh  
![image text](img/comando_para_ingresar.png)  
![image text](img/ingreso_cluster.png)
  
---
  
## **4. Referencias**  
  
* [GitHub de la materia](https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata/03-spark)  
* [Documentación de AWS](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-scoped-libraries.html)
  
  
