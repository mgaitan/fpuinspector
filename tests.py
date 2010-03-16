#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
>>> import wrapper
>>> w = wrapper.Wrapper()


Caso de prueba 1): 
- la pila inicialmente tiene valores no númericos

>>> res = w.get_stack() 
[nan, nan, nan, nan, nan, nan, nan, nan]
>>> w.FLD(3)
>>> w.FLD(5.0)
>>> w.FLD(18.3)
>>> res = w.get_stack() #doctest: +ELLIPSIS
[18.3..., 5.0, 3.0, nan, nan, nan, nan, nan]
>>> res = w.get_stack() #doctest: +ELLIPSIS
[18.3..., 5.0, 3.0, nan, nan, nan, nan, nan]
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
