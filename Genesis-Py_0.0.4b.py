# Genesis-Py v0.0.4a
# UI Design: Nandi, 1064787

import os
import wx
APP_EXIT = 1

name = 'Genesis-Py_v0.0.4a' # GenesisPy version name

class App_Main_Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(App_Main_Frame, self).__init__(*args, **kwargs)

        self.InitUI()


    def InitUI(self):
        menubar = wx.MenuBar()
        toolbar = self.CreateToolBar()

        self.SetSize((800, 600))
        self.SetTitle(name)
        self.Centre

        ###Panel###
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)

        text = wx.StaticText(panel, label="Panel Test")
        sizer.Add(text, pos = (0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        text_ctl = wx.TextCtrl(panel)
        sizer.Add(text_ctl, pos=(1,0), span=(1,5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        buttonOK = wx.Button(panel, label="Ok", size=(90,28))
        sizer.Add(buttonOK, pos=(3,3))
        buttonClose = wx.Button(panel, label="Close", size=(90,28))
        sizer.Add(buttonClose, pos=(3,4), flag=wx.RIGHT|wx.BOTTOM, border=10)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)

        #####TOOLBAR#####
        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Undo', wx.Bitmap('./icons/undo_A.bmp'))
        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Redo', wx.Bitmap('./icons/redo_A.bmp'))

        tool_bar_prime = toolbar.AddSeparator() # vertical separator

        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Save', wx.Bitmap('./icons/save.bmp'))
        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Open File', wx.Bitmap('./icons/open.bmp'))

        tool_bar_prime = toolbar.AddSeparator() # vertical separator

        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Import Admix', wx.Bitmap('./icons/importAdmix.bmp'))
        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Import PCA', wx.Bitmap('./icons/importPCA.bmp'))

        tool_bar_prime = toolbar.AddSeparator() # vertical separator

        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Settings', wx.Bitmap('./icons/settings.bmp'))
        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Search', wx.Bitmap('./icons/search.bmp'))
        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Export Image', wx.Bitmap('./icons/exportPicture.bmp'))
        tool_bar_prime = toolbar.AddTool(wx.ID_ANY, 'Add', wx.Bitmap('./icons/addArrow.bmp'))
        #self.Bind(wx.EVT_TOOL, self.OnQuit, tool_bar_prime)

        toolbar.Realize() # Obligatory method to Windows


        #####MENUS and SUBMENUS#####
        menu_file = wx.Menu()

        quit_menu_item = wx.MenuItem(menu_file, APP_EXIT, '&Quit\tCtrl+Q')
        quit_menu_item.SetBitmap(wx.Bitmap('./icons/exit.bmp'))

        import_sub_menu = wx.Menu()
        import_sub_menu.Append(wx.ID_ANY, '&Import Admixture data')
        import_sub_menu.Append(wx.ID_ANY, '&Import PCA data')

        menu_file.Append(wx.ID_NEW, '&New')
        menu_file.Append(wx.ID_ANY, '&Import', import_sub_menu)
        menu_file.Append(wx.ID_SAVE, '&Save')
        menu_file.Append(wx.ID_SAVEAS, '&Save as ...')

        menu_file.AppendSeparator() # horizontal menu separator

        menu_file.Append(quit_menu_item)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(menu_file, '&File') # adds above menu elements to the menubar
        self.SetMenuBar(menubar)


    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = App_Main_Frame(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
