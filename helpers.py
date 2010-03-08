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


## {{{ Recipe 440528 (r2): Conversion in base 2 
_nibbles = {"0":"0000", "1":"0001", "2":"0010", "3":"0011",
            "4":"0100", "5":"0101", "6":"0110", "7":"0111",
            "8":"1000", "9":"1001", "A":"1010", "B":"1011",
            "C":"1100", "D":"1101", "E":"1110", "F":"1111",
            "-":"-"}

def toBase2(number):
    """toBase2(number): given an int/long, converts it to
    a string containing the number in base 2."""
    # From a suggestion by Dennis Lee Bieber.
    if number == 0:
        return "0"
    result = [_nibbles[nibble] for nibble in "%X"%number]
    result[number<0] = result[number<0].lstrip("0")
    result.reverse()
    return result
    




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
