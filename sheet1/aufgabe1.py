from __future__ import unicode_literals, print_function, division
import matplotlib.pyplot as plt

def aufg1():
    import numpy as np
    import ROOT as ROOT


#Funktion definieren
#def function(x):
#    return (1-x)**6

    x = np.arange(0.999, 1.001, 0.00001)
    y1 = (1-x)**6
    y2 = x**6-6*x**5+15*x**4-20*x**3+15*x**2-6*x+1
    y3 = 1+x*(-6+x*(15+x*(-20+x*(15+x*(-6+x)))))

#Normal
    fig = plt.figure()
    fig.subplots_adjust(hspace=1)						#Abstand zwischen den einzelnen Canvas
    ax1 = fig.add_subplot(311)							#y-Richtung (3 Felder), x-Richtung (1 Feld), Ausgewähltes Feld
    ax1.plot(x,y1)
    plt.xlim(0.999, 1.001)
    plt.title("Direkt")

#Naib binomisch
    ax2 = fig.add_subplot(312)
    ax2.plot(x,y2)
    plt.xlim(0.999, 1.001)
    plt.title("Naiv binomisch")

#Horner Schema
    ax3 = fig.add_subplot(313)
    ax3.plot(x,y3)
    plt.xlim(0.999, 1.001)
    plt.title("Horner Polynom")

    plt.show()

if __name__ == '__main__':
	aufg1()





