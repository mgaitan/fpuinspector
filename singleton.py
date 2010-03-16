#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

class Singleton(type): 
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)
 
    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args,**kw)
        return cls.__instance


class BufferStack:
    __metaclass__ = Singleton
    def __init__(self):
        self._value = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

 
