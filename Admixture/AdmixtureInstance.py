import matplotlib.pyplot as plt
import numpy as np
import wx


class AdmixController:

    def createGraph(self):
        # dataFile = None
        # pheFile = None

        # The following is used to create the two open file dialogue boxes
        # def openAdmixFiles(self):
        app = wx.App()

        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Creates the open file dialogue
        openDataFileDlg = wx.FileDialog(frame, "Open Data File", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openDataFileDlg.ShowModal()

        # Store the path received from this dialogue
        dataPath = openDataFileDlg.GetPath()

        openDataFileDlg.Destroy()

        # Creates the open file dialogue for the phe file
        openPheFileDlg = wx.FileDialog(frame, "Open Data File", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openPheFileDlg.ShowModal()
        # print(openFileDlg.GetPath())
        # Store the path received from this dialogue
        phePath = openPheFileDlg.GetPath()

        openPheFileDlg.Destroy()

        # Here we begin reading data from the two files the user has selected
        dataFile = open(dataPath, "r")
        pheFile = open(phePath, "r")

        # def organiseData(self):

        line = dataFile.readline()
        height = len(line.split())  # splits line into words separated by spans of white space

        dataFile.seek(0)  # takes marker back to byte 0

        # Width is the total number of rows in the file
        width = 0
        for line in dataFile:
            width = width + 1

        dataFile.seek(0)  # Starts reading the file from the beginning again

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

        Matrix = [[0 for x in range(width)] for y in range(height)]
        count = 0

        # Will keep track of how many values are in each row of data (for later use)
        wordTotal = 0

        for line in dataFile:
            # Fills Array with values from file
            words = line.strip().split()

            # Stores total sum of all values in this line for scaling later
            lineTotal = 0

            wordCount = 0
            for values in words:
                Matrix[wordCount][count] = float(words[wordCount])
                lineTotal = lineTotal + Matrix[wordCount][count]
                wordCount = wordCount + 1

            wordTotal = wordCount

            # Scale the values to all be a percentage value that adds up to 1
            # scale each value based on the line total we calculated above

            valueNum = 0
            for values in range(height):
                Matrix[valueNum][count] = float(Matrix[valueNum][count]) / lineTotal
                valueNum = valueNum + 1

            # this counter keeps track of which line we're on currently
            count = count + 1

        # Organising our group labels

        # Here we extract the various group labels from the Phe file
        currentLabel = ""

        # This will store group names and the positions their members take up for labelling purposes.
        groupList = []
        # This will just store group names to simplify the sorting process
        conciseGroupList = []
        groupExists = False
        column = 4
        count = 0
        groupCount = 0
        for lines in pheFile:
            currentLine = lines.split()

            # This checks if the current label in the file is equal to the previous one
            # If there is a change, we know we're dealing with a potential new group
            # We then compare this with a list of groups already encountered.
            # If it is not in said list, we add it as a new group.
            if currentLine[column] != currentLabel:
                currentLabel = currentLine[column]
                for group in conciseGroupList:
                    if currentLabel == group:
                        groupExists = True
                if groupExists != True:
                    conciseGroupList.append(currentLabel)
                    groupCount = groupCount + 1

            count = count + 1
            groupExists = False

        # We create an array with group names and their starting positions
        # groupList.append([count, currentLabel])
        pheFile.seek(0)

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

        # Here we actually construct the graph to be shown
        x = [x for x in range(width)]

        fig, ax = plt.subplots()
        ax.stackplot(x, sortedMatrix)  # Defines the size of our x axis and our y values

        # Here we label the x axis with the group names and their adjusted positions
        # (positions must be adjusted to the centre of the group)
        labels = []
        positions = []
        count = 1
        for label in range(groupCount):
            labels.append(groupList[count][1])
            positions.append((groupList[count][0] + groupList[count - 1][0]) / 2)
            count = count + 1

        plt.xticks(positions, labels)

        plt.show()

        dataFile.close()
        pheFile.close()


