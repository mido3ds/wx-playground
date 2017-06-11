#!/usr/bin/env python3
import wx

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    

        # main items
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        viewMenu = wx.Menu()
        
        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statubar', 
            'Show Statusbar', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 
            'Show Toolbar', kind=wx.ITEM_CHECK)
            
        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)

        menubar.Append(fileMenu, '&File')
        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('I am a status bar')

        self.SetSize((350, 250))
        self.SetTitle('Check menu item')
        self.Centre()
        self.Show(True)
        
        
    def ToggleStatusBar(self, e):
        
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

            

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()