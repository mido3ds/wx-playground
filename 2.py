#!/usr/bin/env python3
import wx

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()

        # make menuitems
        fileMenu.Append(id=-1, item='New', helpString='Do something')
        fileMenu.AppendSeparator()
        fitem = fileMenu.Append(id=-1, item='Quit', helpString='Quit application')

        nothing = wx.Menu()
        nothing.Append(id=-1, item='Hello', helpString='mmmmm, prints hello!')

        submenu = wx.Menu()
        submenu.Append(id=-1, item='import nothing')
        submenu.Append(id=-1, item='import something else')
        submenu.Append(id=-1, item='import nothing again')

        nothing.AppendSeparator()
        nothing.Append(-1, 'import', submenu)

        menubar.Append(fileMenu, '&File')
        menubar.Append(nothing, 'Nothing')

        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()
        self.Show(True)
        
    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()