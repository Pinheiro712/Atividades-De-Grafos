from bibgrafo.grafo_lista_adj_dir import GrafoListaAdjacenciaDirecionado
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):

        nao_adjacentes = set()

        vertices = self.vertices

        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                v1 = vertices[i].rotulo
                v2 = vertices[j].rotulo

                adjacente = False
                for aresta in self.arestas.values():
                    if (aresta.v1.rotulo == v1 and aresta.v2.rotulo == v2) or (
                            aresta.v1.rotulo == v2 and aresta.v2.rotulo == v1):
                        adjacente = True
                        break

                if not adjacente:
                    nao_adjacentes.add(f"{v1}-{v2}")

        return nao_adjacentes





    def ha_laco(self):
        return any(aresta.v1.rotulo == aresta.v2.rotulo for aresta in self.arestas.values())





    def grau_entrada(self, V=''):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(V)
        return sum(1 for aresta in self.arestas.values() if aresta.v2.rotulo == V)

    def grau_saida(self, V=''):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(V)
        return sum(1 for aresta in self.arestas.values() if aresta.v1.rotulo == V)

    def ha_paralelas(self):
        vistos = {}
        for aresta in self.arestas.values():
            chave = (aresta.v1.rotulo, aresta.v2.rotulo)
            if chave in vistos:
                return True
            vistos[chave] = True
        return False






    def arestas_sobre_vertice(self, V):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(V)
        return {
            rot for rot, aresta in self.arestas.items()
            if aresta.v1.rotulo == V or aresta.v2.rotulo == V
        }







    def eh_completo(self):
        if self.ha_laco() or self.ha_paralelas():
            return False

        n = len(self.vertices)
        return len(self.arestas) == n * (n - 1) // 2









    def dfs(self, V=''):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(V)

        visitados = []
        pilha = [V]
        arvore_dfs = MeuGrafo()
        arvore_dfs.adiciona_vertice(V)

        while pilha:
            atual = pilha.pop()
            if atual not in visitados:
                visitados.append(atual)
                for aresta in sorted(self.arestas_sobre_vertice(atual)):
                    a = self.arestas[aresta]
                    vizinho = a.v2.rotulo if a.v1.rotulo == atual else a.v1.rotulo

                    if vizinho not in visitados:
                        if not arvore_dfs.existe_rotulo_vertice(vizinho):
                            arvore_dfs.adiciona_vertice(vizinho)
                        arvore_dfs.adiciona_aresta(aresta, atual, vizinho)
                        pilha.append(vizinho)

        return arvore_dfs












    def bfs(self, V=''):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(V)

        visitados = []
        fila = [V]
        arvore_bfs = MeuGrafo()
        arvore_bfs.adiciona_vertice(V)

        while fila:
            atual = fila.pop(0)
            if atual not in visitados:
                visitados.append(atual)
                for aresta in sorted(self.arestas_sobre_vertice(atual)):
                    a = self.arestas[aresta]
                    vizinho = a.v2.rotulo if a.v1.rotulo == atual else a.v1.rotulo

                    if vizinho not in visitados and vizinho not in fila:
                        if not arvore_bfs.existe_rotulo_vertice(vizinho):
                            arvore_bfs.adiciona_vertice(vizinho)
                        arvore_bfs.adiciona_aresta(aresta, atual, vizinho)
                        fila.append(vizinho)

        return arvore_bfs




  