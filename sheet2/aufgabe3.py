from __future__ import print_function, unicode_literals, division


def aufg3():
	import ROOT
	import numpy as np

	#Erstellen des linear-kongruenten Zufallsgenerators fuer beliebige Laenge und Darstellung der Pseudozufallszahlen im Histogramm
	#Aufgabenteil (a) + (b)

	#a: Faktor/Multiplikator, b: Inkrement, m: Modul, length: Laenge des zufaelligen Arrays, x0: Startwert
	def random(a, b, m, length, x0):
		randomarray = np.zeros(length)
		randomarray[0] = x0
		for i in range(len(randomarray)-1):							#len(): gibt die Laenge eines Objekts zurueck
			randomarray[i+1] = (a*randomarray[i] + b) % m
		randomarray = randomarray/m
		return randomarray	

	#Werte des Generator + beliebigen Wert fuer Startwert x0 und length n
	a = 1601
	b = 3456
	m = 10000
	x0 = 6000
	n = 10000														#Ergebnis auch abhaengig von Laenge n


	#Fuellen des Histogramms mit Pseudozufallszahlen
	pseudo = random(a,b,m,n,x0)
	canv = ROOT.TCanvas("canv", "Zufallsgenerator", 800, 600)
	histrandom = ROOT.TH1F("histrandom", "Zufallsgenerator", 100, 0,1)
	for i in range(len(pseudo)):
		histrandom.Fill(pseudo[i])
	histrandom.Draw()
	canv.SaveAs("Aufgabe3b1.pdf")


	#Ueberpruefung der Abhaengigkeit des Generators vom Startwert
	start = np.array([0, 50, 100, 500, 1000, 5000, 10000, 50000])
	matrix = [[0 for x in range(n)] for x in range(len(start))]		#Speicher wird erzeugt fuer die erforderten Daten

	for i in range(len(start)):
		matrix[i] = random(a,b,m,n,start[i])


	#Erstellen des Canvas und der Histogramme
	canvas = ROOT.TCanvas("canvas", "canvas", 800, 600)
	canvas.Divide(4, 2)
	hists = []
	for i in range(len(start)):
		hist = ROOT.TH1F("hist", "hist"+str(start[i]), 100, 0,1)
		for j in range(n):
			hist.Fill(matrix[i][j])
		hists.append(hist)
		
	#Histogramme zeichnen und speichern
	for i in range(len(start)):
		canvas.cd(i+1)
		hists[i].Draw()
	canvas.SaveAs("Aufgabe3b2.pdf")


	#Aufeinanderfolgende Zahlen/Tuples als Histogramme darstellen - Aufgabenteil (c)
	#2D
	array2dim = random(a,b,m,20000,x0).reshape(10000,2)				#reshape(a,newshape): array_like, int or tuple of ints (hier:3000x2)
	canv2d = ROOT.TCanvas("canv2d", "2D", 800, 600)
	hist2d = ROOT.TH2F("hist2d", "2D", 100, 0, 1,100, 0, 1)
	for i in range(10000):
		hist2d.Fill(array2dim[i][0], array2dim[i][1])
	hist2d.Draw("COLZ")
	canv2d.SaveAs("Aufgabe3c-2D.pdf")

	#3D
	array3dim = random(a,b,m,30000,x0).reshape(10000,3)
	canv3d = ROOT.TCanvas("canv3d", "3D", 800, 600)
	hist3d = ROOT.TH3F("hist3d", "3D", 100, 0,1, 100,0,1, 100,0,1)
	for i in range(10000):
		hist3d.Fill(array3dim[i][0], array3dim[i][1], array3dim[i][2])
	hist3d.Draw("BOX")
	canv3d.SaveAs("Aufgabe3c-3D.pdf")

	#Erstellen von Zufallszahlen zwischen 0 und 1 mittels Trandom
	canve1d = ROOT.TCanvas("canve1d", "Rndm1D", 800,600)
	histe1d = ROOT.TH1F("histe1d", "Rndm1D", 100, 0,1)
	rndm = ROOT.TRandom()
	for i in range(10000):
		histe1d.Fill(rndm.Rndm())
	histe1d.Draw()
	canve1d.SaveAs("Aufgabe3e-1D.pdf")

	canve2d = ROOT.TCanvas("canve2d", "Rndm2D", 800,600)
	histe2d = ROOT.TH2F("histe2d", "Rndm2D", 100, 0,1, 100, 0, 1)
	rndm = ROOT.TRandom()
	for i in range(10000):
		histe2d.Fill(rndm.Rndm(), rndm.Rndm())
	histe2d.Draw("COLZ")
	canve2d.SaveAs("Aufgabe3e-2D.pdf")

	canve3d = ROOT.TCanvas("canve3d", "Rndm3D", 800,600)
	histe3d = ROOT.TH3F("histe3d", "Rndm3D", 100, 0,1, 100, 0, 1, 100, 0,1)
	rndm = ROOT.TRandom()
	for i in range(10000):
		histe3d.Fill(rndm.Rndm(), rndm.Rndm(), rndm.Rndm())
	histe3d.Draw("BOX")
	canve3d.SaveAs("Aufgabe3e-3D.pdf")


if __name__ == '__main__':
	aufg3()