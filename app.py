#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Inicializador del programa. Levanta la ventana principal y el entorno
necesario
"""


import wx
import sys

class main():
    def __init__(self):
        self.app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        self.frame_1 = MainFrame(None, -1, "")
        #frame_1.actionRefreshControl(None)
        #frame_1.actionRefreshStatus(None)
        self.frame_1.actionRefreshAll(None)
        self.app.SetTopWindow(self.frame_1)
        self.frame_1.Show()
        self.app.MainLoop()


if __name__ == "__main__":
    try:
        main()
    except NameError:
        print u'FPU Inspector requiere Python 2.6 o superior para funcionar'
