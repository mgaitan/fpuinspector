# -*- coding: utf-8 -*-
#!/usr/bin/env python


import wx

class InstructionListCtrl(wx.ListCtrl):
    """widget List que permite seleccionar y mover filas"""
    
    def __init__(self, parent, ID, pos=wx.DefaultPosition,size=wx.DefaultSize, style=0, tooltips=None):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        #self.statusbar = statusbar
        self.Bind(wx.EVT_MOTION, self.updateToolTip)
        self.tooltips = tooltips
    
        
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


    def updateToolTip(self, event):
        (x,y) = event.GetPosition()
        alto_fila = 22 #self.GetSize().GetHeight()/self.GetItemCount()
        fila = y/alto_fila
        #print y, alto_fila, fila
        instruc = self.GetItem(fila,0).GetText()
        try:
            instruc = instruc.split()[0]
            self.SetToolTipString(self.tooltips[instruc])
        except:
            pass
                
        
        

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

    def run_from_selected(self):

        #TODO TODO TODO
        """ejecuta desde la primera instrucción seleccionada o desde el inicio"""
        run_from = self.get_selected_items()[0] or 0
        
        
                

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
        self.SetToolTipString(u"")
        
               

'''

wxPython Custom Widget Collection 20060207
Written By: Edward Flick (eddy -=at=- cdf-imaging -=dot=- com)
            Michele Petrazzo (michele -=dot=- petrazzo -=at=- unipex -=dot=- it)
            Will Sadkin (wsadkin-=at=- nameconnector -=dot=- com)
Copyright 2006 (c) CDF Inc. ( http://www.cdf-imaging.com )
Contributed to the wxPython project under the wxPython project's license.

'''

import locale, wx, sys, cStringIO

import  wx.lib.mixins.listctrl  as  listmix

from wx import ImageFromStream, BitmapFromImage
#----------------------------------------------------------------------
def getSmallUpArrowData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00<IDAT8\x8dcddbf\xa0\x040Q\xa4{h\x18\xf0\xff\xdf\xdf\xffd\x1b\x00\xd3\
\x8c\xcf\x10\x9c\x06\xa0k\xc2e\x08m\xc2\x00\x97m\xd8\xc41\x0c \x14h\xe8\xf2\
\x8c\xa3)q\x10\x18\x00\x00R\xd8#\xec\xb2\xcd\xc1Y\x00\x00\x00\x00IEND\xaeB`\
\x82'

def getSmallUpArrowBitmap():
    return BitmapFromImage(getSmallUpArrowImage())

def getSmallUpArrowImage():
    stream = cStringIO.StringIO(getSmallUpArrowData())
    return ImageFromStream(stream)


def getSmallDnArrowData():
    return \
"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00HIDAT8\x8dcddbf\xa0\x040Q\xa4{\xd4\x00\x06\x06\x06\x06\x06\x16t\x81\
\xff\xff\xfe\xfe'\xa4\x89\x91\x89\x99\x11\xa7\x0b\x90%\ti\xc6j\x00>C\xb0\x89\
\xd3.\x10\xd1m\xc3\xe5*\xbc.\x80i\xc2\x17.\x8c\xa3y\x81\x01\x00\xa1\x0e\x04e\
?\x84B\xef\x00\x00\x00\x00IEND\xaeB`\x82"

def getSmallDnArrowBitmap():
    return BitmapFromImage(getSmallDnArrowImage())

def getSmallDnArrowImage():
    stream = cStringIO.StringIO(getSmallDnArrowData())
    return ImageFromStream(stream)
#----------------------------------------------------------------------

class myListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID=-1, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class TextCtrlAutoComplete (wx.TextCtrl, listmix.ColumnSorterMixin ):

    """Código tomado de http://wiki.wxpython.org/TextCtrlAutoComplete"""

    def __init__ ( self, parent, colNames=None, choices = None,
                  multiChoices=None, showHead=True, dropDownClick=True,
                  colFetch=-1, colSearch=0, hideOnNoMatch=True,
                  selectCallback=None, entryCallback=None, matchFunction=None,
                  **therest) :
        '''
        Constructor works just like wx.TextCtrl except you can pass in a
        list of choices.  You can also change the choice list at any time
        by calling setChoices.
        '''

        if therest.has_key('style'):
            therest['style']=wx.TE_PROCESS_ENTER | therest['style']
        else:
            therest['style']=wx.TE_PROCESS_ENTER

        wx.TextCtrl.__init__(self, parent, **therest )

        #Some variables
        self._dropDownClick = dropDownClick
        self._colNames = colNames
        self._multiChoices = multiChoices
        self._showHead = showHead
        self._choices = choices.keys()
        self._lastinsertionpoint = 0
        self._hideOnNoMatch = hideOnNoMatch
        self._selectCallback = selectCallback
        self._entryCallback = entryCallback
        self._matchFunction = matchFunction

        self._screenheight = wx.SystemSettings.GetMetric( wx.SYS_SCREEN_Y )

        #sort variable needed by listmix
        self.itemDataMap = dict()

        #Load and sort data
        if not (self._multiChoices or self._choices):
            raise ValueError, "Pass me at least one of multiChoices OR choices"

        #widgets
        self.dropdown = wx.PopupWindow( self )

        #Control the style
        flags = wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_SORT_ASCENDING
        if not (showHead and multiChoices) :
            flags = flags | wx.LC_NO_HEADER

        #Create the list and bind the events
        self.dropdownlistbox = myListCtrl( self.dropdown, style=flags,
                                 pos=wx.Point( 0, 0) )

        #initialize the parent
        if multiChoices: ln = len(multiChoices)
        else: ln = 1
        #else: ln = len(choices)
        listmix.ColumnSorterMixin.__init__(self, ln)

        #load the data
        if multiChoices: self.SetMultipleChoices (multiChoices, colSearch=colSearch, colFetch=colFetch)
        else: self.SetChoices ( self._choices )

        gp = self
        while ( gp != None ) :
            gp.Bind ( wx.EVT_MOVE , self.onControlChanged, gp )
            gp.Bind ( wx.EVT_SIZE , self.onControlChanged, gp )
            gp = gp.GetParent()

        self.Bind( wx.EVT_KILL_FOCUS, self.onControlChanged, self )
        self.Bind( wx.EVT_TEXT , self.onEnteredText, self )
        self.Bind( wx.EVT_KEY_DOWN , self.onKeyDown, self )

        #If need drop down on left click
        if dropDownClick:
            self.Bind ( wx.EVT_LEFT_DOWN , self.onClickToggleDown, self )
            self.Bind ( wx.EVT_LEFT_UP , self.onClickToggleUp, self )

        self.dropdown.Bind( wx.EVT_LISTBOX , self.onListItemSelected, self.dropdownlistbox )
        self.dropdownlistbox.Bind(wx.EVT_LEFT_DOWN, self.onListClick)
        self.dropdownlistbox.Bind(wx.EVT_LEFT_DCLICK, self.onListDClick)
        self.dropdownlistbox.Bind(wx.EVT_LIST_COL_CLICK, self.onListColClick)

        self.il = wx.ImageList(16, 16)

        self.sm_dn = self.il.Add(getSmallDnArrowBitmap())
        self.sm_up = self.il.Add(getSmallUpArrowBitmap())

        self.dropdownlistbox.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        self._ascending = True


    #-- methods called from mixin class
    def GetSortImages(self):
        return (self.sm_dn, self.sm_up)

    def GetListCtrl(self):
        return self.dropdownlistbox

    # -- event methods
    def onListClick(self, evt):
        toSel, flag = self.dropdownlistbox.HitTest( evt.GetPosition() )
        #no values on poition, return
        if toSel == -1: return
        self.dropdownlistbox.Select(toSel)

    def onListDClick(self, evt):
        self._setValueFromSelected()

    def onListColClick(self, evt):
        col = evt.GetColumn()

        #reverse the sort
        if col == self._colSearch:
            self._ascending = not self._ascending

        self.SortListItems( evt.GetColumn(), ascending=self._ascending )
        self._colSearch = evt.GetColumn()
        evt.Skip()

    def onEnteredText(self, event):
        text = event.GetString()

        if self._entryCallback:
            self._entryCallback()

        if not text:
            # control is empty; hide dropdown if shown:
            if self.dropdown.IsShown():
                self._showDropDown(False)
            event.Skip()
            return


        found = False
        if self._multiChoices:
            #load the sorted data into the listbox
            dd = self.dropdownlistbox
            choices = [dd.GetItem(x, self._colSearch).GetText()
                for x in xrange(dd.GetItemCount())]
        else:
            choices = self._choices

        for numCh, choice in enumerate(choices):
            if self._matchFunction and self._matchFunction(text, choice):
                found = True
            elif choice.lower().startswith(text.lower()) :
                found = True
            if found:
                self._showDropDown(True)
                item = self.dropdownlistbox.GetItem(numCh)
                toSel = item.GetId()
                self.dropdownlistbox.Select(toSel)
                break

        if not found:
            self.dropdownlistbox.Select(self.dropdownlistbox.GetFirstSelected(), False)
            if self._hideOnNoMatch:
                self._showDropDown(False)

        self._listItemVisible()

        event.Skip ()

    def onKeyDown ( self, event ) :
        """ Do some work when the user press on the keys:
            up and down: move the cursor
            left and right: move the search
        """
        skip = True
        sel = self.dropdownlistbox.GetFirstSelected()
        visible = self.dropdown.IsShown()

        KC = event.GetKeyCode()
        if KC == wx.WXK_DOWN :
            if sel < (self.dropdownlistbox.GetItemCount () - 1) :
                self.dropdownlistbox.Select ( sel+1 )
                self._listItemVisible()
            self._showDropDown ()
            skip = False
        elif KC == wx.WXK_UP :
            if sel > 0 :
                self.dropdownlistbox.Select ( sel - 1 )
                self._listItemVisible()
            self._showDropDown ()
            skip = False
        elif KC == wx.WXK_LEFT :
            if not self._multiChoices: return
            if self._colSearch > 0:
                self._colSearch -=1
            self._showDropDown ()
        elif KC == wx.WXK_RIGHT:
            if not self._multiChoices: return
            if self._colSearch < self.dropdownlistbox.GetColumnCount() -1:
                self._colSearch += 1
            self._showDropDown()

        if visible :
            if event.GetKeyCode() == wx.WXK_RETURN :
                self._setValueFromSelected()
                skip = False
            if event.GetKeyCode() == wx.WXK_ESCAPE :
                self._showDropDown( False )
                skip = False
        if skip :
            event.Skip()

    def onListItemSelected (self, event):
        self._setValueFromSelected()
        event.Skip()

    def onClickToggleDown(self, event):
        self._lastinsertionpoint = self.GetInsertionPoint()
        event.Skip ()

    def onClickToggleUp ( self, event ) :
        if ( self.GetInsertionPoint() == self._lastinsertionpoint ) :
            self._showDropDown ( not self.dropdown.IsShown() )
        event.Skip ()

    def onControlChanged(self, event):
        self._showDropDown( False )
        event.Skip()


    # -- Interfaces methods
    def SetMultipleChoices(self, choices, colSearch=0, colFetch=-1):
        ''' Set multi-column choice
        '''
        self._multiChoices = choices
        self._choices = None
        if not isinstance(self._multiChoices, list):
            self._multiChoices = [ x for x in self._multiChoices]

        flags = wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_SORT_ASCENDING
        if not self._showHead:
            flags |= wx.LC_NO_HEADER
        self.dropdownlistbox.SetWindowStyleFlag(flags)

        #prevent errors on "old" systems
        if sys.version.startswith("2.3"):
            self._multiChoices.sort(lambda x, y: cmp(x[0].lower(), y[0].lower()))
        else:
            self._multiChoices.sort(key=lambda x: locale.strxfrm(x[0]).lower() )

        self._updateDataList(self._multiChoices)

        lChoices = len(choices)
        if lChoices < 2:
            raise ValueError, "You have to pass me a multi-dimension list"

        for numCol, rowValues in enumerate(choices[0]):

            if self._colNames: colName = self._colNames[numCol]
            else: colName = "Select %i" % numCol

            self.dropdownlistbox.InsertColumn(numCol, colName)

        for numRow, valRow in enumerate(choices):

            for numCol, colVal in enumerate(valRow):
                if numCol == 0:
                    index = self.dropdownlistbox.InsertImageStringItem(sys.maxint, colVal, -1)
                self.dropdownlistbox.SetStringItem(index, numCol, colVal)
                self.dropdownlistbox.SetItemData(index, numRow)

        self._setListSize()
        self._colSearch = colSearch
        self._colFetch = colFetch

    def SetChoices(self, choices):
        '''
        Sets the choices available in the popup wx.ListBox.
        The items will be sorted case insensitively.
        '''
        self._choices = choices
        self._multiChoices = None
        flags = wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_SORT_ASCENDING | wx.LC_NO_HEADER
        self.dropdownlistbox.SetWindowStyleFlag(flags)

        if not isinstance(choices, list):
            self._choices = [ x for x in choices]

        #prevent errors on "old" systems
        if sys.version.startswith("2.3"):
            self._choices.sort(lambda x, y: cmp(x.lower(), y.lower()))
        else:
            self._choices.sort(key=lambda x: locale.strxfrm(x).lower())

        self._updateDataList(self._choices)

        self.dropdownlistbox.InsertColumn(0, "")

        for num, colVal in enumerate(self._choices):
            index = self.dropdownlistbox.InsertImageStringItem(sys.maxint, colVal, -1)

            self.dropdownlistbox.SetStringItem(index, 0, colVal)
            self.dropdownlistbox.SetItemData(index, num)

        self._setListSize()

        # there is only one choice for both search and fetch if setting a single column:
        self._colSearch = 0
        self._colFetch = -1

    def GetChoices(self):
        if self._choices:
            return self._choices
        else:
            return self._multiChoices

    def SetSelectCallback(self, cb=None):
        self._selectCallback = cb

    def SetEntryCallback(self, cb=None):
        self._entryCallback = cb

    def SetMatchFunction(self, mf=None):
        self._matchFunction = mf


    #-- Internal methods
    def _setValueFromSelected( self ) :
         '''
         Sets the wx.TextCtrl value from the selected wx.ListCtrl item.
         Will do nothing if no item is selected in the wx.ListCtrl.
         '''
         sel = self.dropdownlistbox.GetFirstSelected()
         if sel > -1:
            if self._colFetch != -1: col = self._colFetch
            else: col = self._colSearch

            itemtext = self.dropdownlistbox.GetItem(sel, col).GetText()
            if self._selectCallback:
                dd = self.dropdownlistbox
                values = [dd.GetItem(sel, x).GetText()
                    for x in xrange(dd.GetColumnCount())]
                self._selectCallback( values )

            self.SetValue (itemtext)
            self.SetInsertionPointEnd ()
            self.SetSelection ( -1, -1 )
            self._showDropDown ( False )


    def _showDropDown ( self, show = True ) :
        '''
        Either display the drop down list (show = True) or hide it (show = False).
        '''
        if show :
            size = self.dropdown.GetSize()
            width, height = self . GetSizeTuple()
            x, y = self . ClientToScreenXY ( 0, height )
            if size.GetWidth() != width :
                size.SetWidth(width)
                self.dropdown.SetSize(size)
                self.dropdownlistbox.SetSize(self.dropdown.GetClientSize())
            if (y + size.GetHeight()) < self._screenheight :
                self.dropdown . SetPosition ( wx.Point(x, y) )
            else:
                self.dropdown . SetPosition ( wx.Point(x, y - height - size.GetHeight()) )
        self.dropdown.Show ( show )

    def _listItemVisible( self ) :
        '''
        Moves the selected item to the top of the list ensuring it is always visible.
        '''
        toSel =  self.dropdownlistbox.GetFirstSelected ()
        if toSel == -1: return
        self.dropdownlistbox.EnsureVisible( toSel )

    def _updateDataList(self, choices):
        #delete, if need, all the previous data
        if self.dropdownlistbox.GetColumnCount() != 0:
            self.dropdownlistbox.DeleteAllColumns()
            self.dropdownlistbox.DeleteAllItems()

        #and update the dict
        if choices:
            for numVal, data in enumerate(choices):
                self.itemDataMap[numVal] = data
        else:
            numVal = 0
        self.SetColumnCount(numVal)

    def _setListSize(self):
        if self._multiChoices:
            choices = self._multiChoices
        else:
            choices = self._choices

        longest = 0
        for choice in choices :
            longest = max(len(choice), longest)

        longest += 3
        itemcount = min( len( choices ) , 7 ) + 2
        charheight = self.dropdownlistbox.GetCharHeight()
        charwidth = self.dropdownlistbox.GetCharWidth()
        self.popupsize = wx.Size( charwidth*longest, charheight*itemcount )
        self.dropdownlistbox.SetSize ( self.popupsize )
        self.dropdown.SetClientSize( self.popupsize )



        
if __name__ == '__main__':
    pass
