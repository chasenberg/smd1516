import ROOT
import numpy as np
import sympy 
from sympy import *
x, y, z, r , N, n, tau, xmin, xmax= symbols(' x y z r N n tau xmin xmax')

def aufg4():
	#Anzahl Zufallszahlen
	k=1000
	
	np.random.seed(42) #Seed setzen
	y = np.random.uniform(0,1,k) #erzeugen von 1000 Zufallszahlen zwischen 0 und 1

	#Transformation einer Gleichverteilung gemäß Folie 27 GenerationZufallszahlen.pdf 
	def tra(f,xmin,xmax): #Funktion der Verteilung, sowie den Integrationsbereich übergeben
		A=integrate(f, (x, xmin, xmax)) #Normierung, gesamte Fläche unter der Kurve
		B=integrate(f, (x, xmin, x)) #Fläche bis zur Zufallsvariablen
		s=solve(B/A -r, x) #normierte relative fläche r=B/A bestimmen und nach x auflösen(invertieren)
		d=s[0].replace(cot, atan) #cotangens von sympy durch atan für numpy ersetzen	
		print(d) #Formel ausgeben
		return d

#Aufgabenteil a)
	#Grenzen der Gleichverteilung angeben
	xmin=5 
	xmax=10

	#definition der Verteilung
	def gleich(xmin,xmax):
		return 1/(xmax-xmin)


	z = lambdify(r, tra(gleich(xmin,xmax),xmin,xmax), "numpy") 	#mit numpyarray auswertbare funktion erstellen
	j=np.asarray(z(y))	#Dateityp ändern um die werte ins histogramm füllen zu können
	
	#erzeugte Zufallszahlen als Histogramm darstellen
	canv1 = ROOT.TCanvas("canv1", "TH1F Beispiel", 800, 600)
	hist1 = ROOT.TH1F("hist1", "hist1", 40, 0, 20)
	for i in np.arange(k):
    		hist1.Fill(j[i])
	hist1.SetMinimum(0)
	hist1.SetLineColor(2)
	hist1.SetLineStyle(2)
	hist1.SetLineWidth(3)
	hist1.Draw()
	canv1.Update()
	canv1.SaveAs("Canvas1.pdf")

#Aufgabenteil b)
	#Grenzen der Exponentialfunktion setzen
	xmin=0
	xmax=oo

	#Parameter der Exponentialverteilung setzen
	N=3
	tau=2

	#Definition der Exponentialfunktion
	def exponential(N,tau):
		return N*exp(-x/tau)

	z = lambdify(r, tra(exponential(N,tau),xmin,xmax), "numpy")	#mit numpyarray auswertbare funktion erstellen
	j=np.asarray(z(y))	#Dateityp ändern um die werte ins histogramm füllen zu können

	#erzeugte Zufallszahlen als Histogramm darstellen
	canv2 = ROOT.TCanvas("canv2", "TH1F Beispiel", 800, 600)
	hist2 = ROOT.TH1F("hist2", "hist2", 40, 0, 20)
	for i in np.arange(k):
    		hist2.Fill(j[i])
	hist2.SetMinimum(0)
	hist2.SetLineColor(2)
	hist2.SetLineStyle(2)
	hist2.SetLineWidth(3)
	hist2.Draw()
	canv2.Update()
	canv2.SaveAs("Canvas2.pdf")

#Aufgabeneteil c)
	#Grenzen der Potenzverteilung
	xmin=2
	xmax=10

	#Parameter der Potenzverteilung 
	N=3
	n=2

	#Definiton der Potenzfunktion 
	def potenz(N,n):
		return N*x**(-n)

	z = lambdify(r, tra(potenz(N,n),xmin,xmax), "numpy")	#mit numpyarray auswertbare funktion erstellen
	j=np.asarray(z(y))	#Dateityp ändern um die werte ins histogramm füllen zu können

	#erzeugte Zufallszahlen als Histogramm darstellen
	canv3 = ROOT.TCanvas("canv3", "TH1F Beispiel", 800, 600)
	hist3 = ROOT.TH1F("hist3", "hist3", 40, 0, 20)
	for i in np.arange(k):
    		hist3.Fill(j[i])
	hist3.SetMinimum(0)
	hist3.SetLineColor(2)
	hist3.SetLineStyle(2)
	hist3.SetLineWidth(3)
	hist3.Draw()
	canv3.Update()
	canv3.SaveAs("Canvas3.pdf")

#Aufgabeneteil d)
	#Grenzen der Cauchy-Verteilung
	xmin=-oo
	xmax=oo

	#Definition der Cauchy-Funktion
	def cauchy():
		return (1/pi)*(1/(1+x**2))

	z = lambdify(r, tra(cauchy(),xmin,xmax), "numpy")	#mit numpyarray auswertbare funktion erstellen
	j=np.asarray(z(y))	#Dateityp ändern um die werte ins histogramm füllen zu können

	#erzeugte Zufallszahlen als Histogramm darstellen
	canv4 = ROOT.TCanvas("canv4", "TH1F Beispiel", 800, 600)
	hist4 = ROOT.TH1F("hist4", "hist4", 40, -2, 2)
	for i in np.arange(k):
    		hist4.Fill(j[i])
	hist4.SetMinimum(0)
	hist4.SetLineColor(2)
	hist4.SetLineStyle(2)
	hist4.SetLineWidth(3)
	hist4.Draw()
	canv4.Update()
	canv4.SaveAs("Canvas4.pdf")

#Aufgabenteil e)
	#Histogramm einlesen und darstellen
	canv5 = ROOT.TCanvas("canv5", "TH1F Beispiel", 800, 600)
	t_file=ROOT.TFile("empirisches_histogramm.root", "read")
	histo= t_file.Get("h1")
	histo.DrawCopy()
	print("Zum Beenden ENTER drücken")
	input()	

if __name__ == '__main__':
	aufg4()
