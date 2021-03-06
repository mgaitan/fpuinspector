# -*- coding: utf-8 -*-


"""
Este es el código de la ventana principal, y el verdadero controlador del programa

Contiene diferentes "widgets" (listas, cajas de texto, botones, menúes,...) que pueden producir eventos. 
Un evento es un click, la presión de una tecla, etc. Los eventos se asociacion 
a uno (o más) métodos de respuesta a través del método Bind() que provee wx. 

La aplicación de escritorio se convierte en una "aplicación orientada a eventos"
ya que un hilo principal (el mainloop() que se ejecuta en app.py) está todo el 
tiempo escuchando eventos y despachando al método encargado de hacer algo en 
consecuencia (es simular a las interrupciones del procesador). 

Los métodos que comienzan con *action* son los que responden a eventos. Hay 
dos grupos: los que actuan sobre la lista  de intrucciones (abrir, guardar, mover 
o quitar instrucciones de la lista, etc) y los que actuan sobre la libreria FPU
(refrescar pila, refrescar registros, ejecutar siguiente instruccion). 

El método __init__ , como en cualquier clase de Python, es el inicializador. 
Cuando se crea un objeto MainFrame() (como el que se crea en app.py), 
automáticamente se ejecuta este método que es el encargado de crear los elementos
de la ventana, ubicarlos en diferentes 'sizer' (que son divisiones de la ventana, 
la manera que tiene WX de distribuir los objetos en la ventana), y darle las 
propiedades. Para una cuestión de claridad, esas tareas se separan en dos  métodos 
completarios (que hacen las veces de subrutinas): son _do_layout() y _set_properties()
La mayoría de este código lo produjo la herramienta wxGlade, que sirve para 
diseñar la ventana visualmente, como en los IDEs de Java o Visual Basic. 
Con la ventaja que al producir código, luego se puede modificar a mano. 

Dos objetos importantes se instancian como atributos de un objeto MainFrame

Estos son self.manager y self.lib  . El primero es un manejador del proxy 
que separa una parte del programa (el objeto lib) en un proceso hijo.
self.lib es un objeto Wrapper() (ver `wrapper.py`) instanciado a través del 
manejador. 

La gestión de archivos utiliza el módulo Pickle, que es la herramienta para 
serializar objetos de (casi) cualquier índole. En vez de tener que definir
una estructura para el archivo, y luego tener que decodificarla, simplemente
serializamos el contenido a guardar (los elementos de la lista de instrucciones)
y dejamos que Pickle se encargue de escribir y de leer el archivo. 


Hay abundantes comentarios en el código. Espero sea de utilidad!
"""





import wx    #nuestra biblioteca GUI 
import os       # vamos a manejar archivos y directorios
import pickle   # serialización de datos para guardar y leer objetos a un archivo
from multiprocessing.managers import BaseManager  #la magia que crea un proceso nuevo
                                                  #y lo maneja como si fuera uno sólo

from AboutFrame import AboutFrame       #la ventana de "Acerca de" donde estamos nosotros

#algunos widgets están 'mejorados' ver docu de `myWidgets.py`
from myWidgets import InstructionListCtrl, RegisterListCtrl, TextCtrlAutoComplete

from helpers import *   #funciones de formateo, etc. 
from wrapper import Wrapper  #la interfaz con C!

class MyManager(BaseManager):
    """MyManager simplemente hereda de BaseManager. Es el manejador de proxy
        que sabe crear y comunicarse con otro proceso"""
    pass

#hay que decirle al manejador qué tipo de objetos va a separar en otro proceso. 
#el primer parámetro es la identificación de ese tipo de objetos a través 
#del wrapper. Para no complicar las cosas, se llama igual. 
MyManager.register('Wrapper', Wrapper)  



_path = os.path.abspath(os.path.dirname(__file__)) #la ruta desde donde se ejecuta el programa

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        """inicializador. Dibuja los elementos en la ventana y le asigna propiedades"""

        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.sizer_12_staticbox = wx.StaticBox(self, -1, "Pila")
        self.sizer_7_staticbox = wx.StaticBox(self, -1, "Registro de Control")
        self.sizer_8_staticbox = wx.StaticBox(self, -1, "Registro de Estado")
        self.sizer_3_staticbox = wx.StaticBox(self, -1, "Instrucciones")
        
        # Menu Bar
        menues_ids = [wx.NewId() for i in range(7)]
        
        self.frame_1_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(menues_ids[0], "&Nuevo", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(menues_ids[1], "&Abrir", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(menues_ids[2], "&Guardar", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(menues_ids[3], "Guardar como...", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(menues_ids[4], "&Salir", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "&Archivo")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(menues_ids[5], u"Índ&ice", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(menues_ids[6], "&Acerca de..", "", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "A&yuda")
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end
        self.statusbar = self.CreateStatusBar(1, 0)
        
        # Tool Bar
        tools_ids = [wx.NewId() for i in range(11)]
        
        self.frame_1_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_DOCKABLE)
        self.SetToolBar(self.frame_1_toolbar)
        self.frame_1_toolbar.AddLabelTool(tools_ids[0], "Nuevo", wx.Bitmap("%s/icons/document-new.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Nuevo archivo", "Crea una nueva secuencia de instrucciones")
        self.frame_1_toolbar.AddLabelTool(tools_ids[1], "Abrir", wx.Bitmap("%s/icons/document-open.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Abrir archivo", "Abre una secuencia de instrucciones de un archivo")
        self.frame_1_toolbar.AddLabelTool(tools_ids[2], "Guardar", wx.Bitmap("%s/icons/document-save.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Guardar", "Guarda la secuencia de instrucciones actual")
        self.frame_1_toolbar.AddLabelTool(tools_ids[3], "Guardar como...", wx.Bitmap("%s/icons/document-save-as.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Guardar como...", "Guarda la secuencia en un nuevo archivo")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(tools_ids[4], "Arriba", wx.Bitmap("%s/icons/go-top.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Subir al tope", "Agrupa y sube las intrucciones selecciones al principio")
        self.frame_1_toolbar.AddLabelTool(tools_ids[5], "Subir", wx.Bitmap("%s/icons/go-up.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Subir una intrucción", "Sube las instrucciones seleccionadas un paso")
        self.frame_1_toolbar.AddLabelTool(tools_ids[6], "Bajar", wx.Bitmap("%s/icons/go-down.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Bajar una instrucción", "Baja las intrucciones seleccionadas un paso")
        self.frame_1_toolbar.AddLabelTool(tools_ids[7], "Abajo", wx.Bitmap("%s/icons/go-bottom.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Bajar al final", "Agrupa y baja las instrucciones seleccionadas al final")
        self.frame_1_toolbar.AddLabelTool(tools_ids[8], "Borrar", wx.Bitmap("%s/icons/list-remove.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Borrar", "Borra las instrucciones seleccionadas")
        self.frame_1_toolbar.AddSeparator()
        self.frame_1_toolbar.AddLabelTool(tools_ids[9], "Ejecutar", wx.Bitmap("%s/icons/go-next.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Ejecutar instrucción", "Ejecuta la siguiente instrucción de la secuencia")
        self.frame_1_toolbar.AddLabelTool(tools_ids[10], "Actualizar", wx.Bitmap("%s/icons/view-refresh.png" % _path, wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Actualizar entorno", "Actualiza los registros y el estado de la pila")
        # Tool Bar end
        
        
        #libreria de interfaz con C. la gran magia. 
        self.manager = MyManager()    #mediante un proxy que desacopla el wrapper en otro proceso (¡Viva python!)
        self.manager.start()        
        self.lib = self.manager.Wrapper()

        implementadas = self.lib.get_valid_instructions()
        #input de instrucciones
        self.instructionInput = TextCtrlAutoComplete(self, "", style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB, choices=implementadas)
        
        
        self.bitmap_button_1 = wx.BitmapButton(self, -1, wx.Bitmap("%s/icons/list-add.png" % _path, wx.BITMAP_TYPE_ANY))
        self.instructionsList = InstructionListCtrl(self, -1, style=wx.LC_REPORT| wx.LC_NO_HEADER|wx.LC_HRULES|wx.SUNKEN_BORDER, tooltips=implementadas)
        
        self.stackList = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)        

        #listas que muestran flags binarios
        self.controlList = RegisterListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.statusList = RegisterListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.actionNew, id=menues_ids[0])
        self.Bind(wx.EVT_MENU, self.actionOpen, id=menues_ids[1])
        self.Bind(wx.EVT_MENU, self.actionSave, id=menues_ids[2])
        self.Bind(wx.EVT_MENU, self.actionSaveAs, id=menues_ids[3])
        self.Bind(wx.EVT_MENU, self.actionExit, id=menues_ids[4])
        self.Bind(wx.EVT_MENU, self.actionShowHelp, id=menues_ids[5])
        self.Bind(wx.EVT_MENU, self.actionShowAbout, id=menues_ids[6])
       
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)

        self.Bind(wx.EVT_TOOL, self.actionNew, id=tools_ids[0])
        self.Bind(wx.EVT_TOOL, self.actionOpen, id=tools_ids[1])
        self.Bind(wx.EVT_TOOL, self.actionSave, id=tools_ids[2])
        self.Bind(wx.EVT_TOOL, self.actionSaveAs, id=tools_ids[3])
        self.Bind(wx.EVT_TOOL, self.actionGoTop, id=tools_ids[4])
        self.Bind(wx.EVT_TOOL, self.actionUp, id=tools_ids[5])
        self.Bind(wx.EVT_TOOL, self.actionDown, id=tools_ids[6])
        self.Bind(wx.EVT_TOOL, self.actionBottom, id=tools_ids[7])
        self.Bind(wx.EVT_TOOL, self.actionDelete, id=tools_ids[8])
        self.Bind(wx.EVT_TOOL, self.actionRunNext, id=tools_ids[9])
        self.Bind(wx.EVT_TOOL, self.actionRefreshAll, id=tools_ids[10])
       
       
        self.Bind(wx.EVT_TEXT_ENTER, self.actionAdd, self.instructionInput)
        self.Bind(wx.EVT_BUTTON, self.actionAdd, self.bitmap_button_1)
        # end wxGlade

        self.doiexit = wx.MessageDialog( self, u'Desea salir? \n',
                        "Saliendo...", wx.YES_NO)
       
        self.dirname = ''
        self.filename = None
        self.modificado = False

        
        
    def __set_properties(self):
        """asignación de propiedades iniciales a los distintos widgets"""

        self.titulo = "FPU Inspector"
        self.SetTitle(self.titulo)
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("%s/icons/icon.jpg" % _path, wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.statusbar.SetStatusWidths([-1])
        # statusbar fields

        self.updateStatusBar()
        
            
        self.frame_1_toolbar.Realize()
        self.instructionInput.SetMinSize((200, 27))
        self.instructionInput.SetToolTipString(u"Ingrese una instrucción de FPU aquí")
        self.instructionInput.SetFocus()
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())    
        # end wxGlade
        
        
        self.instructionsList.InsertColumn(0,u'Código')
        self.instructionsList.SetColumnWidth(0,220)
        
        registro_estado = [('IE',u'Bit de error de operación inválida',
                        u'Indica una operación inválida: desbordamiento '
                        u'de la pila, un valor indeterminado, raíz '
                        u'cuadrada de número negativo,..'),
                        ('DE',u'Bit de error de operando no normalizado',
                        u'Indica que al menos uno de los operandos no está normalizado.'),
                        ('ZE',u'Bit de error de división por cero',
                        u'Indica una división por cero.'),
                        ('OE',
                         u'Bit de error de overflow',
                         u'Indica un error de desbordamiento (resultado demasiado'
                         u' grande para ser representado).'),
                        ('UE', 
                         u'Bit de erro de underflow', 
                         u'Indica un error de subflujo (resultado diferente a 0 '
                         u'que es demasiado pequeño para ser representado '
                         u'con la precisión actual seleccionada por la palabra de control).'),
                        ('PE', 
                         u'Bit de error de precisión', 
                         u'Indica que el resultado o los operandos exceden '
                         u'la precisión seleccionada.'),
                        ('SF', 
                         u'Bit de operación inválida', 
                         u'Diferencia entre las operaciones inválidas al '
                         u'interpretar los bits del código de condición.'),
                        ('ES', 
                         u'Bit de resumen de errores', 
                         u'Si está a 1, indica que cualquiera de los bits de '
                         u'error no enmascarado está a 1.'),
                        ('C0', 
                         u'Bits del código de condición', 
                         u'indican condiciones del coprocesador, '
                         u'resultado de operaciones aritméticas y de comparación '
                         u'en punto flotante. Utilizados para el tratamiento '
                         u'de excepciones.'),
                        ('C1', 
                         u'Bits del código de condición', 
                         u'indican condiciones del coprocesador, resultado '
                         u'de operaciones aritméticas y de comparación '
                         u'en coma flotante. Utilizados para el tratamiento '
                         u'de excepciones.'),
                        ('C2', 
                        u'Bits del código de condición', 
                        u'indican condiciones del coprocesador, resultado '
                        u'de operaciones aritméticas y de comparación en punto ' 
                        u'flotante. Utilizados para el tratamiento de excepciones.'),
                        
                        ('TOP0', 
                         u'Campo de tope o cima de pila', 
                         u'Muestra el primer registro activo de la pila '
                         u'(registro actualmente diseccionado como registro '
                         u'superior de la pila (ST)).'),
                        ('TOP1', 
                         u'Campo de tope o cima de pila', 
                         u'Muestra el primer registro activo de la pila '
                         u'(registro actualmente diseccionado como registro '
                         u'superior de la pila (ST)).'),
                        ('TOP2', 
                         u'Campo de tope o cima de pila', 
                         u'Muestra el primer registro activo de la pila '
                         u'(registro actualmente diseccionado como registro '
                         u'superior de la pila (ST)).'),
                        ('C3', 
                        u'Bits del código de condición', 
                        u'indican condiciones del coprocesador, resultado '
                        u'de operaciones aritméticas y de comparación en punto' 
                        u'flotante. Utilizados para el tratamiento de excepciones.'),
                        ('B',
                         u'Bit de ocupado', 
                         u'Indica que el coprocesado está ocupado realizando '
                         u'una tarea. Los coprocesadores actuales no necesitan '
                         u'verificar este bit, ya que se sincronizan automáticamente '
                         u'con el microprocesador.'),]
            
        registro_control = [('IM',u'Máscara de operación inválida',''),
                        ('DM',u'Máscara de operando no normalizado',''),
                        ('ZM',u'Máscara de división por cero',''),
                        ('OM',u'Máscara de overflow',''),
                        ('UM', u'Máscara de underflow', ''),
                        ('PE', u'Máscara de error de precisión', ''),
                        ('', '', ''),
                        ('', '', ''),
                        ('PC0', u'Control de precisión', u'\n00: precisión sencilla\n'
                        u'01:Reservado\n10:Doble precisión (largo)\n'
                        u'11: Precisión extendida (temporal)'),
                        ('PC1', u'Control de precisión', u'\n00: precisión sencilla\n'
                        u'01:Reservado\n10:Doble precisión (largo)\n'
                        u'11: Precisión extendida (temporal)'),
                        ('RC0', u'Control de redondeo', u'\n00:redondeo al más cercano o par\n'
                        u'01:Redondeo hacia abajo\n10:Redondeo hacia arriba\n'
                        u'11: Trunca'),
                        ('RC1', u'Control de redondeo', u'\n00:redondeo al más cercano o par\n'
                        u'01:Redondeo hacia abajo\n10:Redondeo hacia arriba\n'
                        u'11: Trunca'),
                        ('IC', u'Control de infinito', u'\n0: Proyectivo\n1: Afin'),
                        ('', '', ''),
                        ('', '', ''),
                        ('', '', ''),
                        ]
        
        
        #Configuro las columnas para los registros
        self.controlList.SetColumns(registro_control)
        self.statusList.SetColumns(registro_estado)
        
            
        
        #Lista de pila
        
        stack_cols = ('ST', 'Float', 'Etiqueta')
        for n,col in enumerate(stack_cols):
            self.stackList.InsertColumn(n,col)
        self.stackList.SetColumnWidth(0,30)
        self.stackList.SetColumnWidth(1,100)
        self.stackList.SetColumnWidth(2,100)
        
        
                            
    def __do_layout(self):
        """genera las divisiones y las ubicaciones de cada elemento en la ventana"""
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.HORIZONTAL)
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.StaticBoxSizer(self.sizer_12_staticbox, wx.HORIZONTAL)
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.VERTICAL)
        sizer_4 = wx.FlexGridSizer(1, 3, 0, 0)
        sizer_4.Add(self.instructionInput, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.bitmap_button_1, 0, 0, 0)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_3.Add(self.instructionsList, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_12.Add(self.stackList, 1, wx.LEFT|wx.EXPAND, 0)
        sizer_2.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_7.Add(self.controlList, 1, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add(self.statusList, 1, wx.EXPAND|wx.FIXED_MINSIZE, 0)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_6, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade



    def actionExit(self, event):
        """Salir y cerrar la puerta"""
        self.Close(True)

    def onCloseWindow(self, event):
        """al salir se ejecuta este método que verifica el estado del archivo"""
        if self.modificado:
            #self.actionSave(event)
            dlg = wx.MessageDialog(self, "El archivo no se ha guardado\nDesea guardarlo?", "Salir", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
            answer = dlg.ShowModal()
            dlg.Destroy()
            if answer == wx.ID_YES:
                self.actionSave(event)
            elif answer == wx.ID_NO:
                self.Destroy() # frame
        else:
            dlg = wx.MessageDialog(self, "Desea salir?", "Salir", wx.YES_NO | wx.ICON_QUESTION)
            answer = dlg.ShowModal()
            dlg.Destroy()
            if answer == wx.ID_YES:
                self.Destroy()
        
        

    def actionShowHelp(self, event): # wxGlade: MainFrame.<event_handler>
        print "Event handler `actionShowHelp' not implemented!"
        

    def actionShowAbout(self, event): # wxGlade: MainFrame.<event_handler>
        self.about = AboutFrame(None, -1, "")
        self.about.Show(True)
        
        

    def actionGoTop(self, event): # wxGlade: MainFrame.<event_handler>
        num = self.instructionsList.num_selected_items()
        if num > 0:   
            self.instructionsList.move_top()
            self.modificado = True
            self.updateStatusBar(u"%i instrucciones movidas al inicio de la sencuencia" % num)
        else:
            self.updateStatusBar(u"No hay instrucciones seleccionadas")

    def actionUp(self, event): # wxGlade: MainFrame.<event_handler>
        num = self.instructionsList.num_selected_items()
        if num > 0:   
            self.instructionsList.move_up()
            self.modificado = True
            self.updateStatusBar(u"%i instrucciones subidas un paso" % num)
        else:
            self.updateStatusBar(u"No hay instrucciones seleccionadas")
        

    def actionDown(self, event): # wxGlade: MainFrame.<event_handler>
        num = self.instructionsList.num_selected_items()
        if num > 0:   
            self.instructionsList.move_down()
            self.modificado = True
            self.updateStatusBar(u"%i instrucciones bajadas un paso" % num)
        else:
            self.updateStatusBar(u"No hay instrucciones seleccionadas")
        

    def actionBottom(self, event): # wxGlade: MainFrame.<event_handler>
        num = self.instructionsList.num_selected_items()
        if num > 0:   
            self.instructionsList.move_bottom()
            self.modificado = True
            self.updateStatusBar(u"%i instrucciones movidas al final de la secuencia" % num)
        else:
            self.updateStatusBar(u"No hay instrucciones seleccionadas")

    def actionDelete(self, event): # wxGlade: MainFrame.<event_handler>
        num = self.instructionsList.num_selected_items()
        if num > 0:   
            self.instructionsList.delete()
            self.modificado = True
            self.updateStatusBar(u"%i instrucciones eliminadas" % num)
        else:
            self.updateStatusBar(u"No hay instrucciones seleccionadas")


    def actionRunNext(self, event): # wxGlade: MainFrame.<event_handler>
        """ejecuta desde la primera instrucción seleccionada o desde el inicio"""
        sel_items = self.instructionsList.get_selected_items()
        if len(sel_items)>0:
            run_from = sel_items[0]
        else:
            run_from = 0
        instruction = self.instructionsList.get_list()[run_from][0]
        self.lib.run_or_test_instruction(instruction, True)
        self.actionRefreshAll(event)
        self.instructionsList.select_next(run_from)

    def actionRefreshAll(self, event=None): # wxGlade: MainFrame.<event_handler>
        self.actionRefreshControl(event)
        self.actionRefreshStatus(event)
        self.actionRefreshStack(event)
        self.updateStatusBar(u"Registros y pila actualizados")
        
    
    def actionRefreshControl(self, event):
        control_val = self.lib.get_control()
        print "control: " + str(control_val)
        self.controlList.DeleteAllItems()
        self.controlList.Append(int2bin(control_val))
        
    def actionRefreshStatus(self, event):
        status_val = self.lib.get_estado()
        print "estado: " + str(status_val)
        self.statusList.DeleteAllItems()
        self.statusList.Append(int2bin(status_val))
    
    def actionRefreshStack(self, event=None):
        stack = self.lib.get_stack()
        self.stackList.DeleteAllItems()
        #stack = [10.8, 10, 0, 0, 0, 0, 0, 1]
        for n,val in enumerate(stack):
            self.stackList.Append([u'%i' % n, unicode(val), u''])
        #self.lib.set_stack(stack)
        
        
        
  
    def actionAdd(self, event): # wxGlade: MainFrame.<event_handler>
        instruccion = self.instructionInput.GetValue().upper()
        if self.lib.run_or_test_instruction(instruccion):
            self.instructionsList.Append([instruccion])
            self.instructionInput.SetValue('')
            self.instructionInput.SetFocus()
            self.updateStatusBar(u"Instrucción '%s' agregada" % instruccion)
            self.modificado = True
        else:
            self.updateStatusBar(u"Instrucción incorrecta")


    def actionOpen(self,event):
        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        dlg = wx.FileDialog(self, "Elija un archivo", self.dirname, "", "*.fpu", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()

            # Open the file, read the contents and set them into
            # the text edit window
            filehandle=open(os.path.join(self.dirname, self.filename),'r')
            lista = pickle.load(filehandle)
            
            #update list
            self.instructionsList.updateList(lista)

            filehandle.close()

            # Report on name of latest file read
            self.SetTitle("%s <%s>" % (self.titulo, self.filename))
            
            self.modificado = False
            self.updateStatusBar(u"Archivo %s abierto correctamente" % self.filename)
        dlg.Destroy()


    def actionNew(self, event): # wxGlade: MainFrame.<event_handler>
        if self.modificado:
            dlg = wx.MessageDialog(None, u'Si no guarda, se perderán permanentemente los cambios realizados\n¿Desea guardar antes?', 
                u'Los cambios no ha sido guardados', 
                style=wx.YES_NO | wx.CANCEL | wx.ICON_EXCLAMATION | wx.STAY_ON_TOP)
                
            selection = dlg.ShowModal()
            if selection == wx.ID_YES:
                self.actionSave(event)
            elif selection == wx.ID_CANCEL:
                evtent.Skip()
            dlg.Destroy() 
        
        self.instructionsList.DeleteAllItems()
        self.filename = None
        self.SetTitle(self.titulo)
        
    



    def actionSaveAs(self,event):
        """guarda la lista de intrucciones actual dando un nombre nuevo"""
        dlg = wx.FileDialog(self, "Elija un archivo", self.dirname, "", "*.fpu", \
                wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            self.actionSave(event)
            
        # Get rid of the dialog to keep things tidy
        dlg.Destroy()

    def actionSave(self,event):
        """guarda la lista de instrucciones en el archivo abierto. Si no existe, 
        abre el dialogo Guardar como"""
        print event
        if self.filename is None:
            self.actionSaveAs(event)
        else:
            list = self.instructionsList.get_list()
            filehandle=open(os.path.join(self.dirname, self.filename),'w')
            pickle.dump(list,filehandle)
            filehandle.close()
            self.SetTitle("%s <%s>" % (self.titulo, self.filename))
            self.modificado = False
            
            self.updateStatusBar(u"Archivo %s guardado" % filename)
        return


    def updateStatusBar(self, msg=u'Agregue una instrucción'):
        statusbar_fields = []
        if isinstance(msg,str):
            statusbar_fields.append(msg)
        elif hasattr(msg,'__iter__'):
            statusbar_fields = msg
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(str(statusbar_fields[i]), i)
        
        

# end of class MainFrame


