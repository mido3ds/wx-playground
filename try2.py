import wx

BACKGROUND = 'image.jpg'

class MyFrame(wx.Frame): 
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(
            self, parent=None, 
            size=(720, 480), 
            style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),
            *args, **kwargs
        )
        
        self.SetTitle('Hello wx')
        self.Center()

        # create panel
        MyPanel(frame=self)

        # create menu bar
        MyBar(frame=self)

        self.Show()

class MyPanel(wx.Panel): 
    def __init__(self, frame, *args, **kwargs):
        wx.Panel.__init__(self, frame, *args, **kwargs)

        # add objects to it
        button = wx.Button(parent=self, label='click me')
        button.Bind(
            event=wx.EVT_BUTTON,
            handler=lambda evt, text='hello': wx.MessageBox(
                                                                message=text,
                                                                caption='this is a caption',
                                                                style= wx.OK | wx.ICON_ERROR,
                                                            ),
        )

        # add background
        try:    
            bmp = wx.Image(BACKGROUND, type=wx.BITMAP_TYPE_ANY).Blur(10).ConvertToBitmap()
        except:
            print('could not open image ', BACKGROUND)
            wx.Exit()

        self.b_ground = wx.StaticBitmap(self, -1, bmp, (0, 0))
        

class MyBar(wx.MenuBar): 
    def __init__(self, frame):
        wx.MenuBar.__init__(self)

        frame.SetMenuBar(self)

        """ create file menu """
        file_menu = wx.Menu()
        file_menu.Append(id=wx.ID_ANY, item='New File')
        file_menu.Append(id=wx.ID_ANY, item='New Window')
        file_menu.AppendSeparator()
        file_menu.Append(id=wx.ID_ANY, item='Open...')

        open_recent_item = wx.Menu()
        open_recent_item.Append(id=wx.ID_ANY, item='from the past')
        open_recent_item.Append(id=wx.ID_ANY, item='from the future')
        open_recent_item.Append(id=wx.ID_ANY, item='from no-where')
        file_menu.Append(id=wx.ID_ANY, item='Open Recent', subMenu=open_recent_item)    # add submenu
        

        self.Append(file_menu, 'File')

        """ create help menu """
        help_menu = wx.Menu()
        help_menu.Append(id=wx.ID_ANY, item='Documentation')
        self.Append(help_menu, 'Help')
    

class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        wx.App.__init__(self, redirect=redirect, filename=filename)

    def OnInit(self):
        MyFrame()
        return True


def main():
    App().MainLoop()
    
if __name__=="__main__":
    main()