#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
>>> import wrapper
>>> w = wrapper.Wrapper()

caso de prueba: FLDxx (constantes)

>>> w.FLD1()
>>> w.FLDL2E()
>>> w.FLDL2T()
>>> w.FLDLG2()
>>> w.FLDZ()
>>> w.FLDPI()
>>> res = w.get_stack() #doctest: +ELLIPSIS
[3.14159..., 0.0, 0.30102..., 3.32192..., 1.44269..., 1.0, nan, nan]
"""



if __name__ == '__main__':
    import doctest
    doctest.testmod()
