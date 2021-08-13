import matplotlib.pyplot as plt #libreria para graficar
import random                   #libreria generar numeros aleatorios

#Punto B

#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 1
#----------------------------------------------------------------------------------------------------------------------------------------

#Función que calcula la función de masa de probabilidad de la variable aleatoria
def masa_prob(x):
    base=range(6,16)
    
    if x in base:
        return 1/10
    return 0

#Función que calcula la función probabilidad acumulada de la variable aleatoria
def acumm_prob(x):
    prob={6:1/10,7:2/10,8:3/10,9:4/10,10:5/10,
        11:6/10,12:7/10,13:8/10,14:9/10} #Definimos las probabilidades
   
    for i,j in prob.items():
        if i+1>x>=i:
            return prob[i]
    if x>=15:
        return 1
    return 0

#Función que simula la variable aleatoria
def generator(x):
    for i in range(5,16):
        if acumm_prob(i)<x<=acumm_prob(i+1):
            return i+1
    return 1

#Graficación del histograma 
data=[]
for i in range(10000):
    data.append(generator(random.random()))

plt.hist(data,density=True,alpha=0.5,rwidth=0.5,align='left',bins=range(6,17))
plt.show()
#Graficación de la masa de probabilidad teorica
masa=[]
for i in range(5,17):
    masa.append(masa_prob(i))

plt.stem(range(5,17),masa,linefmt='red',use_line_collection=True)
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 2
#----------------------------------------------------------------------------------------------------------------------------------------

#Función que calcula la probabilidad
def value_prob():
    d={1:1/506}
    c=1/506
    for i in range(2,12):
        c+=i**2/506
        d[i]=c
    return d
    
#Definimos la probabilidad
prob=value_prob()

#Función que calcula la función de masa de probabilidad de la variable aleatoria
def masa_prob(x):
    base=range(1,12)
    
    if x in base:
        return x**2/506
    return 0

#Función que calcula la función probabilidad acumulada de la variable aleatoria
def acumm_prob(x):
    global prob
    for i,j in prob.items():
        if i+1>x>=i:
            return prob[i]
    if x>=15:
        return 1
    return 0

#Función que simula la variable aleatoria
def generator(x):
    for i in range(1,12):
        if acumm_prob(i)<x<=acumm_prob(i+1):
            return i+1
    return 1

#Graficación del histograma
data=[]
for i in range(10000):
    data.append(generator(random.random()))

plt.hist(data,density=True,alpha=0.5,rwidth=0.5,align='left',bins=range(1,13))
plt.show()

masa=[]
for i in range(0,13):
    masa.append(masa_prob(i))

plt.stem(range(0,13),masa,linefmt='red',use_line_collection=True)
plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 3
#----------------------------------------------------------------------------------------------------------------------------------------
#Definimos la probabilidad
prob=11/16

#Función que calcula la función de masa de probabilidad de la variable aleatoria
def masa_prob(x):
    global prob

    return ((1-prob)**x)*prob
    
#Función que calcula la función probabilidad acumulada de la variable aleatoria
def acumm_prob(x):
    global prob
    return 1-((1-prob)**(int(x)))

#Función que simula la variable aleatoria
def generator(x):
    for i in range(0,11):
        if acumm_prob(i)<x<=acumm_prob(i+1):
            return i
    return 1

#Graficación del histograma
data=[]
for i in range(10000):
    data.append(generator(random.random()))

plt.hist(data,density=True,alpha=0.5,rwidth=0.5,align='left',bins=range(0,13))
plt.show()

masa=[]
for i in range(0,10):
    masa.append(masa_prob(i))

plt.stem(range(0,10),masa,linefmt='red',use_line_collection=True)
plt.show()