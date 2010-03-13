#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import os



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


def get_svn_revision(path=None):
    rev = None
    if path is None:
        path = os.path.dirname( __file__ )# __path__[0]
    
    entries_path = '%s/.svn/entries' % path

    if os.path.exists(entries_path):
        entries = open(entries_path, 'r').read()
        # Versions >= 7 of the entries file are flat text.  The first line is
        # the version number. The next set of digits after 'dir' is the revision.
        if re.match('(\d+)', entries):
            rev_match = re.search('\d+\s+dir\s+(\d+)', entries)
            if rev_match:
                rev = rev_match.groups()[0]
        # Older XML versions of the file specify revision as an attribute of
        # the first entries node.
        else:
            from xml.dom import minidom
            dom = minidom.parse(entries_path)
            rev = dom.getElementsByTagName('entry')[0].getAttribute('revision')

    if rev:
        return u' SVN-%s' % rev
    return u'1.0'

