# -*- coding: utf-8 -*-
from ctypes import cdll #para interfaz con C
import platform #para detectar sistema operativo
import inspect #para generar las instrucciones válidas


class Wrapper:
    def __init__(self):
        # load the shared object
        if platform.system()=='Linux':
            self.lib = cdll.LoadLibrary('./libregistros.so.1.0')
        elif platform.system()=='Windows':
            self.lib = cdll.LoadLibrary('./libregistros.dll') #TODO
    
    def get_control(self):
        return self.lib.get_control()
    
    def get_estado(self):
        return self.lib.get_estado()
    
    def get_st0(self):
        """retorna el valor de la cabecera de la pila ST"""
        return self.lib.get_st0()

        
    def reset(self):
        self.lib.reset()
    
    ##### INSTRUCCIONES IMPLEMENTADAS ######
    
    def FINIT(self,run=True):
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
            self.lib.fld(n)

    def FCOM(self, n=0, run=True):
        """FCOM compares ST0 with the given operand, and sets the FPU flags accordingly. ST0 is treated as the left-hand side of the comparison, so that the carry flag is set (for a "less-than"  result) if ST0 is less than the given operand. """
        if run:
            self.lib.fcom(n)

    def FXCH(self, n=0, run=True):
        """FXCH exchanges ST0 with a given FPU register. The no-operand form exchanges ST0 with ST1."""
        if run:
            self.lib.fxch(n)

    def FADDP(self, n=1, run=True):
        """performs the same function as FADD, but pops the register stack after storing the result."""
        if run:
            self.lib.faddp(n)
    
    def FSUBP(self, n=1, run=True):
        """performs the same function as FSUB, but pops the register stack after storing the result."""
        if run:
            self.lib.fsubp(n)
    
    def FSINCOS(self, run=True):
        """FSINCOS does the same, but then pushes the cosine of the same value on the register stack, so that the sine ends up in ST1 and the cosine in ST0."""
        if run:
            self.lib.fsincos()

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
    def is_valid(self,line):
        """se fija si la instrucción ingresada es válida"""
        line.replace(',',' ')
        commlista = line.split()
        comm = commlista[0]
        params = commlista[1:]
        
        paramline = "("
        i=0
        for p in params:
            if i>0:
                paramline+=", "
            paramline+=str(p)
            i+=1
        paramline += "run=False)"
        commline = "self."+comm + paramline
        #print commline
        try:
            #run=False just check the call is right but do nothing
            exec commline 
            return True
        except:
            return False



