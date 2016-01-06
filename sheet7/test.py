from sklearn import tree
import pandas as pd 
import numpy as np 

gamma = pd.read_csv('/Users/christopher/Downloads/Gamma-MC.csv',delimiter=' ')
proton = pd.read_csv('/Users/christopher/Downloads/Proton-MC.csv',delimiter=' ')
a= gamma['photonchargeMean']

print(a)