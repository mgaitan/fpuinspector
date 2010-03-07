#!/usr/bin/env python
# -*- coding: utf-8 -*- 


def F2XM1():
	pass


def FABS():
	pass

# Operaciones de Adición
"""
Operaciones de adición
Opcode Instruction Description
D8 C0+i FADD ST(0), ST(i)Add ST(0) to ST(i) and store result in ST(0)
DC C0+i FADD ST(i), ST(0)Add ST(i) to ST(0) and store result in ST(i)
DE C0+i FADDP ST(i), ST(0) Add ST(0) to ST(i), store result in ST(i), and pop the
 register stack
DE C1 FADDP Add ST(0) to ST(1), store result in ST(1), and pop the

"""

#FADD
def FADD(st0=0,sti=1):
    pass

#FADDP
def FADDP(sti=1,st0=0):
    pass
    
"""
Opcode  Instruction        Description
D8 E0+i FSUB ST(0), ST(i)  Subtract ST(i) from ST(0) and store result in ST(0)
DC E8+i FSUB ST(i), ST(0)  Subtract ST(0) from ST(i) and store result in ST(i)
DE E8+i FSUBP ST(i), ST(0) Subtract ST(0) from ST(i), store result in ST(i), and pop
                           register stack
DE E9   FSUBP              Subtract ST(0) from ST(1), store result in ST(1), and pop
                           register stack

"""

def FSUB(st0=0,sti=1):
	pass
    
def FSUBP(st0=0,sti=1):
	pass

#Operaciones de Signo

def FCHS():
	pass
    
def FNCLEX():
	pass


#Operaciones de Comparación
"""
Opcode  Instruction   Description
D8 /2   FCOM m32real  Compare ST(0) with m32real.
DC /2   FCOM m64real  Compare ST(0) with m64real.
D8 D0+i FCOM ST(i)    Compare ST(0) with ST(i).
D8 D1   FCOM          Compare ST(0) with ST(1).
D8 /3   FCOMP m32real Compare ST(0) with m32real and pop register stack.
DC /3   FCOMP m64real Compare ST(0) with m64real and pop register stack.
D8 D8+i FCOMP ST(i)   Compare ST(0) with ST(i) and pop register stack.
D8 D9   FCOMP         Compare ST(0) with ST(1) and pop register stack.
DE D9   FCOMPP        Compare ST(0) with ST(1) and pop register stack twice.
"""

def FCOM(sti):
	pass

def FCOMP(sti):
	pass
    
def FCOMPP():
	pass

#Operaciones sobre st0

def FCOS():
    pass



"""
Opcode Instruction Description
D9 FE  FSIN        Replace ST(0) with its sine.
"""
def FSIN():
    pass

"""
Opcode Instruction Description
D9 FB  FSINCOS     Compute the sine and cosine of ST(0); replace ST(0) with
                   the sine, and push the cosine onto the register stack.

"""
def FSINCOS():
    pass

"""
Opcode Instruction Description
D9 FA  FSQRT       Calculates square root of ST(0) and stores the result in
                   ST(0)
"""
def FSQRT():
	pass
    
"""
Opcode  Instruction        Description
D8 F0+i FDIV ST(0), ST(i)  Divide ST(0) by ST(i) and store result in ST(0)
DC F8+i FDIV ST(i), ST(0)  Divide ST(i) by ST(0) and store result in ST(i)
DE F8+i FDIVP ST(i), ST(0) Divide ST(i) by ST(0), store result in ST(i), and pop the
                           register stack
"""
def FDIV (st0,sti):
	pass
    
def FDIVP (sti,st0):
	pass

#Operaciones de liberación de cabeza de pila
def FFREE():
	pass
    
def FLD(num):
    pass

"""
Opcode Instruction Description
D9 E8  FLD1        Push +1.0 onto the FPU register stack.
D9 E9  FLDL2T      Push log210 onto the FPU register stack.
D9 EA  FLDL2E      Push log2e onto the FPU register stack.
D9 EB  FLDPI       Push π onto the FPU register stack.
D9 EC  FLDLG2      Push log102 onto the FPU register stack.
D9 ED  FLDLN2      Push loge2 onto the FPU register stack.
D9 EE  FLDZ        Push +0.0 onto the FPU register stack.
"""

def FLD1():
    pass

def FLDL2T():
	pass
    
def FLDL2E():
	pass
    
def FLDPI():
	pass
    
def FLDLG2():
	pass
    
def FLDLN2():
	pass
    
def FLDZ():
	pass
    
"""
Opcode  Instruction  Description
D9 /2   FST m32real  Copy ST(0) to m32real
DD /2   FST m64real  Copy ST(0) to m64real
DD D0+i FST ST(i)    Copy ST(0) to ST(i)
D9 /3   FSTP m32real Copy ST(0) to m32real and pop register stack
DD /3   FSTP m64real Copy ST(0) to m64real and pop register stack
DB /7   FSTP m80real Copy ST(0) to m80real and pop register stack
DD D8+i FSTP ST(i)   Copy ST(0) to ST(i) and pop register stack
"""

def FST(mreal):
	pass

def FSTP(mreal):
	pass
    
#incrementa TOP de status
def FINCSTP():
	pass
