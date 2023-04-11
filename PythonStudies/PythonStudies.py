import numpy as np
import itertools
from itertools import permutations

valorinicial = 13000.00
valorterminal = 0.00
listavalores = []
listavalorescomparativos = []
listavaloresfinais = []

while(valorinicial > 0):
    listavalores.append(valorinicial)
    print(f"{valorinicial:.2f}")
    valorinicial -= 0.01

#listavalores = map(lambda x:x - 0.01,valorinicial)

listavalorescomparativos = listavalores
listavalorescomparativos.reverse()


permut = itertools.permutations(listavalores, len(listavalorescomparativos))
for comb in permut:
    zipped = zip(comb, listavalorescomparativos)
    if(list(zipped) == 13000):
        listavaloresfinais.append(list(zipped))

print("\033[H\033[J", end="")

#for valor in listavalores:
#    for val in listavalorescomparativos:
#        print(f"Comparing {valor:.2f} with {val:.2f}")
#        if valor + val == 13000:
#            listavaloresfinais.update(valor1 = valor, valor2 = val)

print(listavaloresfinais)