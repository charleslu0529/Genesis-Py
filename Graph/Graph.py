# import admix and pca
from PCA import pca
# Info:
# cmd_folder = os.path.dirname(os.path.abspath(__file__)) # DO NOT USE __file__ !!!
# __file__ fails if the script is called in different ways on Windows.
# __file__ fails if someone does os.chdir() before.
# sys.argv[0] also fails, because it doesn't not always contains the path.
# create instance of graph then call function to populate

# Drawgraph(typeOfGraph, graphInstance)
def DrawGraph(typeOFGraph):
    if typeOFGraph == "Admix":
        pass
    elif typeOFGraph == "PCA":
        pcaGraph = pca.PCAGraph()
        pcaGraph.__init__()
        pcaGraph.importEvecFile()
        pcaGraph.importPheFile()
        pcaGraph.readFiles()
        pcaGraph.choosePCA()
        pcaGraph.initGroupColour()
        pcaGraph.plotScatter()

DrawGraph("PCA")