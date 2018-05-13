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
        self.drop_down_box_1 = None
        self.drop_down_box_2 = None
        self.choiceList = ["None"]
        self.choice_1 = 0
        self.choice_2 = 0
        self.label = ""
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

        self.drop_down_box_1 = wx.Choice(self.panel, choices=self.choiceList, style=0, name="Column Selection")
        self.sizer.Add(self.drop_down_box_1, pos=(2, 0), flag=wx.LEFT, border=10)

        self.drop_down_box_2 = wx.Choice(self.panel, choices=self.choiceList, style=0, name="Column Selection")
        self.sizer.Add(self.drop_down_box_2, pos=(2, 1), flag=wx.LEFT, border=10)

        butt_ok = wx.Button(self.panel, label="Ok") # button continue generate graph
        self.sizer.Add(butt_ok, pos=(4,2), flag=wx.RIGHT|wx.BOTTOM, border=10)
        butt_ok.Bind(wx.EVT_BUTTON, self.completeImport)

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
        self.disp_evec_import_loc.Clear()
        self.disp_evec_import_loc.write(self.pca_graph_instance.evecFilePath)

        self.drop_down_box_1.Clear()
        self.drop_down_box_1.Append(self.pca_graph_instance.choiceList)

        self.drop_down_box_2.Clear()
        self.drop_down_box_2.Append(self.pca_graph_instance.choiceList)

    def PCA_import_phe(self, event):
        self.pca_graph_instance.importPheFile()
        self.disp_phe_import_loc.Clear()
        self.disp_phe_import_loc.write(self.pca_graph_instance.pheFilePath)

    def completeImport(self, event):

        self.choice_1 = self.drop_down_box_1.GetSelection()
        self.choice_2 = self.drop_down_box_2.GetSelection()
        print("choice_1 = ", self.choice_1)
        print("choice_2 = ", self.choice_2)
        print("choiceList = ", self.pca_graph_instance.choiceList)

        choice_1_string = "PCA " + str(self.choice_1)
        choice_2_string = "PCA " + str(self.choice_2)

        if choice_1_string and choice_2_string in self.pca_graph_instance.choiceList:  #the value of colNum would be -1 if nothing was selected, but we add 2 to it to  get the correct column
            self.pca_graph_instance.choosePCA(self.choice_1, self.choice_2)
            self.pca_graph_instance.readFiles()
            self.pca_graph_instance.initGroupColour()
            self.pca_graph_instance.plotScatter()

        else:
            errorMessage = wx.MessageDialog(None, "Please select the 2 data sets to plot with.", caption="One of these files was not selected.", style=1)
            errorMessage.ShowModal()

        self.drop_down_box_1.Clear()
        self.drop_down_box_2.Clear()
        self.Close()