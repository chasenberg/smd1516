from __future__ import print_function, unicode_literals, division
import ROOT as r
import numpy as np
import math as m

datei = r.TFile("/Users/christopher/Dropbox/SMD/Code/Blatt4/populationen.root", "RECREATE")

data = np.zeros((3,1))
tree_1 = r.TTree("population1","population1")
tree_1.Branch("x", data[0],"x/D")

def 2populationen()