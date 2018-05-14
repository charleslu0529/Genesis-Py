# Genesis-Py v0.0.8a
# UI Design: Nandi, 1064787

import os
import wx
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

APP_EXIT = 1
name = 'Genesis-Py_v0.0.8a' # GenesisPy version name

from View_Frames.Admix_View.Import_Admix import Admix_Import_View as AdmixImport
from View_Frames.PCA_View.Import_PCA import PCA_Import_View as PCAImport
from View_Frames.Future_Features import Msg_Feature_Frame as FSM
from View_Frames.Setting import Settings_Frame as SF


class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        # self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
       # self.sizer = wx.BoxSizer(wx.VERTICAL)
       # self.sizer.Add(self.canvas, 1, wx.CENTER | wx.TOP | wx.GROW)
        #self.SetSizer(self.sizer)
       # self.Fit()

    # def draw(self):
    #     t = arange(0.0, 3.0, 0.01)
    #     s = sin(2 * pi * t)
    #     self.axes.plot(t, s)

class App_Main_Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(App_Main_Frame, self).__init__(*args, **kwargs)

        self.graphPanel = wx.Panel()
        self.graphPanel.fig = Figure()
        self.graphPanel.axes = None
        self.panel = None

        self.InitUI()




    def InitUI(self):
        menubar = wx.MenuBar()
        toolbar = self.CreateToolBar()

        self.SetSize((800, 600))
        self.SetTitle(name)
        self.Centre()

        ###PANEL###
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(4, 4)

        self.graphPanel = wx.Panel(self.panel)
        self.graphPanel.fig = Figure()
        self.graphPanel.canvas = FigureCanvas(self.graphPanel, -1, self.graphPanel.fig)
        self.graphPanel.axes = self.graphPanel.fig.add_subplot(111)


        self.sizer.Add(self.graphPanel, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.RIGHT,  border=5, span=(4,4))

        # text = wx.StaticText(panel, label="") # Graphing output
        # sizer.Add(text, pos = (0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        #
        # text_ctl = wx.TextCtrl(panel)
        # sizer.Add(text_ctl, pos=(1,0), span=(1,5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)
        #
        # buttonOK = wx.Button(panel, label="Ok", size=(90,28))
        # sizer.Add(buttonOK, pos=(3,3))
        # buttonClose = wx.Button(panel, label="Close", size=(90,28))
        # sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT|wx.BOTTOM, border=10)

        self.sizer.AddGrowableCol(1)
        self.sizer.AddGrowableRow(2)
        self.panel.SetSizer(self.sizer)
        # self.graphPanel.SetSizer(self.sizer)


        #####TOOLBAR#####
        tool_bar_undo = toolbar.AddTool(wx.ID_ANY, 'Undo', wx.Bitmap('./icons/undo_A.bmp')) # undo button, not implemented
        self.Bind(wx.EVT_TOOL, self.Show_FM, tool_bar_undo)
        
        tool_bar_redo = toolbar.AddTool(wx.ID_ANY, 'Redo', wx.Bitmap('./icons/redo_A.bmp')) # redo button
        self.Bind(wx.EVT_TOOL, self.Show_FM, tool_bar_redo)

        tool_bar_prime = toolbar.AddSeparator() # vertical separator

        tool_bar_save = toolbar.AddTool(wx.ID_ANY, 'Save', wx.Bitmap('./icons/save.bmp')) # save button
        self.Bind(wx.EVT_TOOL, self.Show_FM, tool_bar_save)
        
        tool_bar_open = toolbar.AddTool(wx.ID_ANY, 'Open File', wx.Bitmap('./icons/open.bmp')) # open file button
        self.Bind(wx.EVT_TOOL, self.Show_FM, tool_bar_open)

        tool_bar_prime = toolbar.AddSeparator() # vertical separator

        tool_bar_admix = toolbar.AddTool(wx.ID_ANY, 'Import Admix', wx.Bitmap('./icons/importAdmix.bmp')) # admix data import button
        self.Bind(wx.EVT_TOOL, self.Admix_Import, tool_bar_admix)
        
        tool_bar_pca = toolbar.AddTool(wx.ID_ANY, 'Import PCA', wx.Bitmap('./icons/importPCA.bmp')) # pca data import button
        self.Bind(wx.EVT_TOOL, self.PCA_Import, tool_bar_pca)

        tool_bar_prime = toolbar.AddSeparator() # vertical separator

        tool_bar_settings = toolbar.AddTool(wx.ID_ANY, 'Settings', wx.Bitmap('./icons/settings.bmp')) # settings button
        self.Bind(wx.EVT_TOOL, self.show_setting_dialogue, tool_bar_settings)
        
        tool_bar_search = toolbar.AddTool(wx.ID_ANY, 'Search', wx.Bitmap('./icons/search.bmp')) # search button
        self.Bind(wx.EVT_TOOL, self.Show_FM, tool_bar_search)
        
        tool_bar_export = toolbar.AddTool(wx.ID_ANY, 'Export Image', wx.Bitmap('./icons/exportPicture.bmp')) # image export button
        self.Bind(wx.EVT_TOOL, self.Show_FM, tool_bar_export)
        
        tool_bar_elem = toolbar.AddTool(wx.ID_ANY, 'Add', wx.Bitmap('./icons/addArrow.bmp')) # add elem button, do we still need this?
        self.Bind(wx.EVT_TOOL, self.Show_FM, tool_bar_elem)

        toolbar.Realize() # Obligatory method to Windows only


        #####MENUS and SUBMENUS#####
        menu_file = wx.Menu()

        quit_menu_item = wx.MenuItem(menu_file, APP_EXIT, '&Quit\tCtrl+Q') # menu exit
        quit_menu_item.SetBitmap(wx.Bitmap('./icons/exit.bmp'))

        import_sub_menu = wx.Menu()
        menu_admix_import = import_sub_menu.Append(wx.ID_ANY, '&Import Admixture data') # menu admix import
        self.Bind(wx.EVT_MENU, self.Admix_Import, menu_admix_import)

        menu_pca_import = import_sub_menu.Append(wx.ID_ANY, '&Import PCA data') # menu PCA import
        self.Bind(wx.EVT_MENU, self.PCA_Import, menu_pca_import)

        menu_new_file = menu_file.Append(wx.ID_NEW, '&New') # menu new
        self.Bind(wx.EVT_MENU, self.Show_FM, menu_new_file)
        
        menu_file.Append(wx.ID_ANY, '&Import', import_sub_menu)
        
        menu_save = menu_file.Append(wx.ID_SAVE, '&Save') # menu save
        self.Bind(wx.EVT_MENU, self.Show_FM, menu_save)
        
        menu_save_as = menu_file.Append(wx.ID_SAVEAS, '&Save as ...') # menu save as
        self.Bind(wx.EVT_MENU, self.Show_FM, menu_save_as)

        menu_file.AppendSeparator() # horizontal menu separator

        menu_file.Append(quit_menu_item) # menu quit
        self.Bind(wx.EVT_MENU, self.On_Quit, id=APP_EXIT)

        menubar.Append(menu_file, '&File') # adds above menu elements to the menubar
        self.SetMenuBar(menubar)


    #####GENERAL FUNCTIONS#####
    def On_Quit(self, e):
        self.Close()

    def Show_FM(self, e):
        self.child = FSM(self, title="Note")
        self.child.Show()

    def show_setting_dialogue(self, e):
        self.child = SF(self, title="Settings")
        self.child.Show()

    def Admix_Import(self, e):
        self.child = AdmixImport(self, title="Import Admix Data")
        # AdmixImport.axes = self.graphPanel.axes

        self.child.Show()

    def PCA_Import(self, e):
        self.child = PCAImport(self, title="Import PCA Data")
        self.child.Show()


    #####TOOLBAR FUNCTIONS#####
    #####MENU and SUBMENU FUNCTIONS#####


def main():
    app = wx.App()
    ex = App_Main_Frame(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
