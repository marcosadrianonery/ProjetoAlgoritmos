
"""
Created on September 2020

@author: Marcos Adriano, Moacir Mascarenha

"""

def buscas(grafo, velueSpecific, raiz: '1', busca):
    grafoTemp = {}
    grafoTemp = grafo.copy()
    visitados, queue_ = {}, {}
    queue = {}
    queue[raiz] = grafoTemp[raiz]
    while queue:
        if busca == 'profundidade':
            #   ------------------------------------------------------------
            #   PEGA O NÓ A DEPENDER DA BUSCA
            #   ------------------------------------------------------------
            vertice = queue.popitem()
        else:
            queue_ = list(queue)[0]
            vertice = (queue_,queue.pop(queue_))
        if vertice[0] == velueSpecific:
            visitados[vertice[0]] = set()
            printVisitados(visitados)
            return False

        if vertice[0] not in visitados:
            visitados[vertice[0]] = set()
            for atual in vertice[1]:
                if atual not in visitados:
                    queue[atual] = grafoTemp[atual]
                    #print("visitados", visitados)
    return True

#   ------------------------------------------------------------
#   ESTA FUNÇÃO IMPRIME QUAIS NÓS FORAM VISITADOS
#   ------------------------------------------------------------
def printVisitados(visitados):
    print('\n\n')
    print("    ", '-----')
    print("   ", '| Raiz |')
    for x, y in visitados.items():
        print("    ", '-----')
        print(" --> |", x,'|')
        print("    ", '-----')
        if x != list(visitados.items())[-1][0]:
            print("      ", '|')
            print("      ", 'V')

