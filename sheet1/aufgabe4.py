from __future__ import unicode_literals, print_function, division
import numpy as np
import ROOT as ROOT

#Syntax Python:
#def Funktionsname(Parameterliste):
	#Anweisung(en)

# Funktion definieren
def function(x):												
	return (np.sqrt(9-x)-3)/x 											#erhalte Rueckgabewert


# Setze x-Werte in Funktion ein und gebe jeweiligen Funktionswert aus
for i in range(1,21):											
	number = 10**(-i)
	print("x =",number," -> f(x) =",function(number),"\n")	#"\n": neue Zeile
