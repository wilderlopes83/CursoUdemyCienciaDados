# coding: utf-8

#amostra sistematica é a que definimos seguindo algum padrão sistemático previamente escolhido
#neste exemplo, ideia é buscar amostra de 15 no arquivo iris.csv, utilizando um numero sistematico 
#entre 1 e 10 e depois ir somando pela divisão entre população e amostra (no exemplo abaixo, de 10 em 10)

import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15

#ceil realiza arredondamento para cima
k = ceil(populacao / amostra)

#k+1 pois o limite superior nao entra
r = np.random.randint(low = 1, high = k+1, size = 1)

print(r)

acumulador = r[0]
sorteados = []

for i in range(amostra):
    sorteados.append(acumulador-1) #coloquei -1 pq indice do vetor começa em 0
    acumulador += k

print(sorteados)

base = pd.read_csv('iris.csv')
base_final = base.loc[sorteados]

print(base_final)