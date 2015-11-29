from __future__ import print_function, unicode_literals, division
import numpy as np 
import matplotlib.pyplot as plt

E = 50000000
alpha = 1/137
s = (2 * E)**2
x= np.linspace(0,np.pi,10000)
gamma = 50000000/511
b = np.sqrt(1-gamma**(-2))		#beta Faktor
# Verbesserter Wirkungsquerschnitt
def h(Theta):
    return ((alpha**2 / s) * (((gamma**2 * (2 + (np.sin(Theta)**2)))/(1 + gamma**2 * b**2 * np.sin(Theta)**2)) - ((gamma**4 * 2 * np.sin(Theta)**4) / (1 + gamma**2 * b**2 * np.sin(Theta)**2)**2) ))
#Ableitung des verbesserten Wirkungsquerschnitts
def f(Theta):
	return ((alpha**2 / s) *(gamma**2 * np.sin(2 * Theta) * (-2*b**2 * gamma**2 + gamma**2 * (-2*b**4 * gamma**2 + b**2 - 4) * np.sin(Theta)**2+1))/(b**2 * gamma**2 *np.sin(Theta)**2+1)**3)

#Berechnung der Konditionszahl
def cond(Theta):
	return (np.abs(Theta*f(Theta)/h(Theta)))


plt.plot(x,cond(x), label="Verlauf der Konditionszahl")
plt.legend()
plt.show()