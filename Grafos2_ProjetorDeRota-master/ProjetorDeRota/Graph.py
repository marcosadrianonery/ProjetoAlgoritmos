import math

class Grafo(object):

    def __init__(self, grafo={}):
        self.grafo = grafo

    def vertices(self):
        return list(self.grafo.keys())

    def arestas(self):
        return self.gera_arestas()

    def adiciona_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adiciona_arestas(self, *aresta, bidirecional=True):
        (v1, v2, custo) = aresta
        self.adiciona_vertice(v1)
        self.adiciona_vertice(v2)
        self.adiciona_aresta_sem_representacao(v1, v2, custo)
        if bidirecional:
            self.adiciona_aresta_sem_representacao(v2, v1, custo)

    def custo(self, v1, v2):
        list_v1 = self.grafo[v1]
        for (v, custo) in list_v1:
            if v == v2:
                return custo
        else:
            return math.inf

    def adiciona_aresta_sem_representacao(self, v1, v2, custo):
        list_v1 = self.grafo[v1]
        for i, (v, _) in enumerate(list_v1):
            if v == v2:
                list_v1[i] = (v2, custo)
                break
        else:
            list_v1.append((v2, custo))

    def gera_arestas(self):
        arestas = []
        for vertice in self.grafo:
            for (neighbour, custo) in self.grafo[vertice]:
                if (neighbour, vertice) not in arestas:
                    arestas.append((vertice, neighbour, custo))
        return arestas

    def __str__(self):
        return 'Vertices: {0}\nEdges: {1}'.format(sorted(self.vertices()), sorted(self.arestas()))

