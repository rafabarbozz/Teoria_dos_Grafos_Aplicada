from func_ler_grafo import ler_grafo
from algoritmos import Krager


lista_adj, lista_aresta = ler_grafo('Trabalho3/in/graph_1')

algoritmo = Krager(lista_adj, lista_aresta)
print(algoritmo.run())