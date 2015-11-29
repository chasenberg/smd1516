from __future__ import print_function, unicode_literals, division
import ROOT as r
import numpy as np
import math as m

datei = r.TFile("/Users/christopher/Dropbox/SMD/Code/Blatt4/populationen.root", "RECREATE")

data = np.zeros((4,1))
tree_1 = r.TTree("population1","population1")
tree_2 = r.TTree("population2","population2")
tree_1.Branch("x", data[0],"x/D")
tree_2.Branch("y", data[1],"x/D")
n = 10000

histogramm = r.TH2D("histogramm", "histogramm",30,15,15,30,-10,15)
histogramm2 = r.TH2D("histogramm2", "histogramm2",30,15,15,30,-10,15)
def population1(n):
	mu_x1 = 0
	sigma_x1 = 1.5
	mu_y1 = 4
	sigma_y1 = 1.5
	mu_x2 = 4
	sigma_x2 = 3.5
	sigma_y2 = 0.9
	for i in range(n):
            data[0] = np.random.normal(mu_x1,sigma_x1)
            data[1] = np.random.normal(mu_y1,sigma_y1)
            tree_1.Fill()
            histogramm.Fill(data[0],data[1])
            data[2] = np.random.normal(mu_x2,sigma_x2)
            mu_y2 = 2+0.35*(data[2]-4)
            data[3] = np.random.normal(mu_y2,sigma_y2)
            tree_2.Fill()
            histogramm2.Fill(data[2],data[3])
	return histogramm

def population2(n):
	mu_x2 = 4
	sigma_x2 = 3.5
	sigma_y2 = 0.9
	for i in range(n):
            data[2] = np.random.normal(mu_x2,sigma_x2)
            mu_y2 = 2+0.35*(data[2]-4)
            data[3] = np.random.normal(mu_y2,sigma_y2)
            tree_2.Fill()
            histogramm2.Fill(data[2],data[3])
	return histogramm2

population = r.TCanvas("population", "population", 800, 600)
#population.SetLogy()
pop1 = population1(n)
pop1.DrawCopy("COLZ")
pop2 = population2(n)
pop2.Draw("sames")
population.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt4/a2.pdf")

