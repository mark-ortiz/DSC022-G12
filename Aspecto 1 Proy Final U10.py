# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:40:23 2020
Programa creado para el Aspecto 1 del Proyecto Final de IA - Doctorado
@author: Marco
"""
import numpy as np
from scipy.optimize import minimize

def rosen(x):
    #Función rosenbrock
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3,0.7,0.8,1.9,1.2])
res = minimize(rosen, x0, method='BFGS',
               options={'xatol': 1e-8, 'disp': True})

print(res.x)