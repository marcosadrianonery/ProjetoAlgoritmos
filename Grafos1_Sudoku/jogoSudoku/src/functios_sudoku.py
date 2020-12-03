
"""
Created on September 2020

@author: Marcos Adriano, Moacir Mascarenha

"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import src.functionsBusca  as buscas

def inspecionaLinCol(matrix, i, j, alg):
    if all(alg != matrix[i][x] for x in range(9)):
        return all(alg != matrix[x][j] for x in range(9))

def inspecionaBox(matrix, x, y, alg, busca):
    OrigX, OrigY = (x // 3 * 3, y // 3 * 3)
    grafoMont = montGrafo(matrix[OrigX:OrigX + 3, OrigY: OrigY + 3])
    for x in range(OrigX, OrigX + 3):
        for y in range(OrigY, OrigY + 3):
            return buscas.buscas(grafoMont,str(alg), str(matrix[OrigX, OrigY]), busca)
    return True

def adicionar_aresta(G, vertice1, vertice2):
    G[vertice1].add(vertice2)
    G[vertice2].add(vertice1)

def montGrafo (matrixBox):
    Grafo = {}
    Grafo.clear()
    for x in range(0,3):
        for y in range(0,3):
            Grafo[str(matrixBox[x][y])] = set()
    for x in range(1,9):
        if x == 1:
            adicionar_aresta(Grafo, str(matrixBox[0][0]), str(matrixBox[0][1]))
            adicionar_aresta(Grafo, str(matrixBox[0][0]), str(matrixBox[1][0]))
            adicionar_aresta(Grafo, str(matrixBox[0][0]), str(matrixBox[1][1]))
        if x == 2:
            adicionar_aresta(Grafo, str(matrixBox[0][1]), str(matrixBox[0][2]))
        if x == 4:
            adicionar_aresta(Grafo, str(matrixBox[1][0]), str(matrixBox[2][0]))
        if x == 5:
            adicionar_aresta(Grafo, str(matrixBox[1][1]), str(matrixBox[1][2]))
            adicionar_aresta(Grafo, str(matrixBox[1][1]), str(matrixBox[2][1]))
            adicionar_aresta(Grafo, str(matrixBox[1][1]), str(matrixBox[2][2]))
    return Grafo