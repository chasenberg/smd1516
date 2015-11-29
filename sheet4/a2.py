from __future__ import print_function, unicode_literals, division
import ROOT as r
import numpy as np
import math as m

datei = r.TFile("/Users/christopher/Dropbox/SMD/Code/Blatt4/populationen.root", "RECREATE")

data = np.zeros((2,1))
tree_1 = r.TTree("population1","population1")
tree_1.Branch("x", data[0],"x/D")
n = 10000
x_min = -15
histogramm = r.TH1D("histogramm", "histogramm",40,x_min,15)
def population1(n):
	mu_x = 0
	sigma_x = 4
	mu_y = 1.5
	sigma_y = 1.5
	rnd1 = r.TRandom3(1);
	
	for i in range(n):
            data[0] = np.random.normal(mu_x,sigma_x)
            tree_1.Fill()
            histogramm.Fill(data[0])
	return histogramm

population = r.TCanvas("population", "population", 800, 600)
population.SetLogy()
signal = population1(n)
signal.DrawCopy()
population.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt4/a2.pdf")

