import os
import wx

from Graph.PCA.pca import PCAGraph as PCACont

class PCA_Import_View(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(PCA_Import_View, self).__init__(*args, **kwargs)
        self.pca_graph_instance = PCACont()
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(5, 4)
        self.butt_import_evec = None
        self.disp_evec_import_loc = None
        self.disp_evec_import_loc = None
        self.butt_import_phe = None
        self.disp_phe_import_loc =None
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.Show_Window()

    def Show_Window(self):
        self.SetSize((400, 300))
        self.SetTitle('Import PCA Files')
        self.Centre()


    ###Panel###


        self.butt_import_evec = wx.Button(self.panel, label="Import .evec file:") # button select data import location
        self.sizer.Add(self.butt_import_evec, pos=(0,0), flag=wx.LEFT, border=10)
        self.butt_import_evec.Bind(wx.EVT_BUTTON, self.PCA_import_evec)
        #self.Bind(wx.EVT_BUTTON,)

        self.disp_evec_import_loc = wx.TextCtrl(self.panel, value="", style = wx.TE_READONLY) # file path display
        self.sizer.Add(self.disp_evec_import_loc, pos=(0, 1), span=(1, 3), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        self.butt_import_phe = wx.Button(self.panel, label="Import .phe file: ") # button select phe import location
        self.sizer.Add(self.butt_import_phe, pos=(1, 0), flag=wx.LEFT, border=10)
        self.butt_import_phe.Bind(wx.EVT_BUTTON, self.PCA_import_phe)

        #self.Bind(wx.)

        self.disp_phe_import_loc = wx.TextCtrl(self.panel, value="", style=wx.TE_READONLY) # file path display
        self.sizer.Add(self.disp_phe_import_loc, pos=(1,1), span=(1,3), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        butt_ok = wx.Button(self.panel, label="Ok") # button continue generate graph
        self.sizer.Add(butt_ok, pos=(4,2), flag=wx.RIGHT|wx.BOTTOM, border=10)

        butt_no = wx.Button(self.panel, label="Cancel") # button cancel and quit
        self.sizer.Add(butt_no, pos=(4,3), flag=wx.RIGHT|wx.BOTTOM, border=10)

        butt_no.Bind(wx.EVT_BUTTON, self.On_Quit)

        self.sizer.AddGrowableCol(1)
        self.sizer.AddGrowableRow(2)
        self.panel.SetSizer(self.sizer)

    def On_Quit(self, e):
        self.Close()

    def PCA_import_evec(self, event):
        self.pca_graph_instance.importEvecFile()
        self.disp_evec_import_loc.write(self.pca_graph_instance.evecFilePath)

    def PCA_import_phe(self, event):
        self.pca_graph_instance.importPheFile()
        self.disp_phe_import_loc.write(self.pca_graph_instance.pheFilePath)
        # label = wx.StaticText(self.panel, label="PCA choice 1:", style=wx.ALIGN_CENTRE)
        # self.box.Add(label, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)

        
