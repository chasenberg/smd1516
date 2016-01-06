from sklearn import tree
import pandas as pd 
import numpy as np 
from sklearn.datasets import load_iris

data = load_iris()
gamma = pd.read_csv('/Users/christopher/Downloads/Gamma-MC.csv',delimiter=' ',)
proton = pd.read_csv('/Users/christopher/Downloads/Proton-MC.csv',delimiter=' ')

gamma.append(proton)
print(data)
'''def encode_target(gamma, target_column):
	gamma_mod = gamma.copy()
	targets = gamma_mod[target_column].unique()
	map_to_int = {name: n for n, name in enumerate(targets)}
	gamma_mod["Target"] = gamma_mod[target_column].replace(map_to_int)

	return (gamma_mod, targets)

gamma2, targets = encode_target(gamma, "photonchargeMean")
print("* gamma2.head()", gamma2[["Target", "photonchargeMean"]].head(),
      sep="\n", end="\n\n")
print("* gamma2.tail()", gamma2[["Target", "photonchargeMean"]].tail(),
      sep="\n", end="\n\n")
print("* targets", targets, sep="\n", end="\n\n")'''
