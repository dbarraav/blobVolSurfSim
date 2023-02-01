from cc3d import CompuCellSetup

frequency = {{overallFreq}}

from blobVolSurfSim_Steppables import getPropSteppable
CompuCellSetup.register_steppable(steppable=getPropSteppable(frequency))

CompuCellSetup.run()

