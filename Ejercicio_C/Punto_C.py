import matplotlib.pyplot as plt         #Librería para graficar
import numpy as np                      #Libreria para manejar arreglos y operaciones de una manera rapida
import random                           #librería generador de numeros pseudo aleatorios
import math                             #libreria matemática

#Punto C
#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 1
#----------------------------------------------------------------------------------------------------------------------------------------


#Definimos la probabilidad
prob=1/11

#Función que calcula la función de masa de probabilidad de la variable aleatoria
def masa_prob(x):
    global prob
    if x>=0:
        return prob*math.exp(-prob*x)
    return 0

#Función que calcula la función probabilidad acumulada de la variable aleatoria
def acumm_prob(x):
    global prob
    if x>=0:
        return 1-math.exp(-prob*x)
    return 0

#Función que simula la variable aleatoria
def generator(x):
    global prob
    return math.log(1-x)/-prob
    
#Graficación del histograma con la densidad superpuesta
data=[]
for i in range(10000):
    data.append(generator(random.random()))

plt.hist(data,density=True,alpha=0.5,bins=50,histtype='bar',
         ec='black')

dominio=np.arange(-0.5,100,0.001)
masa=[]

for i in dominio:
    masa.append(masa_prob(i))

plt.plot(dominio,masa)

plt.show()

acumm=[]
for i in dominio:
    acumm.append(acumm_prob(i))

plt.plot(dominio,acumm)
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 2
#----------------------------------------------------------------------------------------------------------------------------------------


#Función que calcula la función de masa de probabilidad de la variable aleatoria
def masa_prob(x):
    
    if (x>=0 and  x<=2) or (x>=4 and  x<=6):
        return 1/4
    return 0

#Función que calcula la función probabilidad acumulada de la variable aleatoria
def acumm_prob(x):
    
    if x>=0 and x<=2:
        return x/4
    elif x>2 and x<4:
        return 1/2
    elif x>=4 and x<=6:
        return x/4-1/2
    elif x>6:
        return 1
    return 0

#Función que simula la variable aleatoria
def generator(x):
    if x<1/2:
        return 4*x
    return 4*(x+1/2)
    
#Graficación del histograma con la densidad superpuesta
data=[]
for i in range(10000):
    data.append(generator(random.random()))

plt.hist(data,density=True,alpha=0.5,bins=30,histtype='bar', ec='black')

dominio=np.arange(-0.5,8,0.001)
masa=[]

for i in dominio:
    masa.append(masa_prob(i))

plt.plot(dominio,masa)
plt.show()

acumm=[]

for i in dominio:
    acumm.append(acumm_prob(i))

plt.plot(dominio,acumm)

plt.show()
#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 3
#----------------------------------------------------------------------------------------------------------------------------------------

#Función que calcula la función de masa de probabilidad de la variable aleatoria
def masa_prob(x):
    
    if (x>=0 and  x<=10) :
        return x/150
    elif (x>=10 and  x<=30) :
        return 1/10-x/300
    return 0

#Función que calcula la función probabilidad acumulada de la variable aleatoria
def acumm_prob(x):
    
    if x>=0 and x<=10:
        return x**2/300
    elif x>10 and x<=30:
        return x/10+(-x**2)/600-1/2
    elif x>30:
        return 1
    return 0

#Función que simula la variable aleatoria
def generator(x):
    if x<=1/3:
        return (x*300)**(1/2)
    b=-60
    c=-2400
    z1=-(b+(c*x-c)**(1/2))/2
    
    return z1
   
    
#Graficación del histograma con la densidad superpuesta
data=[]
for i in range(10000):
    data.append(generator(random.random()))

plt.hist(data,density=True,alpha=0.5,bins=30,histtype='bar', ec='black')

dominio=np.arange(-0.5,40,0.001)
masa=[]

for i in dominio:
    masa.append(masa_prob(i))

plt.plot(dominio,masa)
plt.show()
acumm=[]

for i in dominio:
    acumm.append(acumm_prob(i))

plt.plot(dominio,acumm)
plt.show()
