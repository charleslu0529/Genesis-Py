import AdmixtureInstance

admix = AdmixtureInstance.AdmixController()

admix.importData()
admix.importPhe()
admix.drawGraph(4)

admix.changeColour(2)
admix.OnSaveAs()