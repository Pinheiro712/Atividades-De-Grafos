import unittest
from meu_grafo_lista_adj_dir import MeuGrafo


class TestRoteiro3(unittest.TestCase):

    def setUp(self):
        # Grafo 1: Árvore simples
        self.arvore = MeuGrafo()
        for v in ['A', 'B', 'C', 'D']:
            self.arvore.adiciona_vertice(v)
        self.arvore.adiciona_aresta('a1', 'A', 'B')
        self.arvore.adiciona_aresta('a2', 'A', 'C')
        self.arvore.adiciona_aresta('a3', 'C', 'D')

        # Grafo 2: Com ciclo
        self.com_ciclo = MeuGrafo()
        for v in ['A', 'B', 'C']:
            self.com_ciclo.adiciona_vertice(v)
        self.com_ciclo.adiciona_aresta('a1', 'A', 'B')
        self.com_ciclo.adiciona_aresta('a2', 'B', 'C')
        self.com_ciclo.adiciona_aresta('a3', 'C', 'A')

        # Grafo 3: Bipartido
        self.bipartido = MeuGrafo()
        for v in ['X', 'Y', 'Z', 'W']:
            self.bipartido.adiciona_vertice(v)
        self.bipartido.adiciona_aresta('a1', 'X', 'Y')
        self.bipartido.adiciona_aresta('a2', 'X', 'Z')
        self.bipartido.adiciona_aresta('a3', 'W', 'Y')
        self.bipartido.adiciona_aresta('a4', 'W', 'Z')

        # Grafo 4: Não bipartido
        self.nao_bipartido = MeuGrafo()
        for v in ['A', 'B', 'C']:
            self.nao_bipartido.adiciona_vertice(v)
        self.nao_bipartido.adiciona_aresta('a1', 'A', 'B')
        self.nao_bipartido.adiciona_aresta('a2', 'B', 'C')
        self.nao_bipartido.adiciona_aresta('a3', 'C', 'A')

    def test_ha_ciclo(self):
        self.assertFalse(self.arvore.ha_ciclo())
        self.assertTrue(self.com_ciclo.ha_ciclo())
        self.assertFalse(self.bipartido.ha_ciclo())
        self.assertTrue(self.nao_bipartido.ha_ciclo())

    def test_eh_arvore(self):
        self.assertEqual(self.arvore.eh_arvore(), ['B', 'D'])
        self.assertFalse(self.com_ciclo.eh_arvore())
        self.assertFalse(self.bipartido.eh_arvore())
        self.assertFalse(self.nao_bipartido.eh_arvore())

    def test_eh_bipartido(self):
        self.assertTrue(self.bipartido.eh_bipartido())
        self.assertFalse(self.nao_bipartido.eh_bipartido())
        self.assertTrue(self.arvore.eh_bipartido())
        self.assertFalse(self.com_ciclo.eh_bipartido())


if __name__ == '__main__':
    unittest.main()
