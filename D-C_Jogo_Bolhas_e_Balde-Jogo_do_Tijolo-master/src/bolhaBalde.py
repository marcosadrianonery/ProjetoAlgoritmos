
# Desafio Uri: https://www.urionlinejudge.com.br/judge/pt/problems/view/1088
import random
import numpy as np
import utils

lista = [[1, 5, 3, 4, 2], [5, 1, 3, 4, 2], [1, 2, 3, 4, 5],[3, 5, 2, 1, 4, 6], [5, 4, 3, 2, 1] ,[6, 5, 4, 3, 2, 1]]
contSolList = []
nameList = []

for listaItem in lista:
    
    result, contSol = utils.bolhaBalde(listaItem)
    
    contSolList.append(contSol)
    print('-'*40)

    if (contSol%2) == 0:
        print("Carlos")
        nameList.append('Carlos')
    else:
        print("Marcelo")
        nameList.append('Marcelo')

    print('Resultado: ', result)


print('_'*40 + '\n')
print(contSolList)
print('Nomes: ', nameList)
print('_'*40)
