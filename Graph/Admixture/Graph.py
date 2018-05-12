import AdmixtureInstance

admix = AdmixtureInstance.AdmixController()

admix.importData()
admix.importPhe()
admix.populateMatrix()
admix.sortGroups(4)
admix.drawGraph()
