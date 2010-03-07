from ctypes import *
 
# load the shared object
lib = cdll.LoadLibrary('./libregistros.so.1.0')
