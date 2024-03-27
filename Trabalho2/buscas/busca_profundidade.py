import sys
sys.path.insert(0, 'Trabalho2')
from grafo import No_profundidade, Tempo_Global
 

class Busca_profundidade():
    def __init__(self, lista_adj: list):
        self.lista_adj = lista_adj
        self.nos = [No_profundidade(i) for i in range(len(self.lista_adj))] # Nos do grafo
        self.relogio = Tempo_Global() # tempo global
        self.matriz_cores = [[None] * len(self.lista_adj) for _ in range(len(self.lista_adj))] # cor que cada aresta vai receber
    
    def run(self, vertice: int):
        self.relogio.r += 1
        self.nos[vertice].PE = self.relogio.r

        for w in self.lista_adj[vertice]: # Considerando o vertice começando de 0
            if self.nos[w].PE == 0:
                self.matriz_cores[vertice][w] = "0,0,255" # azul para aresta da árvore de profundidade
                self.matriz_cores[w][vertice] = "0,0,255" # azul para aresta da árvore de profundidade
                    
                self.nos[w].pai = vertice
                self.run(w)
                
            elif self.nos[w].PS == 0 and w != self.nos[vertice].pai:
                self.matriz_cores[vertice][w] = "255,0,0" # vermelho para aresta de retorno
                self.matriz_cores[w][vertice] = "255,0,0" # vermelho para aresta de retorno
                    
        self.relogio.r += 1
        self.nos[vertice].PS = self.relogio.r
