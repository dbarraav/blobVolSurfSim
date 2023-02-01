from cc3d.cpp.PlayerPython import * 
from cc3d import CompuCellSetup
from cc3d.core.PySteppables import *
# from cc3d.core.CMLFieldHandler.py
import random 
from math import *
import numpy as np
from random import uniform
import os
import csv 

totalSimTime = {{totalSimTime}}

class getPropSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)
        

    def start(self):
        print('Start')

    def step(self, mcs):
        for cell in self.cell_list_by_type(self.CELL):
            print('This is the targetVolume', cell.targetVolume)
            print('This is the targetSA', cell.targetSurface)          
            
        if mcs >= totalSimTime:
            self.stop_simulation()



