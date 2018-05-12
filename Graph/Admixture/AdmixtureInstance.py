import matplotlib.pyplot as plt
<<<<<<< HEAD
# import numpy as np
=======
#import numpy as np
>>>>>>> origin/Nandi
import wx


class AdmixController:

    app = wx.App()

    def __init__(self):

        self.dataFile = None

        self.pheFile = None
        self.height = 0
        self.width = 0

<<<<<<< HEAD
        self.maxColNum = 0

        self.dataPath = ""
        self.phePath = ""
        self.choiceList = []

=======
>>>>>>> origin/Nandi
        self.Matrix = []
        self.sortedMatrix = []

        # Will keep track of how many values are in each row of data (for later use)
        self.wordTotal = 0

        # This will store group names and the positions their members take up for labelling purposes.
        self.groupList = []
        # This will just store group names to simplify the sorting process
        self.conciseGroupList = []

        self.groupCount = 0
<<<<<<< HEAD

        # Stores which column of the Phe file to use for the plotting
        self.column = 4

        # This gets the default colour palette for the graph
        self.colourPal = plt.rcParams['axes.prop_cycle'].by_key()['color']
        self.graphAlpha = 1

    def importData(self):

        # The following is used to create the an open file dialogue box for the data file
=======
        self.column = 4

    def importData(self):

        # The following is used to create the an open file dialogue box


>>>>>>> origin/Nandi
        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Creates the open file dialogue
        openDataFileDlg = wx.FileDialog(frame, "Open Data File", wildcard="Q data files (*.1;*.2;*.3;*.4;*.5;*.6;*.7)|*.1;*.2;*.3;*.4;*.5;*.6;*.7", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

<<<<<<< HEAD
        # openDataFileDlg.ShowModal()


        if openDataFileDlg.ShowModal() == wx.ID_CANCEL:
            return  # the user changed their mind, thus we will not do anything

        # Store the path received from this dialogue
        self.dataPath = openDataFileDlg.GetPath()
        try:
            # Here we begin reading data from the file the user has selected
            self.dataFile = open(self.dataPath, "r")

            line = self.dataFile.readline()
            self.height = len(line.split())  # splits line into words separated by spans of white space

            self.choiceList = []
            for col in range(self.height):
                self.choiceList.append("Col " + str(col))

            self.dataFile.seek(0)  # takes marker back to byte 0

            # Width is the total number of rows in the file
            self.width = 0
            for line in self.dataFile:
                self.width = self.width + 1

            self.dataFile.seek(0)  # Starts reading the file from the beginning again

        except IOError:
            wx.LogError("Cannot open file '%s'." % self.dataPath)

        openDataFileDlg.Destroy()
=======

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
>>>>>>> origin/Nandi


    def importPhe(self):

<<<<<<< HEAD
        # The following is used to create the an open file dialogue box for the phe file
=======
        # The following is used to create the two open file dialogue boxes
>>>>>>> origin/Nandi

        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Creates the open file dialogue for the phe file
        openPheFileDlg = wx.FileDialog(frame, "Open Data File", wildcard="phe files (*.phe)|*.phe", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

<<<<<<< HEAD
        # Original Open Phe File Function #FearOfCommitment
        '''openPheFileDlg.ShowModal()

        # Store the path received from this dialogue
        self.phePath = openPheFileDlg.GetPath()
=======
        openPheFileDlg.ShowModal()
        # print(openFileDlg.GetPath())
        # Store the path received from this dialogue
        phePath = openPheFileDlg.GetPath()
>>>>>>> origin/Nandi

        openPheFileDlg.Destroy()

        # Here we begin reading data from the two files the user has selected
<<<<<<< HEAD
        self.pheFile = open(self.phePath, "r")'''



        if openPheFileDlg.ShowModal() == wx.ID_CANCEL:
            return  # the user changed their mind, thus we will not do anything

        # Store the path received from this dialogue
        self.phePath = openPheFileDlg.GetPath()
        try:
            # Here we begin reading data from the file the user has selected
            self.pheFile = open(self.phePath, "r")

        except IOError:
            wx.LogError("Cannot open file " + self.phePath + "." % self.phePath)

        openPheFileDlg.Destroy()
=======
        self.pheFile = open(phePath, "r")
>>>>>>> origin/Nandi

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

<<<<<<< HEAD

    # Nandi, call this function to change a single colour on the graph
    # The number represents the index of the colour being changed in our choiceList list
    def changeColour(self, colNum):


        # Here we construct a dialogue with the colour picker in it
        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        wxColourPicker = wx.ColourDialog(wx.Frame(None, -1, "win.py"))
        wxColourPicker.ShowModal()

        # The colour data contains a member called colour. This is actually a wxColour object.
        # This object has a member function called getAsString. This returns the colour in various formats
        # The flag 4 asks for the string in the hexadecimal form '#FFFFFF'
        new_colour = wxColourPicker.GetColourData().GetColour().GetAsString(flags=4)  # flags=wxC2S_HTML_SYNTAX)

        self.colourPal[colNum] = new_colour

        # This reconstructs the graph, but the data in the graph is not changed.
        # The overall functionality can only be tested with the GUI. When the GUI is integrated I will test this.
        # Hopefully we can get that done soon.
        self.createGraph(self.column)



    # Nandi, call this function to change the alpha value of the graph
    def changeAlpha(self, alpha):

        self.graphAlpha = alpha
        self.createGraph(self.column)


    def createGraph(self,col):
=======
    def drawGraph(self):
>>>>>>> origin/Nandi

        # Here we actually construct the graph to be shown==============================================================
        x = [x for x in range(self.width)]

        fig, ax = plt.subplots()
<<<<<<< HEAD

        ax.stackplot(x, self.sortedMatrix, colors=self.colourPal,
                     alpha=self.graphAlpha)  # Defines the size of our x axis and our y values
=======
        print(x)
        print(self.sortedMatrix)
        ax.stackplot(x, self.sortedMatrix)  # Defines the size of our x axis and our y values
>>>>>>> origin/Nandi

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



<<<<<<< HEAD
    def drawGraph(self, col):

        self.populateMatrix()
        self.sortGroups(col)  # note that col is the column we wish to use in the phe file
        self.createGraph(col)


    #def saveGraph(self):

    def saveGraph(self, saveFile):

        print("I\'m saving this booi!!!!")

        saveFile.close()


    def OnSaveAs(self):

        # Here we construct a save as dialogue box
        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 175, 60)

        with wx.FileDialog(frame, "Save current work in GEN file", wildcard="GEN files (*.gen)|*.gen",
                               style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as SaveAsDlg:

            if SaveAsDlg.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind, thus we will not do anything

            # save the current contents in the file
            savePath = SaveAsDlg.GetPath()
            try:
                with open(savePath, 'w') as saveFile:
                    self.saveGraph(saveFile)
            except IOError:
                wx.LogError("Cannot save current data in file " + savePath + "." % savePath)

=======
>>>>>>> origin/Nandi

# admix = AdmixController(4)