# Arquivo com as funções que dizem respeito ao grafo

# Classe no que será utilizada no algoritmo de busca em profundidade
class No_profundidade:
    def __init__(self, vertice):
        self.vertice = vertice 
        self.PE = 0 # profundidade de entrada do vertice
        self.PS = 0 # profundidade de saida do vertice
        self.pai = None # ponteiro que define a arvore de profundidade


# Classe no que será utilizada no algoritmo de busca em largura
class No_largura:
    def __init__(self, vertice):
        self.vertice = vertice
        self.pai = None
        self.nivel = 0
        self.L = 0
        


# Classe tempo que diz em qual ordem vai ser feita a busca
class Tempo_Global:
    def __init__(self):
        self.r = 0
    
    def adicionar(self, vertice):
        self.r += vertice