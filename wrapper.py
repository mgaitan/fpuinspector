# -*- coding: utf-8 -*-

""" 
Interfaz con la biblioteca dinámica C que es un intermediario hacia rutinas de ensamblador  
Cada instrucción de FPU implementada en bajo nivel tiene su acceso desde un objeto Wrapper


Desacople en dos procesos
-------------------------

Para mantener la coherencia del estado interno del procesador, un objeto Wrapper()
se gestiona a través de un proxy de multiproceso, del paquete multiproccess 
incorporado en Python 2.6

Del módulo MainFrame podemos ver:


  ``
    import Wrapper
    from multiprocessing.managers import BaseManager

    class MyManager(BaseManager):
        pass
    MyManager.register('Wrapper', Wrapper)    
    
    manager = MyManager()  
    manager.start()        
    lib = self.manager.Wrapper() ``
    

self.lib es un objeto wrapper, que tiene acceso a todo los métodos de este objeto
pero interfaseado por el objeto manager, que es, en efecto, otro proceso. 

De esta manera el objeto wrapper mantiene una coherencia persistente del estado 
del FPU y el programa en general (con su GUI, que al menos en linux realiza numerosos cálculos
de punto flotante) otro. 

Es el sistema operativo el encargado de entregar a cada proceso su estado previo
cuando el CPU le es asignado, permaneciendo inmune a la interferencia que producen
dos tareas de un mismo proceso.

Brillante esta tarjeta!

Introspección
-------------

Python es un lenguaje interpretado por lo que va 'compilando' a medida que necesita
Esto le permite maneter un total conocimiento de qué es lo que está ejecutando
porque conoce el código. 

También hay una distinción entre cadenas de documentación (en general, cada entididad
como Clase, método o función debería tener un string inmediatamente después que la
describa). 

A través de la introspección se puede conocer cuales son los métodos que efectivamente
existen en el código y recuperar sus cadenas de documentación. 
Eso es lo que hace el método get_valid_instructions(): devuelve todos los métodos
que comienzan con *F* (efe mayúscula, como empiezan todas las instrucciones 
de ensamblador de la FPU) y su descripción, que es la línea 
entre comilla justo debajo de la definición de cada una. 

Esta lista de instrucciones es la que se despliega al usuario como opciones 
válidas para que este ingrese y ejecute. A su vez, su descripción (la cadena
de documentación) se asocia en la interfaz como ToolTip de cada fila de la 
lista de instrucciones 

Con esto tenemos al menos dos ventajas: manetenemos homogeneidad total entre
lo que se mostrará al usuario (la lista de instrucciones válidas implementadas)
con lo que verdaderamente está disponible en el código, y por otro lado
manetenemos el código debidamente comentado y brindamos mejor usabilidad al usuario
sin doble trabajo!

Validación de Instrucciones
---------------------------
El método *run_or_test_instruction* verifica que la intrucción que el usuario
ingresa y posteriormente se ejecutará (se enviará a C y a través de este a ASM)
sea válida. 

Para eso utiliza una forma, no poco ingeniosa, idea de Leonardo Rocha en su 
_fpu8087sim

Se basa en la sentencia `exec` que permite recibir una "cadena de caracteres" 
y la intenta ejecutar como código python. Si la ejecución es exitosa, quiere 
decir que lo que el usuario ingresó es válido. 

Para evitar que efectivamente se ejecute sobre la FPU una intrucción cuando se 
ingresa, en modo Test se agrega una bandera `run=False`. Cada método de intrucción
verifica esta bandera y en caso de ser falso, no realiza ninguna operación. 

Ejemplo de flujo: 

#.  El usuario ingresa 'FINIT'
#.  El método convierte esta cadena a `self.FINIT( run=False)` e intenta ejecutarlo
#.  Como el metodo FINIT(run=False) no existe en el contexto de la clase Wrapper
    el resultado de la ejecución desencadenará una excepción que se canaliza
    en el `except` y devuelve False, indicando que la intrucción no es válida

Otro ejemplo:

#.  El usuario ingresa 'FLD 3.1416'
#.  El método convierte la cadena a `self.FLD(3.1416, run=False)` y ejecuta
#.  Como el método está definido y los parámetros son válidos, el resultado es 
    verdadero. 

Este mismo método es el que invoca actionRunNext (en MainFrame.py) pero con 
run=True para ejecutar efectivamente las intrucciones. 




.. _fpu8087sim : http://code.google.com/p/fpu8087sim
"""


from ctypes import * #para interfaz con C
import platform #para detectar sistema operativo
import inspect #para generar las instrucciones válidas
import os

import pickle

class Wrapper:
    def __init__(self):
        if platform.system()=='Linux':
            self.lib = cdll.LoadLibrary('%s/libfpu.so.1.0' % os.path.abspath(os.path.dirname(__file__)) ) # % os.path.dirname( __file__ ))
        elif platform.system()=='Windows':
            self.lib = cdll.WinDLL('%s/libfpu.dll' % os.path.abspath(os.path.dirname(__file__)) ) #TODO
        
        
    def get_control(self):
        return self.lib.get_control()
    
    def get_estado(self):
        return self.lib.get_estado()
    

    def set_stack_from_file(self):
        fh = open('stack.tmp', 'r')
        stack = pickle.load(fh)
        set_stack(stack)
        fh.close()
    
    def get_stack_to_file(self):
        stack = [v for v in self.get_stack()]
        fh = open('stack.tmp', 'w')
        stack = pickle.dump(stack, fh)
        fh.close()


    def get_stack(self):
        """retorna un array con los valores del stack"""
        space = c_double * 8
        pila = space()
        ok = self.lib.get_pila(pila)
        self.set_stack(pila)
        return [val for val in pila] 
    
    def set_stack(self, stack):
        pila_al_vesre = []   
        for valor in stack:
            #print valor
            pila_al_vesre.insert(0,valor) #invierto el iterable en una lista
        for valor in pila_al_vesre:
            self.FLD(valor)
        

    def reset(self):
        self.lib.reset()
    
    ##### INSTRUCCIONES IMPLEMENTADAS ######
    
    def _FINIT(self,run=True):
        #not necessary
        """initialises the FPU to its default state. It flags all registers as empty, although it does not actually change their values. """
        if run:
            self.lib.finit()    

    def FFREE(self, n=0, run=True):
        """FFREE marks the given register as being empty."""
        if run:
            self.lib.ffree(n)
            
    def FLD(self, n=0.0, run=True):
        """loads a floating-point value out of the given register or memory location, and pushes it on the FPU register stack"""
        if run:
            self.lib.fld(c_double(n))

    def _FLDCW(self, n, run=True):
        #no devuelve el valor esperado
        """FLDCW loads a 16-bit value out of memory and stores it into the FPU control word (governing things like the rounding mode, the precision, and the exception masks)."""
        if run:
            self.lib.fldcw(c_int(n))



    def FLD1(self, run=True):
        if run:
            self.lib.fld1()

    def FLDL2E(self, run=True):
        if run:
            self.lib.fldl2e()

    def FLDL2T(self, run=True):
        if run:
            self.lib.fldl2t()

    def FLDLG2(self, run=True):
        if run:
            self.lib.fldlg2()

    def FLDLN2(self, run=True):
        if run:
            self.lib.fldln2()

    def FLDPI(self, run=True):
        if run:
            self.lib.fldpi()

    def FLDZ(self, run=True):
        if run:
            self.lib.fldz()



    def FCOM(self, n=0, run=True):
        """FCOM compares ST0 with the given operand, and sets the FPU flags accordingly. ST0 is treated as the left-hand side of the comparison, so that the carry flag is set (for a "less-than"  result) if ST0 is less than the given operand. """
        if run:
            self.lib.fcom(n)

    def FXCH(self, n=0, run=True):
        """FXCH exchanges ST0 with a given FPU register. The no-operand form exchanges ST0 with ST1."""
        if run:
            self.lib.fxch(n)


    def FCLEX(self, run=True):
        """FCLEX clears any floating-point exceptions which may be pending."""
        if run:
            self.lib.fclex()
            
    def FCHS(self, run=True):
        """FCHS negates the number in ST0: negative numbers become positive, and vice versa.  """
        if run:
            self.lib.fabs_()


    def FABS(self, run=True):
        """FABS computes the absolute value of ST0, storing the result back in ST0. """
        if run:
            self.lib.fabs()

    def FPREM(self, run=True):
        """FPREM produce the remainder obtained by dividing ST0 by ST1. """
        if run:
            self.lib.fprem()


    def FSCALE(self, run=True):
        """FSCALE scales a number by a power of two: it rounds ST1 towards zero 
        to obtain an integer, then multiplies ST0 by two to the power of that integer, 
        and stores the result in ST0. """
        if run:
            self.lib.fscale()

    def FADD(self, n=1, run=True):
        """performs the sum between st0 and st1 and stores the result in st0"""
        if run:
            self.lib.fadd()

    def FXTRACT(self, run=True):
        """FXTRACT separates the number in ST0 into its exponent and significand 
        (mantissa), stores the exponent back into ST0, and then pushes the significand 
        on the register stack 
        (so that the significand ends up in ST0, and the exponent in ST1). """
        if run:
            self.lib.fxtract()


    def _FADDP(self, n=1, run=True):
        #not yet implemented
        """performs the same function as FADD, but pops the register stack after storing the result."""
        if run:
            self.lib.faddp(n)


    def FSUB(self, run=True):
        """performs the rest between st0 and st1 and stores the result in st0"""
        if run:
            self.lib.fsub()

    def FMUL(self, run=True):
        """FMUL multiplies ST0 by the given operand, and stores the result in ST0"""
        if run:
            self.lib.fmul()

    def FDIV(self, run=True):
        """FDIV divides ST0 by the given operand and stores the result back in ST0,"""
        if run:
            self.lib.fdiv()


    
    def _FSUBP(self, n=1, run=True):
        #not yet implemented
        """performs the same function as FSUB, but pops the register stack after storing the result."""
        if run:
            self.lib.fsubp(n)
    
    def FSINCOS(self, run=True):
        """FSINCOS does the same, but then pushes the cosine of the same value on the register stack, so that the sine ends up in ST1 and the cosine in ST0."""
        if run:
            self.lib.fsincos()

    def FSIN(self, run=True):
        """FSIN calculates the sine of ST0 (in radians) and stores the result in ST0"""
        if run:
            self.lib.fsin()

    def FCOS(self, run=True):
        """FCOS calculates the cosine of ST0 (in radians) and stores the result in ST0"""
        if run:
            self.lib.fcos()

    def FPTAN(self, run=True):
        """FPTAN computes the tangent of the value in ST0 (in radians), and stores the result back into ST0. """
        if run:
            self.lib.fptan()

    def FPATAN(self, run=True):
        """FPATAN computes the arctangent, in radians, of the result of dividing ST1 by ST0, stores the result in ST1, and pops the register stack"""
        if run:
            self.lib.fpatan()


    def FRNDINT(self, run=True):
        """FRNDINT rounds the contents of ST0 to an integer, according to the current rounding mode set in the FPU control word, and stores the result back in ST0. """
        if run:
            self.lib.frndint()

    def FYL2X(self, run=True):
        """FYL2X multiplies ST1 by the base-2 logarithm of ST0, stores the result in ST1, and pops the register stack (so that the result ends up in ST0). ST0 must be non-zero and positive."""
        if run:
            self.lib.fyl2x()

    def FSQRT(self, run=True):
        """FSQRT calculates the square root of ST0 and stores the result in ST0."""
        if run:
            self.lib.fsqrt()
            
    
    ##### FIN INSTRUCCIONES IMPLEMENTADAS ######            

    def get_valid_instructions(self):
        """
        devuelve un diccionario {instrucción=docstring} para instrucciones 
        válidas basado en la instrospección de los métodos de la clase
        """
        valid_instructions = dict([(a,inspect.getdoc(b))  for (a,b) 
                                    in inspect.getmembers(Wrapper,inspect.ismethod) 
                                    if a[0] == 'F'])
        return valid_instructions


    #HELPERS
    def run_or_test_instruction(self,line, run=False):
        """
        En modo run=False se fija si la instrucción ingresada es válida
        En modo run=True ejecuta la instrucción.
        """
        
        line = line.replace(',',' ')
        commlista = line.split()
        comm = commlista[0]
        params = [c+", " for c in commlista[1:]]
        commline = "self.%s(%s run=%s)" % (comm, "".join(params), run)
        print commline
        try:
            #run=False just check the call is right but do nothing
            exec commline 
            return True
        except:
            return False



