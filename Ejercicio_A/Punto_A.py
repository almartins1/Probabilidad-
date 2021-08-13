import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
import random

#Punto A
#----------------------------------------------------------------------------------------------------------------------------------------
# Graficando Uniforme                                
x = np.random.uniform(0,1,10000)                                  #genera 10000 simulaciones de variables aleatorias uniformes
fp = stats.uniform().pdf(x)                                       # Función de Probabilidad de una uniforme aplicada a x
fig, ax = plt.subplots()   
data=[]
for i in range(10000):
    data.append(random.random())                                  #agrega los numeros aleatorios generados a un arreglo 
 

plt.hist(data,density=True,alpha=0.5, histtype='bar', ec='black') #plot histograma de numeros aleatorios generados por random.random 
ax.plot(x, fp, linewidth=2,color='red')                           #plot distribucion teorica de la uniforme
plt.title('Distribución números aleatorios-uniforme')
plt.ylabel('probabilidad')
plt.xlabel('valores')

plt.show()
