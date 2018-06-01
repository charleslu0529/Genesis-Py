import matplotlib.pyplot as plt
# import numpy as np
import wx


class AdmixController:

    app = wx.App()

    def __init__(self):

        self.dataFile = None

        self.pheFile = None
        self.height = 0
        self.width = 0

        self.maxColNum = 0

        self.dataPath = ""
        self.phePath = ""
        self.choiceList = []

        # These check whether the user has actually loaded files or not
        self.pheSelected = False
        self.dataSelected = False

        self.Matrix = []
        self.sortedMatrix = []

        # Will keep track of how many values are in each row of data (for later use)
        self.wordTotal = 0

        # This will store group names and the positions their members take up for labelling purposes.
        self.groupList = []
        # This will just store group names to simplify the sorting process
        self.conciseGroupList = []

        self.groupCount = 0

        # Stores which column of the Phe file to use for the plotting
        self.column = 4

        # This gets the default colour palette for the graph
        self.colourPal = plt.rcParams['axes.prop_cycle'].by_key()['color']
        self.graphAlpha = 1

    def getChoiceList(self):
        return self.choiceList

    def getDataSelected(self):
        return self.dataSelected

    def getPheSelected(self):
        return self.pheSelected

    def getDataPath(self):
        return self.dataPath

    def getPhePath(self):
        return self.phePath

    def importData(self):

        # The following is used to create the open file dialogue box for the data file
        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Creates the open file dialogue
        openDataFileDlg = wx.FileDialog(frame, "Open Data File", wildcard="", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

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

            self.dataFile.seek(0)  # takes marker back to byte 0

            # Width is the total number of rows in the file
            self.width = 0
            for line in self.dataFile:
                self.width = self.width + 1

            self.dataFile.seek(0)  # Starts reading the file from the beginning again

            self.dataSelected = True

        except IOError:
            wx.LogError("Cannot open file '%s'." % self.dataPath)

        openDataFileDlg.Destroy()


    def importPhe(self):

        # The following is used to create an open file dialogue box for the phe file

        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Creates the open file dialogue for the phe file
        openPheFileDlg = wx.FileDialog(frame, "Open Data File", wildcard="phe files (*.phe)|*.phe", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        # Original Open Phe File Function #FearOfCommitment
        '''openPheFileDlg.ShowModal()

        # Store the path received from this dialogue
        self.phePath = openPheFileDlg.GetPath()

        openPheFileDlg.Destroy()

        # Here we begin reading data from the two files the user has selected
        self.pheFile = open(self.phePath, "r")'''



        if openPheFileDlg.ShowModal() == wx.ID_CANCEL:
            return  # the user changed their mind, thus we will not do anything

        # Store the path received from this dialogue
        self.phePath = openPheFileDlg.GetPath()
        try:
            # Here we begin reading data from the file the user has selected
            self.pheFile = open(self.phePath, "r")

            line = self.pheFile.readline()
            height = len(line.split())  # splits line into words separated by spans of white space

            self.choiceList = []
            for col in range(height):
                if col > 1:
                    self.choiceList.append("Col " + str(col))

            self.pheFile.seek(0)

            self.pheSelected = True

        except IOError:
            wx.LogError("Cannot open file " + self.phePath + "." % self.phePath)

        openPheFileDlg.Destroy()

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
            if count < self.width:
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
            else:
             break


        # groupList.append([count, currentLabel])
        self.pheFile.seek(0)

        # We're creating an array with group names and their starting positions
        self.groupList = [[0, "start"]]
        self.sortedMatrix = [[0 for x in range(self.width)] for y in range(self.height)]
        print(self.width)
        print(self.height)
        itemCount = 0
        for collection in self.conciseGroupList:
            self.pheFile.seek(0)
            count = 0
            for lines in self.pheFile:
                if count < self.width:
                    currentLine = lines.split()
                    currentLabel = currentLine[self.column]
                    if currentLabel == collection:
                        for values in range(self.wordTotal):
                            #print(str(values) + "v")
                            #print(str(count) + "c")
                            self.sortedMatrix[values][itemCount] = self.Matrix[values][count]
                            
                            #self.sortedMatrix[values].append(self.Matrix[values][count])
                        itemCount = itemCount + 1
                    count = count + 1
                else:
                    break

            # We create an array with group names and their starting positions
            self.groupList.append([itemCount, collection])


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
        self.createGraph()



    # Nandi, call this function to change the alpha value of the graph
    def changeAlpha(self, alpha):

        self.graphAlpha = alpha
        self.createGraph()


    def createGraph(self):

        # Here we actually construct the graph to be shown==============================================================
        x = [x for x in range(self.width)]

        fig, ax = plt.subplots()

        ax.stackplot(x, self.sortedMatrix, colors=self.colourPal,
                     alpha=self.graphAlpha)  # Defines the size of our x axis and our y values

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



    def drawGraph(self, col):

        self.populateMatrix(self)
        self.sortGroups(self, col)  # note that col is the column we wish to use in the phe file
        self.createGraph(self)


    # This must be called when someone clicks the save button and you've determined that they are trying to save an admix file.
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



    def saveGraph(self, saveFile):

        # This will tell the load function which type of graph to construct
        saveFile.write("admix\n")

        saveFile.write(str(self.width))
        saveFile.write("\n")
        saveFile.write(str(self.height))
        saveFile.write("\n")

        # Stores values from the sorted array
        for h in range(self.height):
            for w in range(self.width):
                saveFile.write(str(self.sortedMatrix[h][w]))
                saveFile.write(" ")
            saveFile.write("\n")

        # saveFile.write(self.sortedMatrix)
        # saveFile.write("\n")


        # Stores the current colour set
        for colours in self.colourPal:
            saveFile.write(colours)
            saveFile.write(" ")
        saveFile.write("\n")


        saveFile.write(str(self.graphAlpha))
        saveFile.write("\n")

        saveFile.write(str(self.groupCount))
        saveFile.write("\n")


        # the extra 1 comes from the dummy group at the start of the list
        for group in range(self.groupCount + 1):
            saveFile.write(str(self.groupList[group][0]))
            saveFile.write(" ")
            saveFile.write(self.groupList[group][1])
            saveFile.write("\n")


        saveFile.close()



    # This function must be called when the user clicks the load button and the file being loaded is an admix graph
    def OnLoad(self):

        # The following is used to create the open file dialogue for .GEN files that were saved previously
        frame = wx.Frame(None, -1, 'win.py')
        frame.SetSize(0, 0, 200, 50)

        # Creates the open file dialogue for the gen file
        openGenFileDlg = wx.FileDialog(frame, "Open GEN File", wildcard="gen files (*.gen)|*.gen",
                                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if openGenFileDlg.ShowModal() == wx.ID_CANCEL:
            return  # the user changed their mind, thus we will not do anything

        # Store the path received from this dialogue
        genPath = openGenFileDlg.GetPath()
        try:
            # Here we begin reading data from the file the user has selected
            genFile = open(genPath, "r")
            self.LoadGraph(genFile)

        except IOError:
            wx.LogError("Cannot open file " + genPath + "." % genPath)

            openGenFileDlg.Destroy()


    def LoadGraph(self, genFile):

        #saveFile.write(str(self.width))
        graphType = genFile.readline()

        self.width = int(genFile.readline())
        self.height = int(genFile.readline())

        # initialise matrices to correct size
        self.Matrix = [[0 for x in range(self.width)] for y in range(self.height)]
        self.sortedMatrix = [[0 for x in range(self.width)] for y in range(self.height)]


        for h in range(self.height):
            currentLine = genFile.readline().split()
            for w in range(self.width):
                self.sortedMatrix[h][w] = float(currentLine[w])

        self.colourPal = genFile.readline().split()

        self.graphAlpha = float(genFile.readline())

        self.groupCount = int(genFile.readline())

        self.groupList = []

        for group in range(self.groupCount + 1):
            currentLine = genFile.readline().split()

            self.groupList.append([int(currentLine[0]), currentLine[1]])


        self.createGraph()

        genFile.close()
