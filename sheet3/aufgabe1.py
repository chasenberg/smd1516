from __future__ import print_function, unicode_literals, division

def aufg1():
    import ROOT as r
    import numpy as np
    import math as m

    GAMMA = 2.7 - 1

    # Datei
    datei = r.TFile("NeutrinoMC.root", "RECREATE")

    ############################
    #a
    ############################

    data = np.zeros((4, 1))
    tree_a = r.TTree("Signal_MC", "Signal_MC")
    tree_a.Branch("Energie", data[0], "x/D")

    #Signale generieren: gibt ein TH1D-Objekt zurueck. xmin: untere Grenze, n:anzahl der Ereignisse
    def signalereignis_hist(xmin, n):
        x_min = np.power(xmin, GAMMA)
        x_max = 0
        
        #Zufallsgenerator erzeugen
        rnd1 = r.TRandom3(1);
        
        #Histogramm fuer das Signal
        histogramm_ort = r.TH1D("histogramm_ort","histogramm_ort", 30, np.log10(xmin), 4)
        histogramm_ort.GetXaxis().SetTitle("log(E/TeV)")
        histogramm_ort.GetYaxis().SetTitle("Anzahl Ereignisse")    

        #Zufallszahlen zwischen x_max un x_min erzeugen und in Histogramm speichern
        
        for i in range(n):
            data[0] = 1./np.power(x_min+rnd1.Rndm()*(x_max-x_min), 1./GAMMA)
            tree_a.Fill()
            histogramm_ort.Fill(np.log10(data[0]))

        return histogramm_ort

    tree_a.Write()


    #gewuenschte Anzahl N der Signalereignisse
    N = np.int_(1e5)
    xmin = 1.0
    xmax = 1e6
    #Datei
    canv_signal = r.TCanvas("canv_signal", "canv_signal", 800, 600)
    canv_signal.SetLogy()
    signal = signalereignis_hist(xmin, N)
    signal.DrawCopy()
    canv_signal.SaveAs("Blatt3A1a.pdf")
    #signal.Write()
    #canv_signal.Write()


    #b
    #Erzeugung eines neuen Tree
    tree_b = r.TTree("Signal_MC_Akzeptanz", "Signal_MC_Akzeptanz")
    #Abspeichern der Ergebnisse
    tree_b.Branch("Signal_MC_Akzeptanz", data[0], "x/D")
    #Berücksichtigung der Akzeptanz mit der Neumannmethode
    def akzeptanz_hist(xmin, n):
        x_min = np.power(xmin, GAMMA)
        x_max = 0
        
        #Zufallsgenerator mit gleichem Seed wie im ersten Aufgabenteil
        rnd1 = r.TRandom3(1)
        #Zufallsgenerator für die Akzeptanz
        rnd2 = r.TRandom3(2)
        #Erzeugung eines TH1D Objekts
        hist_akzeptanz = r.TH1D("hist_akzeptanz", "hist_akzeptanz", 20, np.log10(xmin), 4)
        hist_akzeptanz.GetXaxis().SetTitle("log(E/TeV)")
        hist_akzeptanz.GetYaxis().SetTitle("Anzahl Ereignisse")

        for i in range(n):
            ereignis = 1./np.power(x_min+rnd1.Rndm()*(x_max-x_min), 1./GAMMA) #Generation der Signalevents wie im ersten Teil
            y = np.power((1 - m.exp(-1*ereignis/2)),3); #Einsetzen der Events in Akzeptanzfunktion
            y_rndm = rnd2.Rndm(); #Erzeugung von gleichverteilten Zahlen
            
            if (y_rndm <= y):  #Anwendung des Rückweisungskriteriums
                hist_akzeptanz.Fill(np.log10(ereignis))
                data[1] = ereignis
                tree_b.Fill()
        return hist_akzeptanz
    tree_b.Write()
    #Erzeugung eines Canvas
    canv_akzeptanz = r.TCanvas("canv_akzeptanz", "canv_akzeptanz", 800,600)
    canv_akzeptanz.SetLogy()

    akzeptanz = akzeptanz_hist(xmin, N)
    akzeptanz.DrawCopy()
    canv_akzeptanz.SaveAs("Blatt3A1b.pdf")

    #c

    #Standardabweichung
    sigma = 0.2

    def energiemessung_hist(xmin, n, sigma):
        x_min = np.power(xmin, GAMMA)
        x_max = 0

        rnd1 = r.TRandom3(1)
        rnd2 = r.TRandom3(2)
        rnd3 = r.TRandom3(3)

        hist_energie = r.TH1D("hist_energie", "hist_energie", 20, 0, 5)
        hist_energie.GetXaxis().SetTitle("log(Anzahl Hits)")
        hist_energie.GetYaxis().SetTitle("Anzahl Ereignisse")
        
        for i in range(n):
            ereignis = 1./np.power(x_min + rnd1.Rndm()*(x_max - x_min), 1./GAMMA)
            y = np.power((1-m.exp(-1*ereignis/2)),3)
            y_rndm = rnd2.Rndm()
            
            if (y_rndm <= y):
                while(1):    #immer true 
                    v1 = rnd3.Rndm()*2 - 1
                    v2 = rnd3.Rndm()*2 - 1
                    q = v1*v1 + v2*v2
                    if ((q>=1) or (q==0)): #Check ob Rückweisungsbedingung erfüllt ist
                        continue
                    else:
                        z1 = m.sqrt((-2*np.log(q))/q) #Gaussverteilte Zufallszahl
                        x1 = v1*z1
                        #Transformation der Gaussverteilten  von (0,1) auf (E,0.2E)
                        x1 = sigma*ereignis*x1 + ereignis
                        hits = np.int_(10*x1)
                        if(hits>0):
                            hist_energie.Fill(np.log10(hits))
                        break

        return hist_energie

    canv_energie = r.TCanvas("canv_energie", "canv_energie", 800,600)
    canv_energie.SetLogy()

    energie = energiemessung_hist(xmin, N, sigma)
    energie.DrawCopy()
    canv_energie.SaveAs("Blatt3A1c.pdf")


    #d

    tree_d = r.TTree("Signal_MC_Akzeptanz", "Signal_MC_Akzeptanz")
    tree_d.Branch("AnzahlHits", data[1], "b/D")
    tree_d.Branch("x", data[2], "x/D")
    tree_d.Branch("y", data[3], "y/D")

    def ortsmessung_hist(xmin, n, sigma):
        x_min = np.power(xmin, 1.7)
        x_max = 0

        rnd1 = r.TRandom3(1)
        rnd2 = r.TRandom3(2)
        rnd3 = r.TRandom3(3)
        rnd4 = r.TRandom3(4)

        hist_ort = r.TH2D("hist_ort", "hist_ort", 100, 0, 10,100,0,10)
        hist_ort.GetXaxis().SetTitle("x")
        hist_ort.GetYaxis().SetTitle("y")
        
        mittelwert1 = 7.0
        mittelwert2 = 3.0

        for i in range(n):
            ereignis = 1./np.power(x_min + rnd1.Rndm()*(x_max - x_min), 1./GAMMA)
            data[0] = ereignis
            y = np.power((1-m.exp(-1*ereignis/2)),3)
            y_rndm = rnd2.Rndm()
            
            if (y_rndm <= y):
                while(1):    #immer true, Abbruchbedingung weiter unten
                    u = rnd3.Rndm()*2 - 1
                    v = rnd3.Rndm()*2 - 1
                    q = u*u + v*v
                    if(q>=1 or q==0):
                        continue
                    else:
                        p = m.sqrt((-2*np.log(q))/q)
                        x1 = u*p
                        #Trafo von (0,1) auf (E,0.2E)
                        x1 = sigma*ereignis*x1 + ereignis
                        hits = np.int_(10*x1)   
                        #bis hierhin der gleiche Code wie in a)-c)                 
                        if (hits>0):
                            data[1] = hits                    
                            sigma_ort = 1./np.log10(hits)
                            #Fluktuation der Zufallszahlen um die Mittelwerte 7 und 3 herum
                            x_ort = rnd4.Gaus()*sigma_ort + mittelwert1
                            data[2] = x_ort
                            y_ort = rnd4.Gaus()*sigma_ort + mittelwert2
                            data[3] = y_ort
                            tree_d.Fill()
                            hist_ort.Fill(x_ort, y_ort)     #Schreibe die Ortskoordinaten in Histogramm

                        break
        return hist_ort

    canv_ort = r.TCanvas("canv_ort", "canv_ort", 800,600)
    tree_d.Write()

    ort = ortsmessung_hist(xmin, N, sigma)
    ort.DrawCopy("COL")
    canv_ort.SaveAs("Blatt3A1d.pdf")
    #ort.Write()
    #canv_ort.Write()

    #e


    treee = r.TTree("Untergrund_MC", "Untergrund_MC")
    treee.Branch("Energie", data[0], "a/D")
    treee.Branch("untergrund_events", data[1], "b/D")
    treee.Branch("x", data[2], "x/D")
    treee.Branch("y", data[3], "y/D")

    def untergrund_hist(n):

        rnd5 = r.TRandom3(5)
        sigma1 = 3.
        mittelwert1 = 5.
        sigma2 = 3.
        mittelwert2 = 5.
        rho = 0.5

        hist_untergrund = r.TH2D("hist_untergrund", "hist_untergrund", 100, 0, 10, 100 , 0, 10)
        hist_uenergie = r.TH1D("hist_uenergie","hist_uenergie",20,0,4)
        hist_uenergie.GetXaxis().SetTitle("log(Anzahl Hits)");
        hist_uenergie.GetYaxis().SetTitle("Anzahl Ereignisse");

        for i in range(n):
            #zufaellige Anzahl der Hits
            untergrund_events = rnd5.Gaus(2,1)
            hist_uenergie.Fill(untergrund_events)
            x = rnd5.Gaus()
            y = rnd5.Gaus()
            #Transformation der Zufallszahlen mit den angegebenen Formeln
            x1 = m.sqrt(1.- rho*rho)*sigma1*x + rho*sigma1*y + mittelwert1
            y1 = sigma2*y + mittelwert2 
            hist_untergrund.Fill(x1,y1)    
              
            data[1] = untergrund_events
            data[2] = x
            data[3] = y
            treee.Fill()

        return hist_untergrund, hist_uenergie


    untergrund, uenergie = untergrund_hist(100*N)

    canv_untergrund = r.TCanvas("canv_untergrund", "canv_untergrund", 800,600)
    untergrund.DrawCopy("COL")
    canv_untergrund.SaveAs("Blatt3A1e1.pdf")
    #untergrund.Write()
    #canv_untergrund.Write()

    treee.Write()

    canv_uenergie = r.TCanvas("canv_uenergie", "canv_uenergie", 800,600)
    uenergie.DrawCopy()
    canv_uenergie.SaveAs("Blatt3A1e2.pdf")
    #uenergie.Write()
    #canv_uenergie.Write()

    datei.Close()


if __name__ == '__main__':
    aufg1()

