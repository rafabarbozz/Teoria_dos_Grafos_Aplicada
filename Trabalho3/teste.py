from func_ler_grafo import ler_grafo
from algoritmos import Karger
from tqdm import tqdm
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '..')

lista_adj, lista_aresta = ler_grafo('./instancias/in/graph_type1_1.txt')
algoritmo_1 = Karger(lista_adj, lista_aresta)
qtd_minimo, lista_adj_modificada = (algoritmo_1.run())
algoritmo_1.criar_out('./instancias/out_algoritmo/graph_type1_1.txt')