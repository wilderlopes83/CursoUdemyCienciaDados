#coding: utf-8

import pandas as pd
import numpy as np

#carga do csv usando o pandas
base = pd.read_csv('iris.csv')
print(base.shape)

#comando abaixo (seed) é para forçar sempre os mesmos resultados
#np.random.seed(2345)

#geracao de amostra randomica usando numpy
amostra = np.random.choice(a=[0,1], size=150, replace = True, p=[0.5, 0.5])
print(amostra)

#tamanho da amostra
print(len(amostra))
#quantidade de resultados = 1
print(len(amostra[amostra==1]))
#quantidade de resultados = 0
print(len(amostra[amostra==0]))