import matplotlib.pyplot as plt
import wx
import numpy as np
from collections import defaultdict


class PCAGraph:

    app = wx.App()

    def __init__(self):
        self.pca_evec_entries = defaultdict(list)
        self.phe_entries = defaultdict(list)
        self.evec_file = None
        self.phe_file = None
        self.eigenValues = []
        self.number_of_pca = 0
        self.choiceLen = None
        # these are the column choices from the phenotype file. to get data you will need to run readFile()
        self.choiceList = []

        # these are the file directory string
        self.evecFilePath = ""
        self.pheFilePath = ""

        self.shape = []
        self.idList = []
        self.geoGroup_micro = ""
        self.dotColour = np.random.rand(3, )
        self.groupColour = {}

    def importEvecFile(self):
        wxFileChoiceFrame = wx.Frame(None, -1, "win.py")
        wxFileChoiceFrame.SetSize(0, 0, 200, 50)
        # print("Select evec file\n")
        wxFileChoice = wx.FileDialog(wxFileChoiceFrame, "Open Evec file", wildcard="evec files (*.evec)|*.evec", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        wxFileChoice.ShowModal()
        self.evecFilePath = wxFileChoice.GetPath()
        self.evec_file = open(self.evecFilePath, "r+")

    def importPheFile(self):
        wxFileChoiceFrame = wx.Frame(None, -1, "win.py")
        wxFileChoiceFrame.SetSize(0, 0, 200, 50)
        wxFileChoice = wx.FileDialog(wxFileChoiceFrame, "Open Phenotype file", wildcard="phe files (*.phe)|*.phe", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        wxFileChoice.ShowModal()
        self.pheFilePath = wxFileChoice.GetPath()
        self.phe_file = open(self.pheFilePath, "r+")

        line = self.evec_file.readline()
        data = line.split()
        self.choiceLen = len(data)

        for x in range(1, self.choiceLen):
            self.choiceList.append(x)

    def readFiles(self):
        for line in self.evec_file:
            datas = line.split()
            # print("Datas = ",datas)
            if "#eigvals" in datas[0]:
                for data in datas:
                    self.eigenValues.append(data)
            else:
                for idx, data in enumerate(datas):
                    self.pca_evec_entries[idx].append(data)

        for line in self.phe_file:
            datas = line.split()
            for idx, data in enumerate(datas):
                self.phe_entries[idx].append(data)

        self.idList = self.pca_evec_entries[0]
        self.number_of_pca = len(self.pca_evec_entries) - 1

    def choosePCA(self, user_choice_1, user_choice_2):

        # wxFrame = wx.Frame()
        # panel = wx.Panel(wxFrame)
        # box = wx.BoxSizer(wx.VERTICAL)
        # label = wx.StaticText(panel, label="PCA choice 1:", style=wx.ALIGN_CENTRE)
        # box.Add(label, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10)
        #
        # combo_1 = wx.ComboBox(panel, self.choiceList)
        # box.Add(combo_1, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        #
        # label_2 = wx.StaticText(panel, label="PCA choice 2:", style=wx.ALIGN_CENTRE)
        # box.Add(label_2, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        #
        # combo_2 = wx.ComboBox(panel, self.choiceList)
        # box.Add(combo_2, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        #
        # panel.SetSizer(box)
        #
        # wxFrame.Show()

        # use wxpython to create dropdown for pca choices to plot
        self.choice_1 = self.choiceList[user_choice_1 - 1]
        self.choice_2 = self.choiceList[user_choice_2 - 1]

    def initGroupColour(self):
        self.shape = []
        for value in range(0, len(self.idList)):
            id = self.idList[value].split(":")
            for idx, content in enumerate(self.phe_entries):
                if all(elem in self.phe_entries[idx] for elem in id):
                    position = self.phe_entries[idx].index(id[0])
                    if self.geoGroup_micro == self.phe_entries[2][position]:
                        self.shape.append(self.dotColour)
                    else:
                        self.geoGroup_micro = self.phe_entries[2][position]
                        if self.geoGroup_micro in self.groupColour:
                            self.dotColour = self.groupColour[self.geoGroup_micro]
                        else:
                            self.dotColour = np.random.rand(3, )
                            while all(elem in self.groupColour for elem in self.dotColour):
                                self.dotColour = np.random.rand(3, )
                                self.groupColour[self.geoGroup_micro] = self.dotColour
                                self.shape.append(self.dotColour)

    def changeGroupColour(self, group_name, new_colour):
        self.groupColour[group_name] = new_colour
        self.initGroupColour()
        plt.close()
        plt.scatter(self.pca_evec_entries[self.choice_1], self.pca_evec_entries[self.choice_2], 10, self.shape)
        plt.show()

    def pickColour(self):
        wxColourPicker = wx.ColourDialog(wx.Frame(None, -1, "win.py"))
        wxColourPicker.ShowModal()

        new_colour = wxColourPicker.GetColourData().GetColour()
        print(new_colour)

        self.changeGroupColour("CHD", new_colour)

    def plotScatter(self):
        plt.scatter(self.pca_evec_entries[self.choice_1], self.pca_evec_entries[self.choice_2], 10, self.shape)
        ymin = 0
        ymax = len(self.pca_evec_entries[self.choice_2])
        ystep = int(len(self.pca_evec_entries[self.choice_2]) / 20)

        xmin = ymin
        xmax = len(self.pca_evec_entries[self.choice_1])
        xstep = int(len(self.pca_evec_entries[self.choice_1]) / 20)
        plt.yticks(np.arange(ymin, ymax, ystep))
        plt.xticks(np.arange(xmin, xmax, xstep))
        plt.show()
        self.evec_file.close()
        self.phe_file.close()

pcaGrapher = PCAGraph()

