#coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
#print(iris)
print(iris['class'].value_counts())

x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], 
                              test_size = 0.5, stratify = iris.iloc[:, 4])

print(y.value_counts())

infert = pd.read_csv('infert.csv')
print(infert)

print(infert['education'].value_counts())

#exemplo estratificado para retornar 100 registros
#como sabemos que infert tem 248 registros, para ter 100 de amostra
#temos que usar o indice 0.6 (248*0.6)=148. se retirarmos o 148 do 248, 
#fica 100, que é a amostra que queremos
x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1],
                                test_size = 0.6, stratify=infert.iloc[:, 1])

print(y1.value_counts())