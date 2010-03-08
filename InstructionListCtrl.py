# -*- coding: utf-8 -*-
#!/usr/bin/env python


import wx

class InstructionListCtrl(wx.ListCtrl):
    """widget potenciado que permite seleccionar y mover filas"""
    
    def __init__(self, parent, ID, pos=wx.DefaultPosition,size=wx.DefaultSize, style=0, statusbar=None):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        self.statusbar = statusbar
        
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

    def GetNextSelected(self, current):
        """Returns next selected item, or -1 when no more"""
        return self.GetNextItem(current,
                                wx.LIST_NEXT_ALL,
                                wx.LIST_STATE_SELECTED) 
    
    def updateList(self, list):
        self.DeleteAllItems()
        for row in list:
            self.Append(row)
            
                    
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
        self.updateList(list)

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
        self.updateList(list)
        
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

    def move_bottom(self):
        """agrupa y sube las intrucciones al tope de la lista"""
        selected = self.get_selected_items()
        list = self.get_list()
        last = self.GetItemCount() - 1
        for sel in selected:
            if sel != last:
                item = list.pop(sel)
                list.append(item)
        self.updateList(list)
        
    def delete(self):
        """elimina las intrucciones seleccionadas"""
        selected = self.get_selected_items()
        list = self.get_list()
        for sel in selected:
            list.pop(sel)
        self.updateList(list)
                
                
                
                
        
        


if __name__ == '__main__':
    pass
