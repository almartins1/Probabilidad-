import matplotlib.pyplot as plt         #Librería para graficar
import numpy as np                      #Libreria para manejar arreglos y operaciones de una manera rapida
import random                           #librería generador de numeros pseudo aleatorios
import math                             #libreria matemática
from prettytable import PrettyTable     #libreria para imprimir tablas tablas

#Punto D
#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 1
#----------------------------------------------------------------------------------------------------------------------------------------
#Simulación de la variable aleatoria para m=10000 
simY=[]

for i in range(0,10000):
  simY.append(np.exp(np.random.normal()))

#Función que calcula la función de densidad de una distribución lognormal
def log_normal(x,media,var):
    ex=np.exp(-(np.log(x)-media)**2/(2*var))
    distribucion=ex/(x*(var*2*np.pi)**0.5)
    return distribucion

#Graficación de del histograma de variable aleatoria del ejercicio 1, con la función de densidad de una distribución lognormal superpuesta
dominio=np.arange(0.001,12,0.001)
rango=log_normal(dominio,0.3,0.5)
data=np.random.normal(0.3,0.5**0.5,10000)
y=np.exp(data)
plt.hist(y,density=True,alpha=0.5, histtype='bar', ec='black',bins=np.linspace(0,11,50))
plt.plot(dominio,rango)
plt.show()
#Función que calcula los momentos, de manera teorica, de la variable aleatoria dada en el ejercicio 1 y 2
def momentos(r,media,var):
    return np.exp(media*r+var*r**2/2)
print("Teorico : ",momentos(1,0.3,0.5),momentos(2,0.3,0.5),momentos(5,0.3,0.5))

#Función que calcula los momentos, usando el metodo 3, de la varianle aleatoria dada en el ejercicio 1 y 2
def metodo3(r,moment):
    data=np.random.normal(0.3,0.5**0.5,r)
    y=np.exp(data)**moment
    return np.sum(y)/r
x = PrettyTable() #Impresión de los datos en una tabla
x.field_names = ["  ","E[Y]", "E[Y**2]", "E[Y**5]"]
for i in [10,100,1000, 10000]:
    x.add_row(["r="+str(i),metodo3(i,1),metodo3(i,2),metodo3(i,5)])
print(x)

#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 2
#----------------------------------------------------------------------------------------------------------------------------------------
#Función simulación, que utiliza el método 3 para m realizaciones independientes para un cierto r, y un momento definido
def simulation(m,r,moment):
    result=[]
    for i in range(m):
        result.append(metodo3(r,moment))
    
    return result

#Evaluación y graficación para r=10,100,1000 y 10000, con m=10000
plt.hist(simulation(10000,10,1),alpha=0.5, histtype='bar', ec='black',bins=np.linspace(0.5,4,50))
plt.axvline(x=momentos(1,0.3,0.5), ymin=0, ymax=8000,color="red")
plt.grid()
plt.show()

plt.hist(simulation(10000,100,1),alpha=0.5, histtype='bar', ec='black',bins=np.linspace(1.3,2.5,50))
plt.axvline(x=momentos(1,0.3,0.5), ymin=0, ymax=8000,color="red")
plt.grid()
plt.show()

plt.hist(simulation(10000,1000,1),alpha=0.5, histtype='bar', ec='black',bins=np.linspace(1.5,2,50))
plt.axvline(x=momentos(1,0.3,0.5), ymin=0, ymax=8000,color="red")
plt.grid()
plt.show()
print("")

#----------------------------------------------------------------------------------------------------------------------------------------
#Bonus
#----------------------------------------------------------------------------------------------------------------------------------------
#Función que implementa el método 3 para distribución de Cauchy

def cauchy(r,m):
    result=[]
    for i in range(m):
        a=np.random.standard_cauchy(r)
        result.append(np.sum(1/a)/r)
    return result

#Evaluación y graficación para r=10,100,1000 y 10000, con m=10000
plt.hist(cauchy(10,10000),density=True,alpha=0.5, histtype='bar', ec='black',bins=np.linspace(-10,10,70))
plt.grid()
plt.show()

plt.hist(cauchy(100,10000),density=True,alpha=0.5, histtype='bar', ec='black',bins=np.linspace(-10,10,70))
plt.grid()
plt.show()

plt.hist(cauchy(1000,10000),density=True,alpha=0.5, histtype='bar', ec='black',bins=np.linspace(-10,10,70))
plt.grid()
plt.show()

plt.hist(cauchy(10000,10000),density=True,alpha=0.5, histtype='bar', ec='black',bins=np.linspace(-10,10,70))
plt.grid()
plt.show()