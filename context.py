#!/usr/bin/python
# -*- coding: utf-8 -*-
import wx

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.setUI

    def setUI(self):
          wx.MenuBar()

          self.Bind(wx.EVT_MENU, self.onRightClick)

          self.SetSize((300, 300))
          self.SetTitle('hello wx')
          self.Center()
          self.Show(True)
    
    def onRightClick(self): 
        # make new main menu
        main_menu = wx.PopupMenu() 

        # add new menues
        menu2 = main_menu.Append(id=1, item='Copy')
        menu3 = main_menu.Append(id=1, item='Paste')

        menu2.Bind(wx.EVT_CLK, self.onCopy)
        menu3.Bind(wx.EVT_CLK, self.onPaste)

        main_menu.Append(menu2)
        main_menu.Append(menu3)


    def onCopy(self):
        print('i am copying')

    def onPaste(self):
        print('i am pasting')

def main():
    app = wx.App()
    Example(None)
    app.MainLoop()

if __name__ == '__main__':
    main()