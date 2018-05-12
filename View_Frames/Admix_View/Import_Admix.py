import os
import wx
import sys

from Graph.Admixture.AdmixtureInstance import AdmixController as AdmixCont

class Admix_Import_View(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Admix_Import_View, self).__init__(*args, **kwargs)

        self.ShowWindow()


    def ShowWindow(self):
        self.SetSize((400, 300))
        self.SetTitle('Import Admix Files')
        self.Centre


    ###Panel###
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 4)

        butt_import_data = wx.Button(panel, label="Import data file:") # button select data import location
        sizer.Add(butt_import_data, pos=(0,0), flag=wx.LEFT, border=10)
        self.Bind(wx.EVT_BUTTON, self.admix_import_data, butt_import_data)

        disp_data_import_loc = wx.TextCtrl(panel, value = "", style = wx.TE_READONLY) # file path display
        sizer.Add(disp_data_import_loc, pos=(0,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        butt_import_phe = wx.Button(panel, label="Import .phe file:") # button select phe import location
        sizer.Add(butt_import_phe, pos=(1,0), flag=wx.LEFT, border=10)
        self.Bind(wx.EVT_BUTTON, self.admix_import_phe, butt_import_phe)

        disp_phe_import_loc = wx.TextCtrl(panel, value = "", style = wx.TE_READONLY) # file path display
        sizer.Add(disp_phe_import_loc, pos=(1,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        butt_ok = wx.Button(panel, label="Ok") # button continue generate graph
        sizer.Add(butt_ok, pos=(4,2), flag=wx.RIGHT|wx.BOTTOM, border=10)

        butt_no = wx.Button(panel, label="Cancel") # button cancel and quit
        sizer.Add(butt_no, pos=(4,3), flag=wx.RIGHT|wx.BOTTOM, border=10)
        butt_no.Bind(wx.EVT_BUTTON, self.on_quit)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)


    def on_quit(self, e):
        self.Close()

    def admix_import_data(self, event):
        AdmixCont.importData(self)

    def admix_import_phe(self, event):
        AdmixCont.importPhe(self)


    #def Open_file(self, event):
        #dial_file_dir = wx.FileDialogue(
            #self, message="Choose your file",
            #defaultDir = self.currentDirectory,
            #defaultFile="",
            #wildcard=wildcard,
            #style=wx.FD_OPEN|wx.FD_CHANGE_DIR
            #)

        #if dial_file_dir.ShowModal == wx.ID_OK:
            #self.file_path = dial_file_dir.GetPath()
            #self.text_import_loc.SetValue(self.file_path)


        #butt_import_fam = wx.Button(panel, label="Import .phe file:") # button select fam import location
        #sizer.Add(butt_import_fam, pos=(2,0), flag=wx.LEFT, border=10)

        #disp_fam_import_loc = wx.TextCtrl(panel, value = "", style = wx.TE_READONLY) # file path display
        #sizer.Add(disp_fam_import_loc, pos=(2,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        #label_01 = wx.StaticText(panel, label="Import Settings")
        #sizer.Add(label_01, pos=(2,0), flag=wx.LEFT, border=5)

        

        
