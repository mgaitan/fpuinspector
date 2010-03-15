from ctypes import *
 
# load the shared object
lib = cdll.LoadLibrary('./libfld.so.1.0')

def getpila():
    space = c_double * 8
    pila = space()
    ok = lib.get_pila(pila)
    for valor in pila:
        print valor

def fld(val):
    n = c_double(val)
    lib.fld(n)


if __name__ == '__main__':
    getpila()
    fld(5)
    fld(3)
    fld(3.74534556546)
    lib.fadd()
    getpila()
