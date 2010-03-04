from ctypes import *
 
# load the shared object
libtest = cdll.LoadLibrary('./libregistros.so.1.0')

def int2bin(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be positive"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

#libtest.fpuInit()

reg_control = libtest.getControl() 
reg_estado = libtest.getEstado()
reg_st0_1 = libtest.getSt0()
libtest.fpuFfree(c_uint(0))
reg_st0_2 = libtest.getSt0()



print "Registro de control: %i - %s" %  (reg_control,int2bin(reg_control)) 
print "Registro de estado: %i - %s" %  (reg_estado, int2bin(reg_estado))
print "Registro de pila st0: %f %f"  % (reg_st0_1,reg_st0_2)
