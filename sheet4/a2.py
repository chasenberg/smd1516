from __future__ import print_function, unicode_literals, division

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import ROOT as r

#Anlegen des ROOT-Files
datei = r.TFile("/Users/christopher/Dropbox/SMD/Code/Blatt4/a2.root","RECREATE")

# Aufgabenteil a)
#Populationszahl
n = 10000 
#Erzeugung der Zufallszahlen mit den gegebenen Informationen
x1 = np.random.normal(0, 1.5, n)
y1 = np.random.normal(4, 1.5, n)
x2 = np.random.normal(4, 3.5, n)
y2 = np.zeros(n)

for i, x in zip(range(len(x2)),x2):
    y2[i] = np.random.normal(2 + 0.35 * (x - 4), 0.9)
#Plotten der Daten in 2D-Histogramme fuer die erste Population
fig = plt.figure()    
plt.hist2d(x1, y1, bins=30, norm=LogNorm(), alpha=1)
plt.colorbar()
fig = plt.figure()
plt.hist2d(x2, y2, bins=30, norm=LogNorm(), alpha=1)
plt.colorbar()
fig = plt.figure()    
plt.hist2d(x1, y1, bins=30, norm=LogNorm(), alpha=1)
plt.colorbar()
plt.hist2d(x2, y2, bins=30, norm=LogNorm(), alpha=0.7)
plt.ylim([-4,10])
plt.colorbar()
plt.show()

#Aufgabenteil b)

#Hier werden nun die Mittelwerte,Varianzen und die Kovarianzen der einzelnen Verteilungen berechnet
x1_mean = np.mean(x1)
y1_mean = np.mean(y1)
x2_mean = np.mean(x2)
y2_mean = np.mean(y2)
#Varianz
x1_var = np.var(x1)
y1_var = np.var(y1)
x2_var = np.var(x2)
y2_var = np.var(y2)
#Kovarianz der 1. Population
x1_covariance = np.cov(x1)
y1_covariance = np.cov(y1)
#Kovarianz der 2. Population
x2_covariance = np.cov(x2)
y2_covariance = np.cov(y2)
#Korrelationkoeffizienten rho
x1_correlcoeff = np.correlcoeff(x1)
y1_correlcoeff = np.correlcoeff(y1)
x2_correlcoeff = np.correlcoeff(x2)
y2_correlcoeff = np.correlcoeff(y2)
#Kovarianz der beiden Verteilungen
covariance1 = np.cov(np.array([x1,y1]))
covariance2 = np.cov(np.array([x2,y2]))

# Berechnung der Korrelationskoeffizienten der Gesamtheiten
correlcoeff1 = np.correlcoeff(np.array([x1,y1]))
correlcoeff2 = np.correlcoeff(np.array([x2,y2]))

#Ausgabe der ermittelte Größen
print("Mittelwerte")
print(x1_mean, y1_mean, x2_mean, y2_mean)
print("\n Varianz")
print(x1_var, y1_var, x2_var, y2_var)
print("\n Einzeln Kovarianz")
print(x1_covariance, y1_covariance, x2_covariance, y2_covariance)
print("\n Einzeln Korrelation")
print(x1_correlcoeff, y1_correlcoeff, x2_correlcoeff, y2_correlcoeff)
print("\n Kovarianz")
print(covariance1)
print(covariance2)
print("\n Korrelation")
print(correlcoeff1)
print(correlcoeff2)

#Aufgabenteil c)
#Abspeichern in ROOT-File: Population 1
tree_1 = r.TTree("Population 1", "Population 1")
data = np.zeros((2,1))
tree_1.Branch("x1", data[0], "x/D")
tree_1.Branch("y1", data[1], "x/D")
for i in range(n):
    data[0] = np.random.normal(0, 1.5)
    tree_1.Fill()
    data[1] = np.random.normal(4,1.5)
    tree_1.Fill
tree_1.Write()

#Abspeichern in ROOT-File: Population 2
tree_2 = r.TTree("Population 2", "Population 2")
data2 = np.zeros((2,1))
tree_2.Branch("x2", data2[0], "x/D")
tree_2.Branch("y2", data2[1], "x/D")
for i in range(n):
    data2[0] = np.random.normal(0, 1.5)
    tree_2.Fill()
    mu_y = 2 + 0.35 * (data2[0] - 4)
    data2[1] = np.random.normal(mu_y, 0.9)
    tree_2.Fill
tree_2.Write()

#Abspeichern in ROOT-File: Population 3
tree_3 = r.TTree("Population 3", "Population 3")
n2 =1000
data3 = np.zeros((2,1))
tree_3.Branch("x3", data3[0], "x/D")
tree_3.Branch("y3", data3[1], "x/D")
for i in range(n2):
    data3[0] = np.random.normal(0, 1.5)
    tree_3.Fill()
    data3[1] = np.random.normal(4,1.5)
    tree_3.Fill
tree_3.Write()

