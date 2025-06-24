from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *

from meu_grafo_matriz_adj_dir import MeuGrafo

# Criar o grafo
g = MeuGrafo()

# Adicionar vértices
g.adiciona_vertice('A')
g.adiciona_vertice('B')
g.adiciona_vertice('C')
g.adiciona_vertice('D')

# Adicionar arestas
g.adiciona_aresta('a1', 'A', 'B')
g.adiciona_aresta('a2', 'B', 'C')
g.adiciona_aresta('a3', 'C', 'D')

# Calcular a matriz de alcançabilidade
alc = g.warshall()

# Mostrar a matriz
print("Matriz de Alcançabilidade (Warshall):")
rotulos = [v.rotulo for v in g.vertices]
print("   ", "  ".join(rotulos))
for i in range(len(alc)):
    linha = "  ".join(str(x) for x in alc[i])
    print(f"{rotulos[i]}  {linha}")
