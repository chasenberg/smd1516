from __future__ import print_function, unicode_literals, division
import numpy as np 
import matplotlib.pyplot as plt


E = 50000000
alpha = 1/137
s = (2 * E)**2
x= np.linspace(0.00000005,-0.00000005,10000)
gamma = 50000000/511
b = np.sqrt(1-gamma**(-2))		#beta Faktor

#Urspruenglicher Wirkungsquerschnitt, numerisch instabil um Theta=0
def k(Theta):
	return ((alpha**2 / s) * (((((2 + (np.sin(Theta)**2)))/(1- b**2 * np.cos(Theta)**2)) - ((2 * np.sin(Theta)**4) / (1- b**2 * np.cos(Theta)**2))**2)) )

#numerisch verbesserter Wirkungsquerschnitt
def h(Theta):
    return ((alpha**2 / s) * (((gamma**2 * (2 + (np.sin(Theta)**2)))/(1 + gamma**2 * b**2 * np.sin(Theta)**2)) - ((gamma**4 * 2 * np.sin(Theta)**4) / (1 + gamma**2 * b**2 * np.sin(Theta)**2)**2) ))


plt.plot(x,k(x), label = "Nicht korrigiert")
plt.plot(x,h(x), label = "Numerisch verbessert")
plt.legend()
plt.show()




