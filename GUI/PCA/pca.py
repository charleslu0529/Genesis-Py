import matplotlib.pyplot as plt
import wx
import numpy as np
from collections import defaultdict

pca_evec_entries = defaultdict(list)

print("Select evec file\n")

app = wx.App()

wxFileChoiceFrame = wx.Frame(None , -1 , "win.py")
wxFileChoiceFrame.SetSize(0,0,200,50)

wxFileChoice = wx.FileDialog(wxFileChoiceFrame, "Open evec file", wildcard="evec files (*.evec)|*.evec", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
wxFileChoice.ShowModal()
filename = wxFileChoice.GetPath()

pca_file = open(filename, "r")

wxFileChoice = wx.FileDialog(wxFileChoiceFrame, "Open Phenotype file", wildcard="evec files (*.phe)|*.phe", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
wxFileChoice.ShowModal()
filename = wxFileChoice.GetPath()

phe_file = open(filename, "r")

for line in pca_file:
    datas = line.split()
    for idx, data in enumerate(datas):
        pca_evec_entries[idx].append(data)

number_of_pca = len(pca_evec_entries) - 1

print(pca_evec_entries)
print(number_of_pca)

# wxPcaChoiceFrame = wx.Frame(None, -1, "PCA Choice.py")
# wxPcaChoiceFrame.SetSize(0,0,50,25)

choices = []
for x in range(1,number_of_pca):
    choices.append(x)

# wxPcaChoice = wx.SingleChoiceDialog(None, "Choose data set 1", "pca.py", choices)
# wxPcaChoice.ShowModal()

# dataSet_1 = wxPcaChoice.GetSelection()
# print(dataSet_1)
shape = []
for values in pca_evec_entries[1]:
    shape.append(20)
print(shape)
plt.scatter(pca_evec_entries[1], pca_evec_entries[3],10, shape)
plt.show()
pca_file.close()