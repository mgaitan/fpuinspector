Requerimientos
==============

Se analizan los requerimientos con el fin de establecer las funcionalidades que 
la aplicación  debe cumplir. En ausencia de un cliente los requisitos han sido 
obtenidos de las consignas  del trabajo final de la asignatura 
**Sistemas de Computación de la Facultad de Ciencias  Exactas, Físicas y 
Naturales de la UNC**, a través de su Profesor Adjunto, *Ing. Miguel Solinas*

Los requerimientos han sido categorizados en los siguientes grupos: Funcionales y No  Funcionales. 
Además para su mejor interpretación se usa las siguiente nemotecnia:  

* Nombre de la aplicación.
* Tipo de requisito.
* ID

Requisitos Funcionales (RFUN)
-----------------------------

La  aplicación  dispondrá  de  los  componentes utilizados en  el funcionamiento 
del coprocesador. ­ ­ ­

* Registro de entrada:  Utilizada para introducir manualmente las instrucciones a  ejecutar. 

* Pila de registros de datos:  Arreglo de registros usado para cargar los operandos  
  que intervienen en la instrucción. 
 
* Registro de estado: Los diferentes bits de estado se actualizaran mediante funciones  
  implementadas que tengan como entrada los resultados obtenidos y como salidas los  
  valores 0 ó 1 para indicar ocurrencia o no. 
  
* Registro de control:  Tras  una instrucción éste registro  se carga  con los  
  valores  correspondientes. 

* Registro de etiquetas: Toma valores de acuerdo al contenido de los registros 
  de la  pila. 

* Registro de código: Su valor varía de acuerdo a la última instrucción ejecutada.

­ ­ ­

Actualización y Visualización de los registros de la FPU: La aplicación muestra   el  estado de los flags y el valor de los registros actualizándolos tras cada operación c) Regreso al estado anterior: La aplicación debe disponer de una opción que permita  volver al estado anterior de la FPU. d) Reset de la FPU: La aplicación debe permitir al usuario la reinicialización de la FPU.  e) Reconocimiento  del set: La FPU debe reconocer con un juego reducido de  instrucciones.


Requisitos No Funcionales (RNFUN)
---------------------------------

* Set de instrucciones reducido: Éste contiene la lista de instrucciones capaz 
    de operar el  simulador del coprocesador matemático. 

* Interfaz gráfica ergonómica: La aplicación contiene una interfaz gráfica 
  de fácil manejo  y didáctica, que permite que la interacción con el mismo sea sencilla. 

* Eficiencia en la ejecución: El software requiere como mínimo para ser ejecutado 
  un  procesador igual o superior al Pentium II con 64Mb de RAM. 
  
* Código abierto: Debido a que el software tiene propósitos educativos se ha 
  optado por  un código abierto, esto da la posibilidad de acceder al código, 
  pudiendo así modificarlo o  adaptarlo según las necesidades del usuario.

  
