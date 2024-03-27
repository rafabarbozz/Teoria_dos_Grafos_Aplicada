import sys
sys.path.insert(0, 'Trabalho2')
from grafo import No_largura, Tempo_Global

class Busca_largura():
    def __init__(self, lista_adj: list ):
        self.lista_adj = lista_adj
        self.nos = [No_largura(i) for i in range(len(self.lista_adj))] # Nos do grafo
        self.relogio = Tempo_Global() # tempo global
        self.matriz_cores = [[None] * len(self.lista_adj) for _ in range(len(self.lista_adj))] # cor que cada aresta vai receber
    
    
    def run(self, vertice: int):
        self.nos = [No_largura(i) for i in range(len(self.lista_adj))] # Nos do grafo
        self.relogio = Tempo_Global() # tempo globa
        self.matriz_cores = [[None] * len(self.lista_adj) for _ in range(len(self.lista_adj))] # cor que cada aresta vai receber
        
        F = [vertice]
        
        for no in self.nos:
            if no.vertice == vertice:
                self.relogio.r += 1
                no.L = self.relogio.r

        while (len(F) > 0):    
            v = F.pop(0)
            
            for w in self.lista_adj[v]:
                if self.nos[w].L == 0:
                    self.matriz_cores[v][w] = "0,0,255" # azul - pai
                    self.matriz_cores[w][v] = "0,0,255" # azul - pai

                    self.nos[w].pai = v
                    self.nos[w].nivel = self.nos[v].nivel + 1
                    self.relogio.r += 1
                    self.nos[w].L = self.relogio.r
                    F.append(w)
                     

                elif self.nos[w].nivel == self.nos[v].nivel:
                    if self.nos[w].pai == self.nos[v].pai:
                        self.matriz_cores[v][w] = "255,0,0" # vermelho - irmao
                        self.matriz_cores[w][v] = "255,0,0" # vermelho - irmao
                    else:
                        self.matriz_cores[v][w] = "255,255,0" # amarelo - primo
                        self.matriz_cores[w][v] = "255,255,0" # amarelo - primo

                elif self.nos[w].nivel == self.nos[v].nivel + 1: 
                    self.matriz_cores[v][w] = "0,255,0" # verde - tio
                    self.matriz_cores[w][v] = "0,255,0"  # verde - tio
                
                
    def calc_exentricidade(self):
        valores = [] # vai receber todas as máximas das excentricidades de cada busca em largura para todo os vertices do grafo
        for i in range(len(self.lista_adj)):
            self.run(i) # rodando a busca em largura para todos os vertice
            nivel_max = float('-inf')
            
            for no in self.nos: # percorrendo todos os niveis do grafo resultante do ponto inicial i
                if nivel_max < no.nivel: 
                    nivel_max = no.nivel
            
            valores.append(nivel_max)

        return min(valores), max(valores) # O valor mínimo é o raio e o valor máximo é o diâmetro 
    
    
    def calc_media(self):
        distancias = [[None] * len(self.lista_adj) for _ in range(len(self.lista_adj))]
        
        for c in range(len(self.lista_adj)):
            self.run(c)
            for k in range(len(self.nos)):
                distancias[c][k] = self.nos[k].nivel
        
        total = 0
        contador = 0
        for i in range(len(self.lista_adj)):
            for j in range(i + 1, len(self.lista_adj)): # pegando a parte triangular superior da matriz, pois são grafos não direcionais
                total += distancias[i][j]
                contador += 1
        
        return total / contador