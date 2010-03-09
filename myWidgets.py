# -*- coding: utf-8 -*-
#!/usr/bin/env python


import wx

class InstructionListCtrl(wx.ListCtrl):
    """widget List que permite seleccionar y mover filas"""
    
    def __init__(self, parent, ID, pos=wx.DefaultPosition,size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        #self.statusbar = statusbar
        
        
    def get_list(self):
        """devuelve una lista de items de un list control"""
        list = []
        row = []
        for nrow in range(self.GetItemCount()):
            row = []
            for ncol in range(1):
                row.append(self.GetItem(nrow,ncol).GetText())
            list.append(row)
        return list

    
    def get_selected_items(self):
        """
        Gets the selected items for the list control.
        Selection is returned as a list of selected indices,
        low to high.
        """

        selection = []

        # start at -1 to get the first selected item
        current = -1
        while True:
            next = self.GetNextSelected(current)
            if next == -1:
                return selection
            selection.append(next)
            current = next
    
    def num_selected_items(self):
        return len(self.get_selected_items())

    def GetNextSelected(self, current):
        """Returns next selected item, or -1 when no more"""
        return self.GetNextItem(current,
                                wx.LIST_NEXT_ALL,
                                wx.LIST_STATE_SELECTED) 
    
    def updateList(self, list, selected=[]):
        self.DeleteAllItems()
        for row in list:
            self.Append(row)
        for sel in selected:
            self.SetItemState(sel, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
            
                    
    def move_up(self):
        """sube un nivel las filas seleccionadas"""
        selected = self.get_selected_items()
        if len(selected) == 0:
            self.statusbar.SetStatusText("no hay instrucciones seleccionadas", 0)
            return
        list = self.get_list()
        for sel in selected:
            if sel != 0:
                item = list.pop(sel)
                list.insert(sel-1,item)
        newselected = [sel-1 for sel in selected if sel != 0]
        self.updateList(list, newselected)
        
        
        

    def move_top(self):
        """agrupa y sube las intrucciones al tope de la lista"""
        selected = self.get_selected_items()
        if len(selected) == 0:
            self.statusbar.SetStatusText("no hay instrucciones seleccionadas", 0)
            return
        list = self.get_list()
        for sel in selected:
            if sel != 0:
                item = list.pop(sel)
                list.insert(selected.index(sel),item)
        newselected = [i for i in range(self.num_selected_items())]
        self.updateList(list, newselected)
        
        
        
    def move_down(self):
        """sube un nivel las filas seleccionadas"""
        selected = self.get_selected_items()
        list = self.get_list()
        last = self.GetItemCount() - 1
        for sel in selected:
            if sel != last:
                item = list.pop(sel)
                list.insert(sel+1,item)
        self.updateList(list)
        newselected = [sel+1 for sel in selected if sel != last]
        self.updateList(list, newselected)

    def move_bottom(self):
        """agrupa y sube las intrucciones al tope de la lista"""
        selected = self.get_selected_items()
        list = self.get_list()
        last = self.GetItemCount() - 1
        for sel in selected:
            if sel != last:
                item = list.pop(sel)
                list.append(item)
        newselected = [self.self.GetItemCount()-i for i in range(self.num_selected_items())]
        self.updateList(list, newselected)
        
    def delete(self):
        """elimina las intrucciones seleccionadas"""
        selected = self.get_selected_items()
        list = self.get_list()
        for sel in selected:
            list.pop(sel)
        self.updateList(list)
                

class RegisterListCtrl(wx.ListCtrl):
    """widget de lista que actualiza su tooltip en función de la columna"""
    
    def __init__(self, parent, ID, pos=wx.DefaultPosition,size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        
        self.Bind(wx.EVT_MOTION, self.updateToolTip)
        
    def SetColumns(self, columnas, width=30):
        columnas.reverse()
        self.columnas = columnas
        self.width = width
        for n,col in enumerate(columnas):
            self.InsertColumn(n,col[0], format=wx.LIST_FORMAT_CENTER)
            self.SetColumnWidth(n,width)

    def updateToolTip(self, event):
        (x,y) = event.GetPosition()
        col = x/self.width
        self.SetToolTipString(u"%s: %s" % (self.columnas[col][1],self.columnas[col][2]))
        
                
        
if __name__ == '__main__':
    pass
