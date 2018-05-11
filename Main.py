import matplotlib.pyplot as plt
import numpy as np
import wx

# x=[1,2,3,4,5,6,7,8,9]
# y=[1.1,0.8,0.9,1,1.2,1.1,1.3,1.5,1.6]
# plt.plot(x,y)
# plt.show()


# N = 5
# menMeans = (20, 35, 30, 35, 27)
# womenMeans = (22, 28, 33, 25, 25)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (1, 2, 3, 4, 5)
#
# ind = np.arange(N)  #the x locations for the groups
# width = 0.35 #width of bars: can also be len(x) sequence

#p1 = plt.bar(ind, menMeans, width, yerr=menStd)
#p2 = plt.bar(ind, womenMeans, width, yerr=womenStd)

#p1= plt.stackplot()




# plt.ylabel('Scores')
# plt.title('Scores by group and gender')
# plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
# plt.yticks(np.arange(0, 81, 10))
# plt.legend((p1[0], p2[0]), ('Men', 'Women'))
#
# plt.show()



# import wx
#
# def ask(parent=None, message='', default_value=''):
#     dlg = wx.TextEntryDialog(parent, message, value=default_value)
#     dlg.ShowModal()
#     result = dlg.GetValue()
#     dlg.Destroy()
#     return result
#
# # Initialise wx App
#
# app = wx.App()
# app.MainLoop()
#
# #Call dialog
#
# x = ask(message='Suh Dude. Che Number?')
#
# if int(x) > 10:
#     print('Woah dude, that\'s a big number')
# else:
#     print('Lol. What a smol booi')
#
# print('Your number was ', x)
#
# fiveTimes = int(x)
#
# for num in range(0, 4):
#     fiveTimes = fiveTimes + int(x)
#
#
# print('Five times ', x, ' equals ', fiveTimes)
#
#
# boopFile = open("Boop.txt", "r")
# print(boopFile.read())
# print(boopFile.read(3))
# print(boopFile.readline())
#
# boopFile.close()
#
#
# outFile = open("Out.txt", "w")
#
# outFile.write("It's ye boooi")
# outFile.write("It's ye boooi... AGAIN!")
# outFile.write("The number one OG PRRRAAAAANKSTERRR!")
# outFile.close()

def onButton(event):
    print ("Butt Pressed")

app = wx.App()

frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,50)

#Creates the open file dialogue
openDataFileDlg = wx.FileDialog(frame, "Open Data File", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

openDataFileDlg.ShowModal()
# print(openFileDlg.GetPath())

#Store the path received from this dialogue
dataPath = openDataFileDlg.GetPath()

openDataFileDlg.Destroy()


#Creates the open file dialogue for the phe file
openPheFileDlg = wx.FileDialog(frame, "Open Data File", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

openPheFileDlg.ShowModal()
# print(openFileDlg.GetPath())

#Store the path received from this dialogue
phePath = openPheFileDlg.GetPath()

openPheFileDlg.Destroy()


dataFile = open(dataPath, "r")
pheFile =  open(phePath, "r")

line = dataFile.readline()
height = len(line.split())    #splits line into words separated by spans of white space
#print(height)

dataFile.seek(0)   #takes marker back to byte 0

width = 0

for line in dataFile:
    width = width + 1

#print(width)
dataFile.seek(0)


# Matrix = [[0 for x in range(width)] for y in range(height)]
# count = 0

# for line in testFile:
#     #Fills Array with values from file
#     Matrix[count] = line.strip().split()
#
#     #Scale the values to all be a percentage value that adds up to 1
#
#     #First we need the total sum for this specific line
#     lineTotal = 0
#     for values in Matrix[count]:
#         lineTotal = lineTotal + float(values)
#
#     # then we scale each value based on that total
#     valueNum = 0
#     for values in Matrix[count]:
#         Matrix[count][valueNum] = float(values)/lineTotal
#         valueNum = valueNum + 1
#
#     #this counter keeps track of which line we're on currently
#     count = count+1

Matrix = [[0 for x in range(width)] for y in range(height)]
count = 0
wordTotal = 0

for line in dataFile:
    #Fills Array with values from file
    words = line.strip().split()

    #Stores total sum of all values in this line for scaling later
    lineTotal = 0

    wordCount = 0
    for values in words:
        Matrix[wordCount][count] = float(words[wordCount])
        lineTotal = lineTotal + Matrix[wordCount][count]
        wordCount = wordCount + 1

    # stores total amount of different values for later use
    wordTotal = wordCount

    # Scale the values to all be a percentage value that adds up to 1
    # scale each value based on the line total we calculated above

    valueNum = 0
    for values in range(height):
        Matrix[valueNum][count] = float(Matrix[valueNum][count])/lineTotal
        valueNum = valueNum + 1

    # this counter keeps track of which line we're on currently
    count = count+1


#print (Matrix)


#Plot the new matrix


# x = [1,2,3,4,5]
# y1 = [1,1,2,3,5]
# y2 = [0,4,2,6,8]
# y3 = [1,3,5,7,9]
#
# y = np.vstack([y1,y2,y3])
#
# labels = ["Fib", "Even", "Odd"]
#
# fig, ax = plt.subplots()
# ax.stackplot(x, y1,y2,y3, labels=labels)
# ax.legend(loc=2)
#
# plt.show()
#
# fig, ax = plt.subplots()
# ax.stackplot(x, y)
# plt.show()


# Organising our group labels

# Here we extract the various group labels from the Phe file
currentLabel = ""
groupList = []
conciseGroupList = []
groupExists = False
column = 4
count = 0
groupCount = 0
for lines in pheFile:
    currentLine = lines.split()

    # This checks if the current label in the file is equal to the previous one
    # If there is a change, we know we're dealing with a new group
    if currentLine[column] != currentLabel:
        currentLabel = currentLine[column]
        groupList.append([count, currentLabel])
        for group in conciseGroupList:
            if currentLabel == group:
                groupExists = True
        if groupExists != True:
            conciseGroupList.append(currentLabel)
            groupCount = groupCount + 1

    count = count + 1
    groupExists = False

# We create an array with group names and their starting positions
groupList.append([count, currentLabel])
print(groupList)
print(conciseGroupList)
pheFile.seek(0)
# print(pheFile.read())

groupList = [[0, ""]]
sortedMatrix = [[0 for x in range(width)] for y in range(height)]


itemCount = 0
for collection in conciseGroupList:
    pheFile.seek(0)
    count = 0
    for lines in pheFile:
        currentLine = lines.split()
        currentLabel = currentLine[column]
        if currentLabel == collection:
            for values in range(wordTotal):
                sortedMatrix[values][itemCount] = Matrix[values][count]
            itemCount = itemCount + 1
        count = count + 1


    groupList.append([itemCount, collection])


#groupList.append([count, currentLabel])


    #count = count + 1

# Here we actually construct the graph to be shown
x = [x for x in range(width)]
#print (x.__len__())
#print(Matrix.__len__())

#print(x)

# y = np.hstack(Matrix)

#labels = ["Fib", "Even", "Odd"]

# fig, ax = plt.subplots()
# ax.stackplot(x, y1,y2,y3)
# ax.legend(loc=2)
#
# plt.show()

fig, ax = plt.subplots()
ax.stackplot(x, sortedMatrix)

#  Here we label the x axis with the group names and their adjusted positions (positions must be adjusted to the centre of the group)
labels = []
positions = []
count = 1
for label in range(groupCount):
    labels.append(groupList[count][1])
    positions.append((groupList[count][0] + groupList[count - 1][0])/2)
    count = count + 1

#plt.xticks((111,234,567,900,1134), ("boop", "boop2", "boop3 - boop again", "boop4 - the fourth kind", "boop5 - the boopening"))
plt.xticks(positions, labels)


plt.show()

dataFile.close()
pheFile.close()







# for letter in 'Python':     # First Example
#    print ('Current Letter :', letter)
#
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # Second Example
#    print ('Current fruit :', fruit)