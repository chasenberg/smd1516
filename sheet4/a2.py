from __future__ import print_function, unicode_literals, division
import ROOT as r
import numpy as np
import math as m

########### Aufgabe 2a) ##############
datei = r.TFile("/Users/christopher/Dropbox/SMD/Code/Blatt4/populationen.root", "RECREATE")

data = np.zeros((4,1))
tree_1 = r.TTree("population1","population1")
tree_2 = r.TTree("population2","population2")
tree_1.Branch("x", data[0],"x/D")
tree_2.Branch("y", data[1],"x/D")
n = 10000
mu_x1 = 0
sigma_x1 = 1.5
mu_y1 = 4
sigma_y1 = 1.5

histogramm = r.TH2D("histogramm", "histogramm",30,15,15,30,-10,15)
histogramm2 = r.TH2D("histogramm2", "histogramm2",30,15,15,30,-10,15)

histogramm = r.TH2D("histogramm", "histogramm",30,15,15,30,-10,15)
histogramm2 = r.TH2D("histogramm2", "histogramm2",30,15,15,30,-10,15)

cov_12 = np.array([np.zeros(2),np.zeros(2)])

def population1(n):
	mu_x1 = 0
	sigma_x1 = 1.5
	mu_y1 = 4
	sigma_y1 = 1.5

	for i in range(n):
            data[0] = np.random.normal(mu_x1,sigma_x1)
            data[1] = np.random.normal(mu_y1,sigma_y1)
            tree_1.Fill()
            histogramm.Fill(data[0],data[1])
	print(len(data[0]))
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

############ Aufgabe 2b) #################

#Population 1 
for i in range(n):
	data[0] = np.random.normal(loc=mu_x1,scale=sigma_x1)
	data[1] = np.random.normal(loc=mu_y1,scale=sigma_y1)
	tree_1.Fill()
	histogramm.Fill(data[0],data[1])

# Berechnung der Mittelwerte 
x1_sum= np.sum(data[0])
length1 = len(data[0])
x1_mean = x1_sum/n
y1_sum= np.sum(data[1])
length2 = len(data[1])
y1_mean = y1_sum/n
print("Mean X_1:",x1_mean)
print("Mean Y_1:",y1_mean)

#Berechnung der Kovarianzmatrix
cov_0 = np.array([np.zeros(2),np.zeros(2)])
cov_0[0][0] = np.var(data[0], ddof = 0)
cov_0[1][0] = (np.dot((data[0]-x1_mean),(data[1]-y1_mean)))/(n-1)
cov_0[0][1] = cov_0[1][0]
cov_0[1][1] = np.var(data[1], ddof = 0)
korrel_0 = cov_0[1][0]/(m.sqrt(cov_0[1][1])*m.sqrt(cov_0[0][0]))
print("Kovarianzmatrix:","\n")
print(cov_0[0][0],"\t",cov_0[1][0],"\n")
print(cov_0[0][1],"\t",cov_0[1][1],"\n")
print("Korrelationskoeffizient: ",korrel_0,"\n")

# Population 2
mu_x2 = 4
sigma_x2 = 3.5
sigma_y2 = 0.9
for i in range(n):
    data[2] = np.random.normal(loc=mu_x2,scale=sigma_x2)
    mu_y2 = 2+0.35*(data[2]-4)
    data[3] = np.random.normal(loc=mu_y2,scale=sigma_y2)
    tree_2.Fill()
    histogramm2.Fill(data[2],data[3])

#Berechnung der Mittelwerte
x2_sum= np.sum(data[2])
length3 = len(data[2])
x2_mean = x2_sum/n
y2_sum= np.sum(data[3])
length4 = len(data[3])
y2_mean = y2_sum/n
print("Mean X_2:",x2_mean)
print("Mean Y_2:",y2_mean)


#Berechnung der Kovarianzmatrix
cov_2 = np.array([np.zeros(2),np.zeros(2)])
cov_2[0][0] = np.var(data[2], ddof = 0)
cov_2[1][0] = (np.dot((data[2]-x2_mean),(data[3]-y2_mean)))/(n-1)
cov_2[0][1] = cov_2[1][0]
cov_2[1][1] = np.var(data[3], ddof = 0)
korrel_2 = cov_2[1][0]/(m.sqrt(cov_2[1][1])*m.sqrt(cov_2[0][0]))
print("Kovarianzmatrix:","\n")
print(cov_2[0][0],"\t",cov_2[1][0],"\n")
print(cov_2[0][1],"\t",cov_2[1][1],"\n")
print("Korrelationskoeffizient: ",korrel_0,"\n")


#kombinierte Kovarianzmatrix
cov_12[0][0] = 0.5*(cov_1[0][0]+cov_2[0][0]);
cov_12[1][0] = 0.5*(cov_1[1][0]+cov_2[1][0]);
cov_12[0][1] = cov_12[1][0];
cov_12[1][1] = 0.5*(cov_1[1][1]+cov_2[1][1]);
#aenderung der kovarianz matrix -> 4x4?
#alternativ:

cov_121 = np.array([np.zeros(4),np.zeros(4)])
cov_121[0][0] = cov_1[0][0]
cov_121[1][0] = (np.dot((data[1]-y1_mean),(data[0]-x1_mean)))/(n-1)
cov_121[2][0] = (np.dot((data[2]-x2_mean),(data[0]-x1_mean)))/(n-1)
cov_121[3][0] = (np.dot((data[3]-y2_mean),(data[0]-x1_mean)))/(n-1)
cov_121[0][1] = cov_121[1][0]
cov_121[0][1] = cov_121[1][0]
#Ausgabe
print("Kombinierte Kovarianzmatrix:","\n")
print(cov_12[0][0],"\t",cov_12[1][0],"\n")
print(cov_12[0][1],"\t",cov_12[1][1],"\n")




