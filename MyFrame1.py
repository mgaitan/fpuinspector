# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sat Feb 27 05:22:08 2010

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.labelInput = wx.StaticText(self, -1, "Entrada")
        self.inputTxt = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB|wx.TE_MULTILINE)
        self.button_1 = wx.Button(self, -1, "Ejecutar")
        self.labelOutput = wx.StaticText(self, -1, "Salida")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.labelStack = wx.StaticText(self, -1, "Pila", style=wx.ALIGN_CENTRE)
        self.label_1 = wx.StaticText(self, -1, "ST0")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_1_copy = wx.StaticText(self, -1, "ST1")
        self.text_ctrl_2_copy = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_1_copy_1 = wx.StaticText(self, -1, "ST2")
        self.text_ctrl_2_copy_1 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_1_copy_2 = wx.StaticText(self, -1, "ST3")
        self.text_ctrl_2_copy_2 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_1_copy_3 = wx.StaticText(self, -1, "ST4")
        self.text_ctrl_2_copy_3 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_1_copy_4 = wx.StaticText(self, -1, "ST5")
        self.text_ctrl_2_copy_4 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_1_copy_5 = wx.StaticText(self, -1, "ST6")
        self.text_ctrl_2_copy_5 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_1_copy_6 = wx.StaticText(self, -1, "ST7")
        self.text_ctrl_2_copy_6 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_2 = wx.StaticText(self, -1, "Registro de Control")
        self.text_ctrl_3 = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.label_4 = wx.StaticText(self, -1, "X", style=wx.ALIGN_CENTRE)
        self.label_4_copy = wx.StaticText(self, -1, "X", style=wx.ALIGN_CENTRE)
        self.label_4_copy_copy = wx.StaticText(self, -1, "X", style=wx.ALIGN_CENTRE)
        self.label_4_copy_copy_1 = wx.StaticText(self, -1, "RC1", style=wx.ALIGN_CENTRE)
        self.label_4_copy_copy_2 = wx.StaticText(self, -1, "RC0", style=wx.ALIGN_CENTRE)
        self.label_4_copy_copy_2_copy = wx.StaticText(self, -1, "PC1", style=wx.ALIGN_CENTRE)
        self.label_4_copy_copy_2_copy_1 = wx.StaticText(self, -1, "PC0", style=wx.ALIGN_CENTRE)
        self.label_3 = wx.StaticText(self, -1, "Registro de estado")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.ejectutar, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle("frame_2")
        self.inputTxt.SetFocus()
        self.label_4_copy_copy_1.SetToolTipString("Control de redondeo")
        self.label_4_copy_copy_2.SetToolTipString("Control de redondeo")
        self.label_4_copy_copy_2_copy.SetToolTipString(u"Control de precisión")
        self.label_4_copy_copy_2_copy_1.SetToolTipString(u"Control de precisión")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(2, 16, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(8, 2, 0, 0)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(self.labelInput, 0, 0, 0)
        sizer_5.Add(self.inputTxt, 0, wx.EXPAND, 0)
        sizer_5.Add(self.button_1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_5.Add(self.labelOutput, 0, 0, 0)
        sizer_5.Add(self.text_ctrl_1, 0, wx.EXPAND|wx.ALIGN_RIGHT, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add((8, 20), 0, 0, 0)
        sizer_7.Add(self.labelStack, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1_copy, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2_copy, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1_copy_1, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2_copy_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1_copy_2, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2_copy_2, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1_copy_3, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2_copy_3, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1_copy_4, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2_copy_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1_copy_5, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2_copy_5, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_1_copy_6, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2_copy_6, 0, wx.EXPAND, 0)
        sizer_7.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_2.Add(self.label_2, 0, 0, 0)
        sizer_9.Add(self.text_ctrl_3, 0, 0, 0)
        grid_sizer_2.Add(self.label_4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.label_4_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.label_4_copy_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.label_4_copy_copy_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.label_4_copy_copy_2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.label_4_copy_copy_2_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.label_4_copy_copy_2_copy_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_8.Add(self.label_3, 0, 0, 0)
        sizer_1.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

    def InputProc(self, event): # wxGlade: MyFrame1.<event_handler>
        print self.inputTxt.GetValue()
        event.Skip()

    def ejectutar(self, event): # wxGlade: MyFrame1.<event_handler>
        print "Event handler `ejectutar' not implemented"
        event.Skip()

# end of class MyFrame1


