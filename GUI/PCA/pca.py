import matplotlib.pyplot as plt
import wx
import numpy as np
import random
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

eigenValues = []

for line in pca_file:
    datas = line.split()
    print("Datas = ",datas)
    if "#eigvals" in datas[0]:
        for data in datas:
            eigenValues.append(data)
    else:
        for idx, data in enumerate(datas):
            pca_evec_entries[idx].append(data)

print("Eigenvalues: ",eigenValues,"\n")

number_of_pca = len(pca_evec_entries) - 1

phe_entries = defaultdict(list)


for line in phe_file:
    datas = line.split()
    for idx, data in enumerate(datas):
        phe_entries[idx].append(data)

print("PCA Evec entries ",pca_evec_entries,"\n")
print("number of pca: ",number_of_pca)

# wxPcaChoiceFrame = wx.Frame(None, -1, "PCA Choice.py")
# wxPcaChoiceFrame.SetSize(0,0,50,25)

choices = []
for x in range(1,number_of_pca):
    choices.append(x)

choice_1 = choices[0]
choice_2 = choices[1]
# wxPcaChoice = wx.SingleChoiceDialog(None, "Choose data set 1", "pca.py", choices)
# wxPcaChoice.ShowModal()

# dataSet_1 = wxPcaChoice.GetSelection()
# print(dataSet_1)

print("pca_evec_entries[0] = ", pca_evec_entries[0],"\n")
print("phe Entries = ", phe_entries[0],"\n")
print("pca entry with Choice 2 = ", pca_evec_entries[choice_2],"\n")
shape = []

# common_entries = set(pca_evec_entries[0]).)
# print("Common Entries: ", common_entries)
# for idx, value in range(1,number_of_pca):
#     code = pca_evec_entries[idx].split(":")


# for number in range(1,number_of_pca):
#     for value in pca_evec_entries[number-1]:
#         for type in phe_entries[0]:
#             if type in value:
#                 shape.append(pca_evec_entries[choice_2])

print("shape = ",shape)

# plt.scatter(pca_evec_entries[choice_1], pca_evec_entries[choice_2],10, shape)
print("creating scatter plot with pca_evec_entries[choice_2] as shape\n")

plt.scatter(pca_evec_entries[choice_1], pca_evec_entries[choice_2],10, pca_evec_entries[choice_2])

print(pca_evec_entries[0])
ymin = 0
ymax = len(pca_evec_entries[choice_2])
ystep = int(len(pca_evec_entries[choice_2])/20)

xmin = ymin
xmax = len(pca_evec_entries[choice_1])
xstep = int(len(pca_evec_entries[choice_1])/20)

# print("ystep = ", ystep)
# print("ymin = ", ymin)
# print("ymax = ", ymax,"\n")
# print("xstep = ",xstep)
# print("xmin = ", xmin)
# print("xmax = ", xmax,"\n")

plt.yticks(np.arange(ymin, ymax, ystep))
plt.xticks(np.arange(xmin, xmax ,xstep))
plt.show()
pca_file.close()