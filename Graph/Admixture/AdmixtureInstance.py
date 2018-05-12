import matplotlib.pyplot as plt
#import numpy as np
import wx


class AdmixController:

    app = wx.App()

    def __init__(self):

        self.dataFile = None

        self.pheFile = None
        self.height = 0
        self.width = 0

        self.Matrix = []
        self.sortedMatrix = []

        # Will keep track of how many values are in each row of data (for later use)
        self.wordTotal = 0

        # This will store group names and the positions their members take up for labelling purposes.
        self.groupList = []
        # This will just store group names to simplify the sorting process
        self.conciseGroupList = []

        self.groupCount = 0
        self.column = 4

    def importData(self):

        # The following is used to create the an open file dialogue box


        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Creates the open file dialogue
        openDataFileDlg = wx.FileDialog(frame, "Open Data File", wildcard="Q data files (*.1;*.2;*.3;*.4;*.5;*.6;*.7)|*.1;*.2;*.3;*.4;*.5;*.6;*.7", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)


        openDataFileDlg.ShowModal()

        # Store the path received from this dialogue
        dataPath = openDataFileDlg.GetPath()

        openDataFileDlg.Destroy()

        # Here we begin reading data from the two files the user has selected
        self.dataFile = open(dataPath, "r")

        line = self.dataFile.readline()
        self.height = len(line.split())  # splits line into words separated by spans of white space

        self.dataFile.seek(0)  # takes marker back to byte 0

        # Width is the total number of rows in the file
        self.width = 0
        for line in self.dataFile:
            self.width = self.width + 1

        self.dataFile.seek(0)  # Starts reading the file from the beginning again


    def importPhe(self):

        # The following is used to create the two open file dialogue boxes

        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Creates the open file dialogue for the phe file
        openPheFileDlg = wx.FileDialog(frame, "Open Data File", wildcard="phe files (*.phe)|*.phe", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openPheFileDlg.ShowModal()
        # print(openFileDlg.GetPath())
        # Store the path received from this dialogue
        phePath = openPheFileDlg.GetPath()

        openPheFileDlg.Destroy()

        # Here we begin reading data from the two files the user has selected
        self.pheFile = open(phePath, "r")

    def populateMatrix(self):

        # The following commented out code block will construct the same matrix but with the columns and rows swapped.
        #  This may be useful for displaying a vertical graph later.
        #  Note that for this code to run, the values in width and height need to be swapped
        # ======================================================================================================================

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

        # ======================================================================================================================
        # End of the transposed version's code

        self.Matrix = [[0 for x in range(self.width)] for y in range(self.height)]
        count = 0

        for line in self.dataFile:
            # Fills Array with values from file
            words = line.strip().split()

            # Stores total sum of all values in this line for scaling later
            lineTotal = 0

            wordCount = 0
            for values in words:
                self.Matrix[wordCount][count] = float(words[wordCount])
                lineTotal = lineTotal + self.Matrix[wordCount][count]
                wordCount = wordCount + 1

            self.wordTotal = wordCount

            # Scale the values to all be a percentage value that adds up to 1
            # scale each value based on the line total we calculated above

            valueNum = 0
            for values in range(self.height):
                self.Matrix[valueNum][count] = float(self.Matrix[valueNum][count]) / lineTotal
                valueNum = valueNum + 1

            # this counter keeps track of which line we're on currently
            count = count + 1


    def sortGroups(self, col):
        # Organising our group labels===========================================================================
        self.column = col

        # Here we extract the various group labels from the Phe file
        currentLabel = ""

        groupExists = False
        count = 0
        self.groupCount = 0
        for lines in self.pheFile:
            currentLine = lines.split()

            # This checks if the current label in the file is equal to the previous one
            # If there is a change, we know we're dealing with a potential new group
            # We then compare this with a list of groups already encountered.
            # If it is not in said list, we add it as a new group.
            if currentLine[self.column] != currentLabel:
                currentLabel = currentLine[self.column]
                for group in self.conciseGroupList:
                    if currentLabel == group:
                        groupExists = True
                if groupExists != True:
                    self.conciseGroupList.append(currentLabel)
                    self.groupCount = self.groupCount + 1

            count = count + 1
            groupExists = False


        # groupList.append([count, currentLabel])
        self.pheFile.seek(0)

        # We're creating an array with group names and their starting positions
        self.groupList = [[0, ""]]
        self.sortedMatrix = [[0 for x in range(self.width)] for y in range(self.height)]

        itemCount = 0
        for collection in self.conciseGroupList:
            self.pheFile.seek(0)
            count = 0
            for lines in self.pheFile:
                currentLine = lines.split()
                currentLabel = currentLine[self.column]
                if currentLabel == collection:
                    for values in range(self.wordTotal):
                        self.sortedMatrix[values][itemCount] = self.Matrix[values][count]
                    itemCount = itemCount + 1
                count = count + 1

            # We create an array with group names and their starting positions
            self.groupList.append([itemCount, collection])

    def drawGraph(self):

        # Here we actually construct the graph to be shown==============================================================
        x = [x for x in range(self.width)]

        fig, ax = plt.subplots()
        print(x)
        print(self.sortedMatrix)
        ax.stackplot(x, self.sortedMatrix)  # Defines the size of our x axis and our y values

        # Here we label the x axis with the group names and their adjusted positions
        # (positions must be adjusted to the centre of the group)
        labels = []
        positions = []
        count = 1
        for label in range(self.groupCount):
            labels.append(self.groupList[count][1])
            positions.append((self.groupList[count][0] + self.groupList[count - 1][0]) / 2)
            count = count + 1

        plt.xticks(positions, labels)

        plt.show()

        self.dataFile.close()
        self.pheFile.close()




# admix = AdmixController(4)