import os
import wx
import sys

from Graph.Admixture.AdmixtureInstance import AdmixController as AdmixCont

class Admix_Import_View(wx.Frame):

    choiceList = []

    def __init__(self, *args, **kwargs):
        super(Admix_Import_View, self).__init__(*args, **kwargs)

        self.ShowWindow()

        AdmixCont.__init__(AdmixCont)

        self.choiceList = ["None"]
        self.colNum = 0

    def ShowWindow(self):
        self.SetSize((400, 300))
        self.SetTitle('Import Admix Files')
        self.Centre


    ###Panel###
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(5, 4)

        butt_import_data = wx.Button(self.panel, label="Import data file:") # button select data import location
        self.sizer.Add(butt_import_data, pos=(0,0), flag=wx.LEFT, border=10)
        self.Bind(wx.EVT_BUTTON, self.admix_import_data, butt_import_data)

        self.disp_data_import_loc = wx.TextCtrl(self.panel, value = "", style = wx.TE_READONLY) # file path display
        self.sizer.Add(self.disp_data_import_loc, pos=(0,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        butt_import_phe = wx.Button(self.panel, label="Import .phe file:") # button select phe import location
        self.sizer.Add(butt_import_phe, pos=(1,0), flag=wx.LEFT, border=10)
        self.Bind(wx.EVT_BUTTON, self.admix_import_phe, butt_import_phe)

        self.disp_phe_import_loc = wx.TextCtrl(self.panel, value = "", style = wx.TE_READONLY) # file path display
        self.sizer.Add(self.disp_phe_import_loc, pos=(1,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        self.dropDownBox = wx.Choice(self.panel, choices=self.choiceList, style=0, name="Column Selection")
        self.sizer.Add(self.dropDownBox, pos=(2, 0), flag=wx.LEFT, border=10)

        butt_ok = wx.Button(self.panel, label="Ok") # button continue generate graph
        self.sizer.Add(butt_ok, pos=(4,2), flag=wx.RIGHT|wx.BOTTOM, border=10)
        butt_ok.Bind(wx.EVT_BUTTON, self.completeImport)

        butt_no = wx.Button(self.panel, label="Cancel") # button cancel and quit
        self.sizer.Add(butt_no, pos=(4,3), flag=wx.RIGHT|wx.BOTTOM, border=10)
        butt_no.Bind(wx.EVT_BUTTON, self.on_quit)

        self.sizer.AddGrowableCol(1)
        self.sizer.AddGrowableRow(2)
        self.panel.SetSizer(self.sizer)


    def on_quit(self, event):
        self.dropDownBox.Clear()
        self.Close()

    def admix_import_data(self, event):
        AdmixCont.importData(AdmixCont)

        # This writes the file path into the display box next to the import button
        self.disp_data_import_loc.write(AdmixCont.getDataPath(AdmixCont))

    def admix_import_phe(self, event):
        AdmixCont.importPhe(AdmixCont)

        # This writes the file path into the display box next to the import button
        self.disp_phe_import_loc.write(AdmixCont.getPhePath(AdmixCont))

        self.choiceList = AdmixCont.getChoiceList(AdmixCont)

        self.dropDownBox.Clear()
        self.dropDownBox.Append(self.choiceList)

    def completeImport(self, event):

        self.colNum = self.dropDownBox.GetSelection() + 2

        dataSelected = AdmixCont.getDataSelected(AdmixCont)
        pheSelected = AdmixCont.getPheSelected(AdmixCont)

        if dataSelected == True and pheSelected == True and self.colNum != 1:  #the value of colNum would be -1 if nothing was selected, but we add 2 to it to  get the correct column
            AdmixCont.drawGraph(AdmixCont, self.colNum)

        elif dataSelected == False or pheSelected == False:
            errorMessage = wx.MessageDialog(None, "Please select both a data file and a .phe file",
                                            caption="One of these files was not selected", style=1)
            errorMessage.ShowModal()

        elif self.colNum == 1:
            errorMessage = wx.MessageDialog(None, "Please select a column to label with from the drop down",
                                            caption="A column was not selected", style=1)
            errorMessage.ShowModal()

        self.dropDownBox.Clear()
        self.Close()

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

        

        
