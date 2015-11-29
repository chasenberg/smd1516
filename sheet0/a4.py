from __future__ import unicode_literals, print_function, division

import numpy as np
import ROOT as r

#Anlegen eines Objekts der Klasse TFile, Option RECREATE bewirkt, dass das File neu angelegt wird, Dateiname: a4.root
file = r.TFile("a4.root", "RECREATE")	
#Erzeugen eines TTree mit dem Namen "data"
tree = r.TTree("data", "data")
#Erzeugt neues Array mit Dimension 1 und Datentyp "float"
x = np.zeros(1, dtype=float)
y = np.zeros(1, dtype=float)
z = np.zeros(1, dtype=float)
#Legt die Zweige des TTrees an und befuellt sie mit den Arrays x,y,z
tree.Branch("x", x, "x/D")
tree.Branch("y", y, "y/D")
tree.Branch("z", z, "z/D")
#Generiert Zufallszahlen mit der Klasse TRandom3
generator = r.TRandom3(0)
for i in range(1000):
    x[0] = generator.Rndm()*1000		#Rndm: Gleichverteilte Zufallszahlen
    y[0] = generator.Gaus(x[0],x[0])	#Gaussverteilung
    z[0] = generator.Poisson(x[0])		#Poissonverteilung
    tree.Fill()							#Fuellt den TTree auf

# Ueberpfuefe, ob alles im Baum angekommen ist:      surface: 000826533853
# print(tree.GetBranch("x").GetEntries())

file.Write()
file.Close()

#Erneutes Einlesen des TFiles
readFile = r.TFile("a4.root", "OPEN")
readTree = readFile.Get("data")

#Eintraege im Baum ausgeben
#readTree.Scan("*")

#b) Histogrammieren der x-Werte aus TTree
#Anlegen des Canvas-Objekts
canvas = r.TCanvas("canvas", "a", 800, 600)
readTree.Draw("x")
#canvas.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe4/4b.pdf")


#c) x gegen y
canvasc = r.TCanvas("canvasc", "c", 800,600)
readTree.Draw("y:x", "", "COLZ")
#canvasc.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe4/4c.pdf")


#d) Differenz: x-y
canvasd = r.TCanvas("canvasd", "d", 800, 600)
readTree.Draw("(x-z)")
#canvasd.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe4/4d.pdf")


#e) Histogrammiere x_i's mit  y_i>50
canvase = r.TCanvas("canvase", "e", 800, 600)
histe = r.TH1F("histe", "e", 100, -100, 1100)
#Projektion auf den Teil des TTrees, fuer den x,y>50 erfuellt ist
readTree.Project("histe", "x", "y > 50")
histe.Draw()
#canvase.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe4/4e.pdf")


#f) Zwei eindimensionale Histogramme in einem Ko-System
canvasf = r.TCanvas("canvasf", "f", 800, 600)

histfb = r.TH1F("histfb", "fblack", 100, -1000, 2000)
#schwarz
histfb.SetLineColor(1) 
#Projektion, so dass nur y's ausegewaehlt werden
readTree.Project("histfb", "y")
histfb.Draw()

histfg = r.TH1F("histfg", "fgreen", 100, -100, 1100)
#Projektion, so dass nur x's ausegewaehlt werden
readTree.Project("histfg", "x")
histfg.SetLineColor(8) #gruen
#Option "same" bewirkt, dass dieses Histog. auf gleichem Canvas dargestellt wird
histfg.Draw("same")
#canvasf.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe4/4f.pdf")

#g)Zwei 1D Histogramme von x und z in einem Canvas
canvasg = r.TCanvas("canvasg", "g", 800, 600)
#Splitten in subpads
canvasg.Divide(2,1)

#benutze das Histogramm histfg aus f)
canvasg.cd(1)
histfg.Draw()

canvasg.cd(2)
histg = r.TH1F("histg", "g", 100, -100, 1100)
readTree.Project("histg", "z")
histg.Draw()
#canvasg.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe4/4g.pdf")

#h) x mit x<=100, mit 10 Bins
canvash = r.TCanvas("canvash", "h", 800,600)
histh = r.TH1F("histh", "h", 10, 0, 100)
readTree.Project("histh", "x", "x < 101")
histh.Draw()
#canvash.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe4/4h.pdf")
