import os
import wx

class PCA_Import_View(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(PCA_Import_View, self).__init__(*args, **kwargs)

        self.Show_Window()


    def Show_Window(self):
        self.SetSize((400, 300))
        self.SetTitle('Import PCA Files')
        self.Centre


    ###Panel###
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 4)

        butt_import_evec = wx.Button(panel, label="Import .evec file:") # button select data import location
        sizer.Add(butt_import_evec, pos=(0,0), flag=wx.LEFT, border=10)
        #self.Bind(wx.EVT_BUTTON,)

        disp_evec_import_loc = wx.TextCtrl(panel, value = "", style = wx.TE_READONLY) # file path display
        sizer.Add(disp_evec_import_loc, pos=(0,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        butt_import_phe = wx.Button(panel, label="Import .phe file: ") # button select phe import location
        sizer.Add(butt_import_phe, pos=(1,0), flag=wx.LEFT, border=10)
        #self.Bind(wx.)

        disp_phe_import_loc = wx.TextCtrl(panel, value = "", style = wx.TE_READONLY) # file path display
        sizer.Add(disp_phe_import_loc, pos=(1,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        butt_ok = wx.Button(panel, label="Ok") # button continue generate graph
        sizer.Add(butt_ok, pos=(4,2), flag=wx.RIGHT|wx.BOTTOM, border=10)

        butt_no = wx.Button(panel, label="Cancel") # button cancel and quit
        sizer.Add(butt_no, pos=(4,3), flag=wx.RIGHT|wx.BOTTOM, border=10)
        butt_no.Bind(wx.EVT_BUTTON, self.OnQuit)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)


    def OnQuit(self, e):
        self.Close()
        
