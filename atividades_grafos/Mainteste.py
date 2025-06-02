from grafo_de_teste import grafo_paraiba
from bibgrafo.grafo_lista_adj_dir import GrafoListaAdjacenciaDirecionado
from bibgrafo.grafo_errors import *
from meu_grafo_lista_adj_dir import *

g = grafo_paraiba()

print("DFS a partir de J:")
arvore_dfs = g.dfs('J')
for a in arvore_dfs.arestas.values():
    print(f"{a.rotulo}({a.v1.rotulo}-{a.v2.rotulo})")



print("\nBFS a partir de J:")
arvore_bfs = g.bfs('J')
for a in arvore_bfs.arestas.values():
    print(f"{a.rotulo}({a.v1.rotulo}-{a.v2.rotulo})")