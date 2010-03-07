#!/usr/bin/env python
# -*- coding: utf-8 -*-
import reduced_instruction_set as iset

def is_valid(line):
    '''checks line for a valid asm sentence'''
    line.replace(',',' ')
    commlista = line.split()
    comm = commlista[0]
    params = commlista[1:]
    #probando una nueva manera de hacer las cosas, con una cadena de texto
    paramline = "("
    i=0
    for p in params:
		if i>0:
			paramline+=", "
		paramline+=str(p)
		i+=1
    paramline += ")"
    commline = "iset."+comm + paramline
    
    
    try:
        exec commline
        return True
    except:
        return False


def int2bin(n):
    '''converts denary integer n to binary list 
    [MSB,....,LSB]
    '''
    b = []
    if n < 0:  raise ValueError, "must be positive"
    if n == 0: return [0]
    while n > 0:
        b.append(n % 2)
        n = n >> 1
    while len(b)<16:
        b.append(0)
    b.reverse()
    return b
