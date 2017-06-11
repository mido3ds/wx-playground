#!/usr/bin/env python3
import wx

app = wx.App()


item = wx.Menu()
bar = wx.MenuBar()
bar.Append(item, title='hello menu')

frame = wx.Frame(
                        parent=None, 
                        style=wx.MAXIMIZE_BOX | 
                        wx.RESIZE_BORDER | 
                        wx.CAPTION | 
                        wx.CLOSE_BOX | 
                        wx.STAY_ON_TOP |
                        wx.FRAME_EX_METAL |
                        wx.MAXIMIZE |
                        wx.MAXIMIZE_BOX, 
                        name='My Simple App', 
                        title='Some title'
                                                  )
frame.SetMenuBar(bar)
frame.Center()
frame.Move(x=50, y=60)

frame.Show(True)
app.MainLoop()
