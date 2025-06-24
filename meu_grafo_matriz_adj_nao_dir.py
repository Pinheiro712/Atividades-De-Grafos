from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        verticenao = set()
        for i in range(len(self.matriz)):
            for j in range(i + 1, len(self.matriz)):
                if len(self.matriz[i][j]) == 0:
                    verticenao.add(f"{self.vertices[i].rotulo}-{self.vertices[j].rotulo}")
        return verticenao

    def ha_laco(self):
        for i in range(len(self.matriz)):
            if len(self.matriz[i][i]) > 0:
                return True
        return False


    def grau(self, V=''):

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        indice = self.indice_do_vertice(self.get_vertice(V))
        grau = 0

        for j in range(len(self.matriz)):
            if j == indice:
                grau += len(self.matriz[indice][j]) * 2


            else:
                grau += len(self.matriz[indice][j])
        return grau

    def ha_paralelas(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if len(self.matriz[i][j]) > 1:
                    return True
        return False



    def arestas_sobre_vertice(self, V):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        indice = self.indice_do_vertice(self.get_vertice(V))
        arestas = set()

        for i in range(len(self.matriz)):
            # Arestas onde V é origem
            for aresta in self.matriz[indice][i]:
                arestas.add(aresta)
            # Arestas onde V é destino
            for aresta in self.matriz[i][indice]:
                arestas.add(aresta)

        return arestas

    def warshall(self):
        n = len(self.vertices)
        matriz_alc = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if len(self.matriz[i][j]) > 0:
                    matriz_alc[i][j] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matriz_alc[i][j] == 0 and (matriz_alc[i][k] and matriz_alc[k][j]):
                        matriz_alc[i][j] = 1

        return matriz_alc