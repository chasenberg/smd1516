from __future__ import print_function, division


import matplotlib.pyplot as plt
import numpy as np
import ROOT
from matplotlib import patches

#Gegebene Werte
cov_xy = 4.2
sigma_x = 3.5
sigma_y = 1.5
mu_x = 4
mu_y = 2
rho = cov_xy / (sigma_x * sigma_y)
#Berechnung der Rotation mit der Formel aus dem Skript
alpha = 0.5 * np.arctan((2 * rho * sigma_x * sigma_y) / (sigma_x**2 - sigma_y**2))

#Nutze Parameterform der Ellipsengleichung
t = np.linspace(0,2 * np.pi, 1000)
x = mu_x + sigma_x * np.cos(alpha) * np.cos(t) - sigma_y * np.sin(alpha) * np.sin(t)
y = mu_y - sigma_x * np.sin(alpha) * np.cos(t) + sigma_y * np.cos(alpha) * np.sin(t)
plt.plot(x,y)
plt.savefig("/Users/christopher/Dropbox/SMD/Code/Blatt4/Blatt4_a1.pdf")