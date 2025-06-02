from grafo_lista_adj_dir_test import MeuGrafo

def grafo_paraiba():
    g = MeuGrafo()
    for v in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
        g.adiciona_vertice(v)

    g.adiciona_aresta('a1', 'J', 'C')
    g.adiciona_aresta('a2', 'C', 'E')
    g.adiciona_aresta('a3', 'C', 'E')  # aresta paralela
    g.adiciona_aresta('a4', 'C', 'P')
    g.adiciona_aresta('a5', 'C', 'M')
    g.adiciona_aresta('a6', 'C', 'T')
    g.adiciona_aresta('a7', 'M', 'T')
    g.adiciona_aresta('a8', 'M', 'T')  # aresta paralela
    g.adiciona_aresta('a9', 'T', 'Z')
    return g
