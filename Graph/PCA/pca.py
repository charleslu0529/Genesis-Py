import matplotlib.pyplot as plt
import wx
import numpy as np
from collections import defaultdict
from matplotlib.patches import Patch

class PCAGraph:

    app = wx.App()

    def __init__(self):
        self.pca_evec_entries = defaultdict(list)
        self.phe_entries = defaultdict(list)
        self.evec_file = None
        self.phe_file = None
        self.eigenValues = []
        self.controlList = []
        self.number_of_pca = 0
        self.choice_1 = 0
        self.choice_2 = 0
        self.choiceLen = None
        self.graphType = "PCA"
        # these are the column choices from the phenotype file. to get data you will need to run readFile()
        self.choiceList = []

        # these are the file directory string
        self.evecFilePath = ""
        self.pheFilePath = ""
        self.colours = []
        self.idList = []
        self.geoGroup_micro = ""
        self.dotColour = np.random.rand(3, )
        self.groupColour = {}

    def get_choice_list(self):
        return self.choiceList
    def get_number_of_pca(self):
        return self.number_of_pca

    def importEvecFile(self):
        wxFileChoiceFrame = wx.Frame(None, -1, "win.py")
        wxFileChoiceFrame.SetSize(0, 0, 200, 50)
        # print("Select evec file\n")
        wxFileChoice = wx.FileDialog(wxFileChoiceFrame, "Open Evec file", wildcard="evec files (*.evec)|*.evec", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        wxFileChoice.ShowModal()
        self.evecFilePath = wxFileChoice.GetPath()
        print("evecFilePath = ",self.evecFilePath)
        self.evec_file = open(self.evecFilePath, "r+")

        line = self.evec_file.readline()
        data = line.split()
        self.choiceLen = len(data)

        for x in range(1, self.choiceLen):
            label = "PCA " + str(x)
            self.choiceList.append(label)

        wxFileChoice.Destroy()

    def importPheFile(self):
        wxFileChoiceFrame = wx.Frame(None, -1, "win.py")
        wxFileChoiceFrame.SetSize(0, 0, 200, 50)
        wxFileChoice = wx.FileDialog(wxFileChoiceFrame, "Open Phenotype file", wildcard="phe files (*.phe)|*.phe", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        wxFileChoice.ShowModal()
        self.pheFilePath = wxFileChoice.GetPath()
        self.phe_file = open(self.pheFilePath, "r+")

        wxFileChoice.Destroy()

    def readFiles(self):
        for line in self.evec_file:
            datas = line.split()
            # print("Datas = ",datas)
            if "#eigvals" in datas:
                for data in datas:
                    self.eigenValues.append(data)
            else:
                for idx, data in enumerate(datas):
                    if "Control" in data:
                        self.controlList.append(data)
                    else:
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
        self.choice_1 = user_choice_1 + 1
        self.choice_2 = user_choice_2 + 1

    def initGroupColour(self):

        self.colours = []

        # print("len(idList) = ", len(self.idList), "\n")
        for value in range(0, len(self.idList)):

            id = self.idList[value].split(":")

            # for idx, content in enumerate(self.phe_entries):

            # if all(elem in self.phe_entries[0] for elem in id) or all():

            if id[0] in self.phe_entries[0]:

                position = self.phe_entries[0].index(id[0])
                # print("position = ", position)
                # print("self.geoGroup_micro = ", self.geoGroup_micro)
                # print("self.phe_entries[2][position] = ", self.phe_entries[2][position], "\n")
                if self.geoGroup_micro == self.phe_entries[2][position]:

                    self.colours.append(self.dotColour)
                else:
                    self.geoGroup_micro = self.phe_entries[2][position]

                    # print("self.geoGroup_micro = ", self.geoGroup_micro)

                    if self.geoGroup_micro in self.groupColour:

                        self.dotColour = self.groupColour[self.geoGroup_micro]

                    else:

                        self.dotColour = np.random.rand(3, ).tolist()

                        while all(elem in self.groupColour for elem in self.dotColour):
                            self.dotColour = np.random.rand(3, ).tolist()
                        self.groupColour[self.geoGroup_micro] = self.dotColour
                        # print("self.groupColour[self.geoGroup_micro] = ", self.groupColour[self.geoGroup_micro])
                        self.colours.append(self.dotColour)
            else:
                print(id[0], " is missing\n")

    def changeGroupColour(self, group_name, new_colour):
        self.groupColour[group_name] = new_colour
        self.initGroupColour()
        plt.close()
        # plt.scatter(self.pca_evec_entries[self.choice_1], self.pca_evec_entries[self.choice_2], 10, self.shape)
        self.plotScatter()
        plt.show()

    def pickColour(self, group_name):
        wxColourPicker = wx.ColourDialog(wx.Frame(None, -1, "win.py"))
        wxColourPicker.ShowModal()
        new_colour = wxColourPicker.GetColourData().GetColour().GetAsString(flags=4)

        self.changeGroupColour(group_name, new_colour)

    def plotScatter(self):

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        # for idx, data in enumerate(self.pca_evec_entries[self.choice_1]):
        # for group, colour in self.groupColour:
            # if all(elem in self.groupColour for elem in self.colours[idx]):
                # this_label = next((k for k, v in self.groupColour.items() if v == self.colours[idx]), None)
            # print("self.colours[idx] = ", self.colours[idx])
            # print("self.groupColour = ", self.groupColour, "\n")
            # this_label = ""
            # for key, value in self.groupColour.items():
            #     if self.colours[idx] == value:
            #         this_label = key
        print("plotting with choice_1 = ", self.choice_1, " and choice_2 = ", self.choice_2)
        ax.scatter(self.pca_evec_entries[self.choice_1], self.pca_evec_entries[self.choice_2], alpha=1, c=self.colours, s=10)
        # legend_elements = []
        # for group in self.groupColour:
        #     print("group = ", group, "\n")
        #     legend_elements.append(Patch(facecolor=self.groupColour[group], edgecolor='r', label=group))
        # print("legend_elements = ", legend_elements, "\n")
        # ax.legend(handles=legend_elements, loc='upper right')
        # print("list(self.groupColour.keys()) = ",list(self.groupColour.keys()))
        plt.title('PCA Chart')
        plt.legend(loc=2)

        # plt.scatter(self.pca_evec_entries[self.choice_1], self.pca_evec_entries[self.choice_2], 10, self.shape)
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

    def LoadGraph(self, genFile):
        self.__init__()

        self.graphType = genFile.readline()

        num_of_pca = genFile.readline()
        num_of_phe = genFile.readline()

        for x in range(1, num_of_pca):
            listed_line = genFile.readline().split(",")
            self.pca_evec_entries[listed_line[0]] = listed_line[1]

        for x in range(1, num_of_phe):
            listed_line = genFile.readline().split(",")
            self.phe_entries[listed_line[0]] = listed_line[1]

        self.colours = genFile.readline().split(",")

        self.controlList = genFile.readline().split(",")

        self.choice_1 = genFile.readline()

        self.choice_2 = genFile.readline()

        self.idList = genFile.readline().split(",")

        self.evecFilePath = genFile.readline()

        self.pheFilePath = genFile.readline()

        self.plotScatter()

        genFile.close()

    def saveGraph(self, saveFile):

        saveFile.write("PCA\n")

        saveFile.write(len(self.pca_evec_entries))
        saveFile.write("\n")
        saveFile.write(len(self.phe_entries))
        saveFile.write("\n")
        pca_entries_keys = self.pca_evec_entries.keys()
        pca_entries_values = self.pca_evec_entries.keys()

        for idx, values in pca_entries_keys:
            saveFile.write(pca_entries_keys[idx], ",", pca_entries_values[idx], "\n")

        phe_entries_keys = self.phe_entries.keys()
        phe_entries_values = self.phe_entries.values()

        for idx, values in phe_entries_keys:
            saveFile.write(phe_entries_keys[idx], ",", phe_entries_values[idx], "\n")

        group_colour_keys = self.groupColour.keys()
        group_colour_values = self.groupColour.values()

        for idx, values in group_colour_keys:
            saveFile.write(group_colour_keys[idx], ",", group_colour_values[idx], "\n")

        for idx, value in self.colours:
            if idx == 0:
                saveFile.write(value)
            else:
                saveFile.write(",", value)
        saveFile.write("\n")

        for idx, value in self.controlList:
            if idx == 0:
                saveFile.write(value)
            else:
                saveFile.write(",", value)
        saveFile.write("\n")

        saveFile.write(self.choice_1)
        saveFile.write("\n")
        saveFile.write(self.choice_2)
        saveFile.write("\n")

        for idx,value in self.idList:
            if idx == 0:
                saveFile.write(value)
            else:
                saveFile.write(",", value)
        saveFile.write("\n")

        saveFile.write(self.evecFilePath)
        saveFile.write("\n")
        saveFile.write(self.pheFilePath)

        saveFile.close()


    def OnSaveAs(self):

        # Here we construct a save as dialogue box
        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 175, 60)

        with wx.FileDialog(frame, "Save current work in GEN file", wildcard="GEN files (*.gen)|*.gen", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as SaveAsDlg:

            if SaveAsDlg.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind, thus we will not do anything

            # save the current contents in the file
            savePath = SaveAsDlg.GetPath()
            try:
                with open(savePath, 'w') as saveFile:
                    self.saveGraph(saveFile)
            except IOError:
                wx.LogError("Cannot save current data in file " + savePath + "." % savePath)
