from __future__ import print_function, unicode_literals, division

def aufg2():
    import numpy as np
    import ROOT 

#Binning
############ Aufgabenteil (a) #############


#Einlesen der Daten und Darstellung:
    gewicht, groesse = np.loadtxt("Gewicht_Groesse.txt", unpack=True)

#Erstellen des Canvas in der gewuenschten Unterteilung
    canvas = ROOT.TCanvas("canvas", "canvas", 800, 600)
    canvas.Divide(3, 2)

#Erstellen der verschiedenen Bins
    hists = []
    for i, n in enumerate([5, 10, 15, 20, 30, 50]):
        canvas.cd(i + 1)
        name = "hist" + str(n)
        hists.append(ROOT.TH2F(name, name, n, gewicht.min(), gewicht.max(), n, groesse.min(), groesse.max()))                                         #TH2F: 2dim Histogramm
        for data in zip(gewicht, groesse):                                          #i-tes Tupel mit i-tem Element von jedem Argument
            hists[i].Fill(*data)                     
        hists[i].Draw("COLZ")                                                       #x gegen y mit COLZ-Funktion plotten
    
#Canvas speichern
    canvas.SaveAs("Aufgabe2a.pdf")

############ Aufgabenteil (c) #############


#Gleichverteilte Zahlen ziehen, logarithmieren und darstellen:
    data = []
    rand = ROOT.TRandom3(0)                                                         #Destruktor
    for i in range(0, 10**5):                                                       #10^5 gleichverteilte Zahlen ziehen
        data.append(rand.Rndm() * 100)                                              #.Rndm() erzeugt Werte ]0,1] -> mal 100
        #print(data)                                                                #Generierte Werte ueberpruefen
    data = np.log(data)




#Erstellen des Canvas in der gewuenschten Unterteilung
    canvas = ROOT.TCanvas("canvas", "canvas", 800, 600)
    canvas.Divide(3, 2)

#Histogramme mit entsprechenden Binanzahlen erstellen
    hists = []
    for i, n in enumerate(range(5, 65, 10)):                                        #andere Einstellung um Bins zu generieren: ueber range
        canvas.cd(i + 1)
        name = "hist" + str(n)
        hists.append(ROOT.TH1F(name, name, n, data.min(), data.max()))              #TH1F: 1dim Histogramm
        for d in data: 
            hists[i].Fill(d)
        hists[i].Draw("COLZ")

#Canvas speichern
    canvas.SaveAs("Aufgabe2c.pdf")

if __name__ == '__main__':
    aufg2()