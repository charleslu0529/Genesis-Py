# import admix and pca
from PCA import pca
# Info:
# cmd_folder = os.path.dirname(os.path.abspath(__file__)) # DO NOT USE __file__ !!!
# __file__ fails if the script is called in different ways on Windows.
# __file__ fails if someone does os.chdir() before.
# sys.argv[0] also fails, because it doesn't not always contains the path.
# create instance of graph then call function to populate

# Drawgraph(typeOfGraph, graphInstance)

def draw_graph(type_of_graph):

    if type_of_graph == "Admix":
        pass
    elif type_of_graph == "PCA":
        pca_graph = pca.PCAGraph()
        pca_graph.__init__()
        pca_graph.importEvecFile()
        pca_graph.importPheFile()
        pca_graph.readFiles()
        pca_graph.choosePCA(0, 4)
        pca_graph.initGroupColour()
        pca_graph.plotScatter()
        pca_graph.pickColour("EXM")


draw_graph("PCA")