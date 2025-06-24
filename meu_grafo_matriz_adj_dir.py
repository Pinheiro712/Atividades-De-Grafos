from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        nao_adjacentes = []
        for i, v1 in enumerate(self.N):
            for j, v2 in enumerate(self.N):
                if i != j:
                    arestas = self.M[i][j]
                    if len(arestas) == 0:
                        nao_adjacentes.append(f"{v1}-{v2}")
        return nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau_entrada(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

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