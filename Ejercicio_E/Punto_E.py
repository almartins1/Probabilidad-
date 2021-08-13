import matplotlib.pyplot as plt         #Librería para graficar
import numpy as np                      #Libreria para manejar arreglos y operaciones de una manera rapida
import random                           #librería generador de numeros pseudo aleatorios
import math                             #libreria matemática

#Punto E
#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 1
#----------------------------------------------------------------------------------------------------------------------------------------
#Función para integrar con método 3, para la primera integral
def metodo3e2(a,b,r):
    data=np.random.uniform(a,b,r)
    y=1/((data)**5+1)
    return (b-a)*np.sum(y)/r

#Evaluación para r=10,100,1000 y 10000
print(metodo3e2(11,21,10))
print(metodo3e2(11,21,100))
print(metodo3e2(11,21,1000))
print(metodo3e2(11,21,10000))

#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 2
#----------------------------------------------------------------------------------------------------------------------------------------

#Función para integrar con método 3, para la segunda integral
def metodo3e4(a,b,r):
    data=np.random.uniform(a,b,r)
    y=1/(np.log(data))
    return (b-a)*np.sum(y)/r
    
#Evaluación para r=10,100,1000 y 10000
print(metodo3e4(12,100,10))
print(metodo3e4(12,100,100))
print(metodo3e4(12,100,1000))
print(metodo3e4(12,100,10000))
#----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 3
#----------------------------------------------------------------------------------------------------------------------------------------
#Función para integrar con método 3, para la tercera integral
def metodo3e7(a,b,r):
    data=np.random.uniform(a,b,r)
    y=np.sqrt((np.exp(data**2)+np.tan(data)))
    return (b-a)*np.sum(y)/r
    
#Evaluación para r=10,100,1000 y 10000
print(metodo3e7(0,1,10))
print(metodo3e7(0,1,100))
print(metodo3e7(0,1,1000))
print(metodo3e7(0,1,10000))
