#IMPORTANDO AS BIBLIOTECAS

from pylab import plot,xlabel,ylabel,show,legend
from random import random
from numpy import arange

#DEFINIR CONSTANTES E PARÂMETROS 

NTl = 1000            #número de átomos de tálio 208
NPb = 0               #número de átomos de chumbo 208
tau = 3.053*60        #tempo de meia-vida do tálio 208 em segundos
h = 1.0               #passo de tempo (segundos)
p = 1 - 2**(-h/tau)   #probabilidade
tmax = 2000           #tempo total de simulação

#CRIANDO AS LISTAS

tpoints = arange(0,tmax,h)
Tl = []
Pb = []

#CRIANDO O LOOP

for t in tpoints:
    Tl.append(NTl)
    Pb.append(NPb)

    #cálculo dos átomos que decaem
    decay = 0
    for i in range(NTl):
        if random()<p:
            decay += 1
    NTl -= decay
    NPb += decay

#GERANDO O GRÁFICO 

plot(tpoints,Tl)
plot(tpoints,Pb)
legend(["Átomos de Tálio","Átomos de Chumbo"])
xlabel("Tempo")
ylabel("Número de átomos")
show()