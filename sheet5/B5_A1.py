import ROOT
import numpy as np
import matplotlib.pyplot as plt
from root_numpy import root2array

def aufg1():

###########
#Aufgabenteil a)
###########
	file_name = ROOT.TFile("zwei_populationen.root",'OPEN')
	
	P0 = file_name.Get('P_0_10000')
	l0 = P0.GetEntries()

	P1 = file_name.Get('P_1')
	l1 = P1.GetEntries()

	P0_array = np.zeros((2,l0))
	P1_array = np.zeros((2,l1))

	P0_array[0] = root2array("zwei_populationen.root",'P_0_10000')['x']
	P0_array[1] = root2array("zwei_populationen.root",'P_0_10000')['y']
	P1_array[0] = root2array("zwei_populationen.root",'P_1')['x']
	P1_array[1] = root2array("zwei_populationen.root",'P_1')['y']
	

	fig = plt.figure
	plt.hist2d(P0_array[0],P0_array[1],bins=50, alpha=1.)
	plt.colorbar()
	fig = plt.figure
	plt.hist2d(P1_array[0],P1_array[1],bins=50,alpha=0.7)
	plt.show()

############
#Aufgabenteilb)
############
#Berechnen der Mittelwerte von Population P_0_10000
	P0_mean = np.zeros((2,1))
	P0_mean[0] = np.mean(P0_array[0])
	P0_mean[1] = np.mean(P0_array[1])
	print(P0_mean)

#Berechnen der Mittelwerte von Population P_1
	P1_mean = np.zeros((2,1))
	P1_mean[0] = np.mean(P1_array[0])
	P1_mean[1] = np.mean(P1_array[1])
	print(P1_mean)

##########
#Aufgabenteil c)
##########

#Berechnen der Kovarianzmatrizen
	S0 = np.cov(P0_array[0],P0_array[1])
	print(S0)
	S1 = np.cov(P1_array[0],P1_array[1])
	print(S1)

#Berechnen der Kombinierten Kovarianzmatrix 
	S01 = S0+S1
	print(S01)

#Invertieren der kombinierten Kovarianzmatrix
	S01_invers = np.linalg.inv(S01)
	#print(S01_invers)

##########
#Aufgabenteil d)
###########

#Differenz der Mittelwerte der Populationen
	mean_diff = P0_mean-P1_mean
	#print(mean_diff)
	
#berechnen von Lambda
	lamda = np.dot(S01_invers,mean_diff)
	#print(lamda)

	lamda_norm = lamda/np.linalg.norm(lamda)
	steigung = lamda[1]/lamda[0]
	#print(lamda_norm)
	print(steigung)

#############
#Aufgabenteil e)
#############

#Projektion 
	P0_pro = np.dot(lamda_norm.T,P0_array)
	P1_pro = np.dot(lamda_norm.T,P1_array)
	
	pmin = np.min(np.append(P0_pro,P1_pro))
	pmax = np.max(np.append(P0_pro,P1_pro))
	cut = np.linspace(pmin,pmax,200)

#Funktion zur bestimmung der Effizienz udn Reinheit
	def effizienzundreinheit(cut,signal,untergrund):
		tp=0.
		fp=0.
		fn=0.
		effizienz=0.
		reinheit=0.
		for i in range(len(signal)):
			if (signal[0,i] >= cut):
				tp = tp+1
			else:
				fn = fn+1
		for j in range(len(untergrund)):
			if (untergrund[0,j] >= cut):
				fp = fp+1
		if (tp+fn) == 0:
			effizienz = 0
		else:
			effizienz = tp/(tp+fn)
		if (tp+fp) == 0:
			reinheit = 0
		else:
			reinheit = tp/(tp+fp)
		return effizienz, reinheit

#Berechnen von Effizeinz udn Reinheit
	e = np.zeros((1,len(cut)))
	r = np.zeros((1,len(cut)))
	for i in range(len(cut)):
		e[0,i],r[0,i] = effizienzundreinheit(cut[i],P0_pro,P1_pro)


#PLotten der Effizienz und Reinheit
	EffizienzundReinheit = ROOT.TCanvas("EffizienzundReinheit", "EffizienzundReinheit", 400,300) #Canvas öffnen
	graph_effizienz = ROOT.TGraph(len(cut),cut,e[0,:])
	graph_effizienz.SetMarkerStyle(5)
	graph_effizienz.SetMarkerColor(2) #Farbe
	graph_effizienz.GetXaxis().SetTitle("lamda_cut") #x-achsen Beschriftung
	graph_effizienz.GetYaxis().SetTitle("") #y-achsen Beschriftung
	graph_effizienz.SetTitle("Effizienz und Reinheit") #Titel setzen 
	graph_effizienz.Draw("ALP") # A: Achsen plotten, P aktuellen Marker an Punkte plotten

	graph_reinheit = ROOT.TGraph(len(cut),cut,r[0,:])
	graph_reinheit.SetMarkerStyle(2) 
	graph_reinheit.SetMarkerColor(8) #Farbe
	graph_reinheit.Draw("LP") # A: Achsen plotten, P aktuellen Marker an Punkte plotten

	leg= ROOT.TLegend (0.1,0.7,0.48,0.9) #Legende erstellen
	leg.SetHeader("Legende")
	leg.AddEntry(graph_effizienz,"Effizienz","lp")
	leg.AddEntry(graph_reinheit,"Reinheit","lp")
	leg.Draw()
	EffizienzundReinheit.Update()
	#EffizienzundReinheit.SaveAs("2b.pdf") #Speichern
	#input()


###########
#Aufgabenteil f)
###########

#Funktion zu Berechnung des Signal-Untergrund-Verhältnisses
	def verhaeltnis_func (cut,signal,untergrund):
		tp=0.
		fp=0.
		for i in range(len(signal)):
			if (signal[0,i] >= cut):
				tp = tp+1
		for j in range(len(untergrund)):
			if (untergrund[0,j] >= cut):
				fp = fp+1
		if fp == 0:
			return 0
		else:
			return tp/fp

#Berechnen des Verhältnisses
	verhaeltnis=np.zeros(len(cut))
	for i in range(len(cut)):
		verhaeltnis[i] = verhaeltnis_func(cut[i],P0_pro,P1_pro)

#Plotten des Verhältnisses
	Verhaeltnis = ROOT.TCanvas("Verhaeltnis", "Verhaeltnis", 400,300) #Canvas öffnen
	graph_Verhaeltnis = ROOT.TGraph(len(cut),cut,verhaeltnis)
	graph_Verhaeltnis.SetMarkerStyle(5)
	graph_Verhaeltnis.SetMarkerColor(2) #Farbe
	graph_Verhaeltnis.GetXaxis().SetTitle("lamda_cut") #x-achsen Beschriftung
	graph_Verhaeltnis.GetYaxis().SetTitle("") #y-achsen Beschriftung
	graph_Verhaeltnis.SetTitle("Verhaeltnis") #Titel setzen 
	graph_Verhaeltnis.Draw("ALP") # A: Achsen plotten, P aktuellen Marker an Punkte plotten

#############
#Aufgabenteil g)
##############

#Funktion zur berechnung der Signifikanz
	def signifikanz_func (cut,signal,untergrund):
		tp=0.
		fp=0.
		for i in range(len(signal)):
			if (signal[0,i] >= cut):
				tp = tp+1
		for j in range(len(untergrund)):
			if (untergrund[0,j] >= cut):
				fp = fp+1
		if (tp+fp) == 0:
			return 0
		else:
			return tp/(np.sqrt(tp+fp))

#berechnung der Signifikanz
	signifikanz = np.zeros(len(cut))
	for i in range(len(cut)):
		signifikanz[i] = signifikanz_func(cut[i],P0_pro,P1_pro)

#Plotten der Signifikanz
	Signifikanz = ROOT.TCanvas("Signifikanz", "Signifikanz", 400,300) #Canvas öffnen
	graph_Signifikanz = ROOT.TGraph(len(cut),cut,signifikanz)
	graph_Signifikanz.SetMarkerStyle(5)
	graph_Signifikanz.SetMarkerColor(2) #Farbe
	graph_Signifikanz.GetXaxis().SetTitle("lamda_cut") #x-achsen Beschriftung
	graph_Signifikanz.GetYaxis().SetTitle("") #y-achsen Beschriftung
	graph_Signifikanz.SetTitle("Signifikanz") #Titel setzen 
	graph_Signifikanz.Draw("ALP") # A: Achsen plotten, P aktuellen Marker an Punkte plotten


####################
#Aufgabenteil h)
###################

	P2 = file_name.Get('P_0_1000')
	l2 = P2.GetEntries()

	P2_array = np.zeros((2,l2))

	P2_array[0] = root2array("zwei_populationen.root",'P_0_1000')['x']
	P2_array[1] = root2array("zwei_populationen.root",'P_0_1000')['y']

	P2_mean = np.zeros((2,1))
	P2_mean[0] = np.mean(P2_array[0])
	P2_mean[1] = np.mean(P2_array[1])
	#print(P2_mean)

	S2 = np.cov(P2_array[0],P2_array[1])
	print(S2)
	S02 = S2+S1
	print(S02)

	S02_invers = np.linalg.inv(S02)
	print(S02_invers)
	mean_diff2 = P2_mean-P1_mean
	print(mean_diff2)
	
	lamda2 = np.dot(S02_invers,mean_diff2)
	print(lamda2)

	lamda_norm2 = lamda2/np.linalg.norm(lamda2)
	steigung2 = lamda2[1]/lamda2[0]
	print(lamda_norm)
	print(steigung)

	P2_pro = np.dot(lamda_norm.T,P2_array)
	
	pmin2 = np.min(np.append(P2_pro,P1_pro))
	pmax2 = np.max(np.append(P2_pro,P1_pro))
	cut2 = np.linspace(pmin2,pmax2,200)

	e2 = np.zeros((1,len(cut2)))
	r2 = np.zeros((1,len(cut2)))
	for i in range(len(cut2)):
		e2[0,i],r2[0,i] = effizienzundreinheit(cut2[i],P2_pro,P1_pro)

	EffizienzundReinheit2 = ROOT.TCanvas("EffizienzundReinheit2", "EffizienzundReinheit2", 400,300) #Canvas öffnen
	graph_effizienz2 = ROOT.TGraph(len(cut2),cut2,e2[0,:])
	graph_effizienz2.SetMarkerStyle(5)
	graph_effizienz2.SetMarkerColor(2) #Farbe
	graph_effizienz2.GetXaxis().SetTitle("lamda_cut") #x-achsen Beschriftung
	graph_effizienz2.GetYaxis().SetTitle("") #y-achsen Beschriftung
	graph_effizienz2.SetTitle("Effizienz und Reinheit") #Titel setzen 
	graph_effizienz2.Draw("ALP") # A: Achsen plotten, P aktuellen Marker an Punkte plotten

	graph_reinheit2 = ROOT.TGraph(len(cut2),cut2,r2[0,:])
	graph_reinheit2.SetMarkerStyle(2) 
	graph_reinheit2.SetMarkerColor(8) #Farbe
	graph_reinheit2.Draw("LP") # A: Achsen plotten, P aktuellen Marker an Punkte plotten

	leg= ROOT.TLegend (0.1,0.7,0.48,0.9) #Legende erstellen
	leg.SetHeader("Legende")
	leg.AddEntry(graph_effizienz2,"Effizienz","lp")
	leg.AddEntry(graph_reinheit2,"Reinheit","lp")
	leg.Draw()
	EffizienzundReinheit.Update()
	#input()

	verhaeltnis2 = np.zeros(len(cut2))
	for i in range(len(cut2)):
		verhaeltnis2[i] = verhaeltnis_func(cut2[i],P2_pro,P1_pro)

	Verhaeltnis2 = ROOT.TCanvas("Verhaeltnis2", "Verhaeltnis2", 400,300) #Canvas öffnen
	graph_Verhaeltnis2 = ROOT.TGraph(len(cut2),cut2,verhaeltnis2)
	graph_Verhaeltnis2.SetMarkerStyle(5)
	graph_Verhaeltnis2.SetMarkerColor(2) #Farbe
	graph_Verhaeltnis2.GetXaxis().SetTitle("lamda_cut") #x-achsen Beschriftung
	graph_Verhaeltnis2.GetYaxis().SetTitle("") #y-achsen Beschriftung
	graph_Verhaeltnis2.SetTitle("Verhaeltnis") #Titel setzen 
	graph_Verhaeltnis2.Draw("ALP") # A: Achsen plotten, P aktuellen Marker an Punkte plotten


	signifikanz2 = np.zeros(len(cut2))
	for i in range(len(cut2)):
		signifikanz2[i] = signifikanz_func(cut2[i],P2_pro,P1_pro)

	Signifikanz2 = ROOT.TCanvas("Signifikanz2", "Signifikanz2", 400,300) #Canvas öffnen
	graph_Signifikanz2 = ROOT.TGraph(len(cut2),cut2,signifikanz2)
	graph_Signifikanz2.SetMarkerStyle(5)
	graph_Signifikanz2.SetMarkerColor(2) #Farbe
	graph_Signifikanz2.GetXaxis().SetTitle("lamda_cut") #x-achsen Beschriftung
	graph_Signifikanz2.GetYaxis().SetTitle("") #y-achsen Beschriftung
	graph_Signifikanz2.SetTitle("Signifikanz") #Titel setzen 
	graph_Signifikanz2.Draw("ALP") # A: Achsen plotten, P aktuellen Marker an Punkte plotten

	input()
if __name__ == '__main__':
	aufg1()