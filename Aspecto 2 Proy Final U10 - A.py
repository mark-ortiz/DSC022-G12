"""
Created on Fri Sep 25 21:23:23 2020
Programa creado para el Aspecto 2 del Proyecto Final de IA - Doctorado
@author: Marco Ortiz
"""
#Importamos los módulos que utilizaremos
import numpy as np
import matplotlib.pyplot as plt
import time 
from smt.sampling_methods import Random

#Tomamos el tiempo al inicio de la ejecución
t0=time.clock()
#Definimos un vector (poblacion inicial) para realizar el sampling
xlimits = np.array([[0.0, 4.0], [0.0, 3.0]])
sampling = Random(xlimits=xlimits)

num = 50
x=sampling(num)
#Tomamos el tiempo al finalizar la ejecución del algoritmo
t1=time.clock()

print("El vector de salida tiene forma:", x.shape)
#Imprimimos los puntos seleccionados por el sampling
plt.plot(x[:, 0], x[:, 1], "o")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print("El tiempo de ejecución del programa fue:", t1-t0)
print("Si se realizan 30K iteraciones:", 30000*(t1-t0))