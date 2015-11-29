from __future__ import unicode_literals, division, print_function
import ROOT
import numpy as np
import matplotlib.pyplot as plt

def aufg1(N=100):                               #Definition der Funktion, die das gewuenschte Array baut

    x = np.arange(N) + 1                        #numpy.arange gibt aufsteigende Zahlen bis N-1 zurueck -> 99 + 1

    uni1 = np.random.uniform(0, 1, N)           #numpy.random.uniform zieht N Zufallszahlen zwischen 0 und 1, die gleichverteilt sind
    uni10 = np.random.uniform(0, 10, N)         # "                         "                      0  "  10         "
    uni2030 = np.random.uniform(20, 30, N)      # "                         "                      20 "  30         "

    std_gauss = np.random.normal(0, 1, N)       #numpy.random.normal zieht N normalverteilte Zahlen
    gauss_5_2 = np.random.normal(5, 2, N)       #modifziert zum Mittelwert 5 und Standardabweichung 2

    x_squared = x**2                            #quadriert die 0. Spalte des numpy.array
    cosx = np.cos(x)                            #nimmt den Kosinus der 0. Spalte

    data = np.array([x, uni1, uni10, uni2030, std_gauss, gauss_5_2, x_squared, cosx])   #numpy.array fasst die generierten Zahlen zu einem 2D-Array zusammen
    return data                                 #Rueckgabewert der Funktion
    

def aufg2(data):                                #Defintion der neuen Funktion, Eingangswert ist das zuvor generierte Array
    N = data.shape[1]                           #numpy.ndarray.shape[i] liefert die Dimension der i-ten Spalte
    canv = ROOT.TCanvas("canv", "2 TGraphs")    #Konstruktor TCanvas erzeugt Objekt zum "Auftragen" der Graphen
    canv.SetGrid()                              #Legt ein Gitter an

    graph1 = ROOT.TGraph(N, data[0], data[6])   #erzeugt ein TGraph Objekt: N=Anzahl der Datenpunkte, x-Koordinaten: data[0], y-Koordinaten: data[6]
    graph2 = ROOT.TGraph(N, data[0], data[7])   #erzeugt ein TGraph Objekt: N=Anzahl der Datenpunkte, x-Koordinaten: data[0], y-Koordinaten: data[7]

    graph1.SetMarkerStyle(20)                   #SetMarkerStyle(20): kFullCircle=20 (Kreis)
    graph1.SetMarkerColor(2)                    #SetMarkerColor(2) : rot
    graph1.SetTitle("x^2")                      #Legt Titel an, der spaeter in der Legende benutzt wird

    graph2.SetMarkerStyle(21)                   #Rechtecke
    graph2.SetMarkerColor(3)                    #gruen
    graph2.SetTitle("Zwei Graphen;#it{x};#it{y}")   #Titel
    graph2.GetXaxis().SetDecimals()
    graph2.GetYaxis().SetDecimals()

    graph2.Draw("AP")                           #Traegt Graph auf TCanvas-Objekt auf
    graph1.Draw("P")

    legend = ROOT.TLegend(0.9,0.7,0.7,0.9)
    legend.AddEntry(graph1,"#it{x}^{2}","p")
    legend.AddEntry(graph2,"cos(#it{x})","p")
    legend.SetHeader("Legende")
    legend.Draw()

    canv.Modified()
    canv.Update()
   #canv.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe2/graph.jpg")



if __name__ == "__main__":
    data = aufg1()
    aufg2(data)
