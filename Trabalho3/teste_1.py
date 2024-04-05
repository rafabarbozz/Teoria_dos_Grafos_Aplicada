from func_ler_grafo import ler_grafo
from algoritmos import Karger
import sys
sys.path.insert(0, '..')


nome_arquivo = 'graph_type2_3'
lista_adj, lista_aresta = ler_grafo(f'./instancias/in/{nome_arquivo}')

algoritmo = Karger(lista_adj, lista_aresta)
algoritmo.run()
