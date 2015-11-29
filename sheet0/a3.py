import ROOT
import numpy as np

gaus1 = np.random.normal(0, 1, 1e4)						#numpy.random.uniform zieht 1000 Zufallszahlen mit Mittelwert=0 und sigma=1, die gleichverteilt sind
gaus2 = np.random.normal(1, 2, 1e4)						#numpy.random.uniform zieht 1000 Zufallszahlen mit Mittelwert=1 und sigma=2, die gleichverteilt sind

hist1 = ROOT.TH1F("hist1", "Standard-Normal-Verteilung", 20, -6, 6)	#Erzeugt TH1F Objekt: Histogramm mit 20 Bins von -6 bis 6
hist2 = ROOT.TH1F("hist2", "Andere Normal-Verteilung", 20, -6, 6)	# "    "							" 				"					

for g1, g2 in zip(gaus1, gaus2):						# zip() nimmt als Argumente die generierten Zahlen und liefert tupel
    hist1.Fill(g1)										# Fill fuellt die Tupel in die Histogramme
    hist2.Fill(g2)

hist1.SetLineColor(2)
hist1.SetLineWidth(2)

hist2.SetLineColor(3)
hist2.SetLineWidth(2)
hist2.SetLineStyle(2)


hist2.Scale(2)											#Skaliert das Histogramm mit 2
hist2.SetBinContent(10, 0)

canv = ROOT.TCanvas("canv", "Normalverteilungen")		#erzeugt das benoetigte Canvas Objekt

ROOT.gStyle.SetOptStat("eniouRM")						#hier wird festgelegt, welche Informationen in der Statistik-Box dargestellt 
														#werden sollen: 1. Zahl der Events, 2. Name des Histogramms, 3. Integral der Bins
														#4. Overflow, 5. Underflow, 6. RMS, 7.
														#die Verwendung von Grossbuchstaben bewirkt, dass die Fehler mit angegeben werden

hist1.Draw()				
hist2.Draw("SAMES")										#Diese Option sorgt dafuer, dass hist2 auf demselben Canvas platziert wird. 
														#Das S am Ende von SAME bewirk, dass die Statistik Box erneut generiert wird

ROOT.gPad.Update()										#Update des Canvas-Objekts nach den Modifikationen
stats2 = hist2.GetListOfFunctions().FindObject("stats")	#Ermittel die statistischen Eigenschaften von der Verteilung in hist2
stats2.SetY1NDC(0.5)
stats2.SetY2NDC(0.1)
stats2.Draw()
#Erstellt die Legende
legend = ROOT.TLegend(0.1, 0.9, 0.3, 0.8)
#Fuegt Mittelwerte und Standardabweichungen zur Legende hinzu
legend.AddEntry(hist1, "Gauss #mu=0, #sigma=1")
legend.AddEntry(hist2, "Gauss #mu=1, #sigma=2")
legend.Draw()

canv.Modified()
canv.Update()

#canv.SaveAs("/Users/christopher/Dropbox/SMD/Code/Blatt0/aufgabe3/Diagramm.pdf")
