from random import sample, seed, randint
        
class Karger:
    def __init__(self, matriz_adj: list, lista_aresta: list):
        ''''
        matriz_adj(list): é a lista de adjacência do grafo
        Lista_aresta(list): é uma lista de tuplas que informa quais arestas estão presentes no grafo
        '''
        self.matriz_adj = matriz_adj
        self.lista_aresta = lista_aresta

    
    def run(self):
        lista_aresta_copy = self.lista_aresta.copy() # criando uma cópia
        matriz_adj_modificada = [adj_lista.copy() for adj_lista in self.matriz_adj]  # Criando uma cópia profunda da lista de adjacência
        lista_vertices = [vertice for vertice in range(1, len(self.matriz_adj) + 1)]

        while len(lista_vertices) > 2: # Se só restarem 2 vértices não vazios finaliza o loop
            aresta_escolhida = lista_aresta_copy[randint(0, len(lista_aresta_copy) - 1)] # Escolhendo uma aresta aleatoriamente
                
            lista_vertices.remove(aresta_escolhida[1]) # Removendo o segundo vértice da lista de vértices
            
            # Zerando a ligação entre a aresta_escolhida[0] e aresta_escolhida[1]
            matriz_adj_modificada[aresta_escolhida[1] - 1][aresta_escolhida[0] - 1] = 0
            matriz_adj_modificada[aresta_escolhida[0] - 1][aresta_escolhida[1] - 1] = 0
            
            # Adicionando arestas novas
            for n, elemento in enumerate(matriz_adj_modificada[aresta_escolhida[1] - 1]):
                if elemento != 0:
                    for _ in range(elemento):
                        lista_aresta_copy.append((aresta_escolhida[0], n + 1))
            
            
            for n, elemento in enumerate(matriz_adj_modificada[aresta_escolhida[1] - 1]):
                # Somando todos os elementos da linha aresta_escolhida[1] na aresta_escolhida[0]
                matriz_adj_modificada[aresta_escolhida[0] - 1][n] += elemento
                matriz_adj_modificada[aresta_escolhida[1] - 1][n] = 0
                
                matriz_adj_modificada[n][aresta_escolhida[0] - 1] += elemento
                matriz_adj_modificada[n][aresta_escolhida[1] - 1] = 0
            
            # Tirando a ligação de todos os vértices ao vértice aresta_escolhida[1]
            for linha in matriz_adj_modificada:
                linha[aresta_escolhida[1] - 1] = 0
        
            # Retirando todas as aresta que possuem o aresta_escolhida[1] dentro     
            lista_aresta_copy = [aresta for aresta in lista_aresta_copy if aresta_escolhida[1] not in aresta]
            
        return len(lista_aresta_copy)
    

    def executar_n(self, n):
        corte_minimo = float('inf')
        
        for _ in range(n):
            qtd_corte = (self.run())
            
            if qtd_corte < corte_minimo:
                corte_minimo = qtd_corte
        
        return corte_minimo
    




class Ingenuo:
    def __init__(self, matriz_adj: list, lista_aresta: list):
        ''''
        matriz_adj(list): é a lista de adjacência do grafo
        Lista_aresta(list): é uma lista de tuplas que informa quais arestas estão presentes no grafo
        '''
        self.matriz_adj = matriz_adj
        self.lista_aresta = lista_aresta
    
    def run(self):
        # Criando o corte
        vertices = [i for i in range(1, len(self.matriz_adj) + 1)]
        
        grupo_A = []
        for _ in range(len(self.matriz_adj)):
            num_aleatorio = randint(1, len(self.matriz_adj))
            
            if num_aleatorio not in grupo_A:
                grupo_A.append(num_aleatorio)
                
        grupo_B = [vertice for vertice in vertices if vertice not in grupo_A]
        
        # Criando a duas listas de arestas
        arestas_A = []
        for vertice in grupo_A:    
            for elemento in self.matriz_adj[vertice - 1]:
                arestas_A.append((vertice, elemento))

        arestas_B = []
        for vertice in grupo_B:    
            for elemento in self.matriz_adj[vertice - 1]:
                arestas_B.append((vertice, elemento))
                
        contador_arestas = 0
        for aresta in arestas_A:
            aresta_invertida = (aresta[1], aresta[0])  # Inverte a aresta
            if aresta_invertida in arestas_B:
                contador_arestas += 1
                
        return contador_arestas
    
    
    def executar_n(self, n):
        corte_minimo = float('inf')
        for _ in range(n):
            qtd_corte = (self.run())
            
            if qtd_corte < corte_minimo:
                corte_minimo = qtd_corte
        
        return corte_minimo