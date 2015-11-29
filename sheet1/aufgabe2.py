from __future__ import print_function, unicode_literals, division
import ROOT
import numpy as np
import matplotlib.pyplot as plt

#Bein Durchfuehren wird zunerst der Plot angezeigt. Schliesst man diesen, erscheinen im Terminal die Werte zu Aufgabenteil (b) und (c)

def aufg2():
	import ROOT
	import numpy as np

	
#Aufgabenteil a)
	#analytisches ergebnis:
	ana=2/3
	x1=np.linspace(1,10000000,10000000)
	y1=(x1**3+1/3)-(x1**3-1/3)
	
	print("Aufgabenteil a)")
	#prüfen ab welchem x der numerische um mehr als 1% vom analytischen wert abweicht
	for i in range(0,10000000):
		if ana-y1[i] > 0.01:
			print("Abweichung kleiner 1% im Intervall [" + str(-x1[i]) + "," +str(x1[i])+ "]")
			break

	#prüfen wann das numerische ergebnis Null ergibt
	for i in range(0,10000000):
		if y1[i] == 0:
			print("numerisches Ergebnis gleich Null für x>=" + str(x1[i]) + " , x <=" + str(-x1[i]))
			break

#Aufgabenteil b)
	x2=np.linspace(1,.0000001,10000000)
	y2=((3+x2**3/3)-(3-x2**3/3))/x2**3

	print("Aufgabenteil b)")
	#prüfen ab welchem x der numerische um mehr als 1% vom analytischen wert abweicht
	for i in range(0,10000000):
		if ana-y2[i] > 0.01:
			print("Abweichung größer 1% im Intervall [" + str(-x2[i]) + "," +str(x2[i])+ "]")
			break

	#prüfen wann das numerische ergebnis Null ergibt
	for i in range(0,10000000):
		if y2[i] == 0:
			print("numerisches Ergebnis gleich Null im Intervall [" + str(-x2[i]) + "," +str(x2[i])+ "]")
			break


# Funktionen definieren 
def f(x):
    return (x**3 + 1/3) - (x**3 - 1/3)
def g(x):
    return ((3 + x**3/3) - (3 - x**3/3)) / x**3

#Algebraisches Resultat bestimmen: 2/3
ergebnis = 2/3
x = np.logspace(-5, 5, 1000)						#(a,b,n): generiert n Werte zwischen 10^a and 10^b

def deltaf(x):
    return f(x) - ergebnis

def deltag(x):
    return g(x) - ergebnis



#Graphische veranschaulichung der Abweichungen vom numerischen zum algebraischen Wert - Aufgabenteil (c)
#Einstellungen Plot f(x)
fig = plt.figure()
fig.subplots_adjust(hspace=1)                       #Abstand zwischen den einzelnen Canvas
ax1 = fig.add_subplot(211)                          #y-Richtung (2 Felder), x-Richtung (1 Feld), Ausgewähltes Feld
plt.semilogx(x,deltaf(x),'r.')
plt.xlim(10**(-5), 10**5)
plt.title("deltaf")

#Einstellungen plot g(x)
ax2 = fig.add_subplot(212)
plt.semilogx(x,deltag(x), 'b.')
plt.xlim(10**(-5), 10**5)
plt.title("deltag")

plt.show()

if __name__ == '__main__':
	aufg2()