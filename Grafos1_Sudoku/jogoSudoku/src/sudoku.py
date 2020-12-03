
"""
Created on September 2020

@author: Marcos Adriano, Moacir Mascarenha

"""

import sys
import os
import numpy as np

#   ------------------------------------------------------------
#   VOLTA O DIRETORIO
#   ------------------------------------------------------------
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import src.functios_sudoku  as funcSud

#   ------------------------------------------------------------
#   ESTA FUNÇÃO APENAS RETORNA QUAL POSIÇÃO NO SUDOKU ESTÁ VAZIA
#   ------------------------------------------------------------

def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

#   ------------------------------------------------------------
#   ESTA FUNÇÃO SE OCUPA COM A RESOLUÇÃO DO SUDOKU
#   SENDO RESPONSABILIDADE DELA INSPECIONAR AS COLUNAS
#   E CADA BOX. NA CHAMADA DO BOX OCORRE A CHAMADA DAS BUSCAS
#   ------------------------------------------------------------
def resolve(grid, i=0, j=0, busca = 'largura'):
    printa = 0
    if printa == 1:
        if i == 0 and j==0:
            printsudoku(grid)
        print("Init ==> I:", i, " - - J:", j)
        printsudoku(grid)
    i, j = findNextCellToFill(grid, i, j)
    if printa == 1:
        print("Find ==> I:", i, " - - J:", j)
        printsudoku(grid)
    if i == -1:
        return True, grid
    for e in range(1, 10):
        #   ------------------------------------------------------------
        #   inspeciona a linha e coluna referente a posiçao que está
        #   ------------------------------------------------------------
        if funcSud.inspecionaLinCol(grid, i, j, e):
            #   ------------------------------------------------------------
            #   inspeciona o BOX referente a posiçao que está alem de
            #   definir qual busca será usado para tal
            #   ------------------------------------------------------------
            if funcSud.inspecionaBox(grid, i, j, e, busca):
                grid[i][j] = e
                if resolve(grid, i, j):
                    if len(grid) - 1 == i:
                        print(j)
                    return True, grid
                grid[i][j] = 0
    return False

#   ------------------------------------------------------------
#   ESTA FUNÇÃO IMPRIME O SUDOKU
#   ------------------------------------------------------------
def printsudoku(sudoku):
    print("                    " + "-------------------------")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("                    " + " ----------------------- ")
        for j in range(len(sudoku[i])):
            if j == 0 or j == 3 or j == 6:
                if j == 0:
                    line += "                    "
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line + "|")
    print("                    " + "-------------------------")
