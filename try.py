import wx

def customize_bar(bar):
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
    

    bar.Append(file_menu, 'File')

    """ create help menu """
    help_menu = wx.Menu()
    help_menu.Append(id=wx.ID_ANY, item='Documentation')
    bar.Append(help_menu, 'Help')

def customize_panel(panel):
    button = wx.Button(parent=panel, label='click me')
    button.Bind(
        event=wx.EVT_BUTTON,
        handler=create_dialog,
    )
    
def create_dialog(evt, text='hello'):
    wx.MessageBox(
        message=text,
        caption='this is a caption',
        style= wx.OK | wx.ICON_ERROR,
    )
    
    
def main():
    # app
    app = wx.App()

    # frame
    frame = wx.Frame(
        title='Hello wx',
        parent=None 
    ) 

    # panel
    panel = wx.Panel(parent=frame, pos=wx.RealPoint(53, 66))
    customize_panel(panel)

    # menu bar
    bar = wx.MenuBar()
    frame.SetMenuBar(bar)
    customize_bar(bar)

    # run
    frame.Show()
    app.MainLoop()

if __name__=="__main__":
    main()