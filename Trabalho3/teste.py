from func_ler_grafo import ler_grafo
from algoritmos import Karger
import sys
from tqdm import tqdm
sys.path.insert(0, '..')


nome_arquivo = 'graph_type2_3'
lista_adj, lista_aresta = ler_grafo(f'./instancias/in/{nome_arquivo}')

algoritmo = Karger(lista_adj, lista_aresta)

n_exec = 100
n_iter = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

probabilidades_karger = []
min_corte_correto = int(open(f"./Instancias/out/{nome_arquivo}", 'r').readlines()[0])

for i in tqdm(range(len(n_iter))):
    it = n_iter[i]
    
    n_acertos_karger = 0
    
    
    for _ in tqdm(range(n_exec)):
        min_cut_karger = algoritmo.executar_n(it)
        
        if min_cut_karger == min_corte_correto:
            n_acertos_karger += 1
        

    probabilidades_karger.append(n_acertos_karger / n_exec)


print(probabilidades_karger)