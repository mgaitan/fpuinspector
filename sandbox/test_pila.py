from ctypes import *
 
# load the shared object
lib = cdll.LoadLibrary('./libpila.so.1.0')

def getpila():
    space = c_longdouble * 8
    pila = space()
    ok = lib.get_pila(pila)
    for valor in pila:
        print valor

def fld(val):
    n = c_double(val)
    print n
    lib.fld(n)

if __name__ == '__main__':
    getpila()
    fld(5)
    fld(3)
    getpila()
