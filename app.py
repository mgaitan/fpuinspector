#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Inicializador del programa. Levanta la ventana principal y el entorno
necesario
"""


import wx
from MainFrame import MainFrame

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MainFrame(None, -1, "")
    frame_1.actionRefreshAll()
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
