from __future__ import unicode_literals, division, print_function
import ROOT
import numpy as np
import matplotlib.pyplot as plt

#Aufgabe 1a
x = np.linspace(1, 100, 100)							#Startwert, Endwert, Schrittweite
print(x)												#1 bis 100 chronologisch einfuegen

#array = [np.random.randint(1,100) for _ in range(100)]	#alternative: zufaellig ziehen
#print(array) 



#Aufgabe 1b
N = 100

#Spalten definieren
spalte0 = np.arange(N)+1 								#Ausgabe der Werte bis N -> N selber nicht, daher +1
spalte1 = np.random.uniform(0,1,N)						#Startwert, Endwert, Anzahl der erzeugten Zufallszahlen
spalte2 = np.random.uniform(0,10,N)
spalte3 = np.random.uniform(20,30,N)
spalte4 = np.random.normal(0,1,N)						#Normalverteilung mit Mittelwert 0, Breite 1
spalte5 = np.random.normal(5,2,N)
spalte6 = spalte0**2									#Arrays wenden Rechenoperationen elementweise an
spalte7 = np.cos(spalte0)

#Array auffuellen und printen
ZweiDimArray = np.array([spalte0,spalte1,spalte2,spalte3,spalte4,spalte5,spalte6,spalte7])
#np.set_printoptions(precision=3)						#Anzahl der ausgegebenen Nachkommastellen
print(ZweiDimArray)

