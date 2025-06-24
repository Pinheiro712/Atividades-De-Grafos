import unittest
from meu_grafo_lista_adj_dir import *
from bibgrafo.aresta import ArestaDirecionada
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder


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