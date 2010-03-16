#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
>>> import wrapper
>>> w = wrapper.Wrapper()


Caso de prueba 1: 
- la pila inicialmente tiene valores no númericos

>>> res = w.get_stack() 
[nan, nan, nan, nan, nan, nan, nan, nan]

Caso de prueba 2:
- ingresamos algunos valores al stack mediante FLD

>>> w.FLD(3)
>>> w.FLD(5.0)
>>> w.FLD(18.3)
>>> res = w.get_stack() #doctest: +ELLIPSIS
[18.300..., 5.0, 3.0, nan, nan, nan, nan, nan]

Caso de prueba 3:
- Al pedir la pila consecutivamente los valores deben ser los mismos

>>> res = w.get_stack() #doctest: +ELLIPSIS
[18.300..., 5.0, 3.0, nan, nan, nan, nan, nan]

Caso de prueba:
- Instruccion FADD

>>> w.FADD()
>>> res = w.get_stack() #doctest: +ELLIPSIS
[23.300..., 3.0, nan, nan, nan, nan, nan, nan]


Caso de prueba: Raiz cuadrada

>>> w.FSQRT()
>>> res = w.get_stack() #doctest: +ELLIPSIS
[4.827..., 3.0, nan, nan, nan, nan, nan, nan]


Caso de prueba:
- Almacenar más de 8 valores en la pila

>>> import wrapper
>>> w = wrapper.Wrapper()
>>> for i in range(8):
...     w.FLD(1.0)
... 
>>> w.FLD(2.1)
>>> res = w.get_stack() #doctest: +ELLIPSIS
[2.10..., 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
>>> 




"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
