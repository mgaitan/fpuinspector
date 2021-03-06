.. _index


Marco Teórico
=============

Introducción
------------

Una Unidad de Punto Flotante (Floating Point Unit) es un componente de la CPU 
especializado en el cálculo de operaciones en coma flotante. Las operaciones 
básicas que  toda FPU puede realizar son las aritméticas (suma y multiplicación), 
aunque algunos  sistemas más complejos son capaces también de realizar cálculos 
trigonométricos y/o  exponenciales. No todas las CPUs tienen una FPU dedicada. 

En ausencia de FPU, la CPU puede utilizar  programas en micro código para emular 
una función en coma flotante a través de la unidad  aritmético­lógica (ALU), 
la cual reduce el costo del hardware a cambio de una sensible  pérdida de velocidad. 
En algunas arquitecturas, las operaciones en coma flotante se tratan de forma 
completamente  distinta a las operaciones enteras, con registros dedicados y 
tiempo de ciclo diferentes.  Incluso para operaciones complejas, como la división, 
podrían tener un circuito dedicado a  dicha operación. 

Hasta mediados de la década de los 90 del siglo pasado, era común que las CPU no  
incorporasen una FPU en los ordenadores domésticos, sino que eran un elemento 
opcional  conocido como coprocesador en las CPUs.   

Un coprocesador es simplemente una entidad  que trabaja en cooperación con el 
microprocesador de la PC. El objetivo de su utilización es  ganar mejor desempeño 
gracias a la especialización y división del trabajo. Con el tiempo la FPU se 
convirtió en un elemento común presente en la mayoría de  procesadores domésticos 
(series Pentium y PowerPC en adelante). La estructura interna del coprocesador 
matemático se divide en 2 bloques principales, como  se muestra en la Figura 1: 

* **Unidad de Control (CU)**: Se encarga de establecer una interfaz entre el 
    coprocesador y el  bus de datos del sistema. Encargada de supervisar que 
    las instrucciones se ejecuten  correctamente. 

* **Unidad de Ejecución Numérica (NEU)**: Responsable de la ejecución de las 
    instrucciones  del coprocesador.

.. figure:: ./fig1.jpg
   :alt: Arquitectura de la unidad de punto flotante
    
    Arquitectura de la unidad de punto flotante
    
    
La Arquitectura del Coprocesador Matemático
-------------------------------------------

A continuación se expondrá la estructura interna de la Unidad de Punto Flotante.  
Tal como puede apreciarse en el esquema (Figura 1) el coprocesador contiene varios  
registros organizados, cada uno de ellos tiene una funcionalidad distinta: 

* **Pila**: Conjunto de 8 registros de datos estructurados en forma de pila, 
cada uno de éstos  registros contiene los operandos para cada una de las 
instrucciones a ejecutar, como así  también, los resultados obtenidos. 
Cada uno de estos registros son de 80 bits, y los datos se  almacenan en los 
mismos de la siguiente manera:

Es decir, un bit para el signo, 15 para el exponente y los 64 restantes para 
la parte decimal. Ésta pila posee un puntero (ST) que permite el control de la 
misma y la interacción con los  registros del coprocesador. 

* **Registro de estado**: Indica la situación actual de la FPU. Éste es un 
registro de 16 bits cuya  distribución es la siguiente:

.. figure:: ./reg_estado.jpg
    :alt: Registro de Estado
    
    Registro de estado

    
==== ========================================
bit  Descripción
==== ========================================
B    Indica si el coprocesador está ocupado.
C0­C3 Bit del código de condición. 
TOP  Indica la cima de la pila (primer registro activo). 
ES   Bit de resumen de errores. 
SF   Bit de operación invalida. 
PE   Bit de error de precisión.  
UE   Bit de error de underflow (resultado demasiado pequeño para ser representado) 
OE   Bit de error de overflow (resultado demasiado grande para ser representado) 
ZE   Bit de error de división por cero. 
DE   Bit de error de operando no normalizado 
IE   Bit de error de operación invalida. 
==== ========================================
 

* **Registro de control**: Controla la precisión de la FPU y los métodos de redondeo. 
    La distribución de los bits que constituyen éste registro es la siguiente:

.. figure:: ./reg_estado.jpg
    :alt: Registro de Estado
    
    Registro de estado


* **Registro de etiquetas**: Indica el contenido de los 8 registros de datos de la pila. 
Éste es un  registro de 16 bits que contiene 8 etiquetas (cada una de 2 bits). 
Cada etiqueta puede tomar  uno de los cuatro valores posibles: 

== ============
00 Valor válido 
01 Valor cero 
10 Valor inválido o infinito 
11 Vacío 
== ============

* **Registro de punteros de instrucciones**: Guarda las direcciones virtuales 
de las últimas  instrucciones ejecutadas. Registro de 48 bits. 


* **Registro de punteros de datos**:  Guarda las direcciones virtuales de los 
últimos datos  utilizados. Registro de 48 bits. 

* **Registro de código**:  Almacena el código de la última instrucción ejecutada 
    que no sea de  control. Registro de 11 bits. Se construye de la siguiente manera:

.. figure:: ./reg_codigo.jpg
    :alt: Registro de código
    
    Registro de código


