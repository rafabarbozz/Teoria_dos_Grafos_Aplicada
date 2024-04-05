from random import sample, seed, randint
        
class Karger:
    def __init__(self, lista_adj: list, lista_aresta: list):
        ''''
        Lista_adj(list): é a lista de adjacência do grafo
        Lista_aresta(list): é uma lista de tuplas que informa quais arestas estão presentes no grafo
        '''
        self.lista_adj = lista_adj
        self.lista_aresta = lista_aresta

    
    def run(self):
        lista_aresta_copy = self.lista_aresta.copy() # criando uma cópia
        lista_adj_modificada = [adj_lista.copy() for adj_lista in self.lista_adj]  # Criando uma cópia profunda da lista de adjacência
        lista_vertices = [vertice for vertice in range(1, len(self.lista_adj) + 1)]

        while len(lista_vertices) > 2: # Se só restarem 2 vértices não vazios finaliza o loop
            #seed(8)
            aresta_escolhida = lista_aresta_copy[randint(0, len(lista_aresta_copy) - 1)] # Escolhendo uma aresta aleatoriamente
            #print(f'Aresta escolhida: {aresta_escolhida}')
            #print(f'Lista vertices antes: {lista_vertices}')
            lista_vertices.remove(aresta_escolhida[1]) # removendo o vértice que se refere ao segundo elemento da aresta escolhida
            #print(f'Lista aresta antes: {sorted(lista_aresta_copy, key=lambda x: (x[0], x[1]))}')
            #print(f'Lista adj antes: {lista_adj_modificada}\n')
            
        
        
            for i in range(len(lista_adj_modificada)):
                if aresta_escolhida[1] in lista_adj_modificada[i]: # Retirando todos os vertices ligados ao vertice retirado(aresta_escolhida[1])
                    if i+1 != aresta_escolhida[0]: # Se a lista do vertice for diferente da aresta_escolhida[0], colocando na lista o vértice (aresta_escolhida[0])
                        lista_adj_modificada[i].append(aresta_escolhida[0])
                    
                    if i+1 == aresta_escolhida[0]: # Adicionando na lista do aresta_escolhida[0] a lista_adj_modificada do aresta_escolhida[1]
                        for elemento in lista_adj_modificada[aresta_escolhida[1] - 1]:
                            if elemento != aresta_escolhida[0]:
                                lista_adj_modificada[i].append(elemento)
                        
                    
                    lista_adj_modificada[i] = [valor for valor in lista_adj_modificada[i] if valor != aresta_escolhida[1]]  # removendo todos os aresta_escolhida[1] de todas a sublistas de lista_adj_modificada
            
            
            for elemento in (lista_adj_modificada[aresta_escolhida[1] - 1]):
                # Adicionando na lista_adj_modificada do primeiro elemento todos os vertices do segundo elemento tirando ele mesmo
                if elemento not in lista_adj_modificada[aresta_escolhida[0] - 1] and elemento != aresta_escolhida[0]:
                    lista_adj_modificada[aresta_escolhida[0] - 1].append(elemento)
                
                # Adicionando na lista de aresta todas as arestas do segundo elemento para o primeiro
                if elemento != aresta_escolhida[0]:
                    if elemento > aresta_escolhida[0]:
                        lista_aresta_copy.append((aresta_escolhida[0], elemento))
                    else:
                        lista_aresta_copy.append((elemento, aresta_escolhida[0]))
                        
                        
                        
            # Esvaziando lista adj na posição do segundo elemento da aresta escolhida
            lista_adj_modificada[aresta_escolhida[1] - 1].clear()     
                  
            # Loop usado para retirar as arestas que o segundo elemento da aresta escolhida possui na lista de arestas, 
            # se usar o remove pode dar problema com elementos sendo pulados
            lista_aresta_copy = [aresta for aresta in lista_aresta_copy if aresta_escolhida[1] not in aresta]

                    
            
            #print(f'Lista vertices depois: {lista_vertices}')
            #print(f'Lista aresta depois: {sorted(lista_aresta_copy, key=lambda x: (x[0], x[1]))}')
            #print(f'Lista adj depois: {lista_adj_modificada}')
            #print('\n')
        
        #print(len(lista_aresta_copy))
            
        return len(lista_aresta_copy)
    

    def executar_n(self, n):
        corte_minimo = float('inf')
        
        for _ in range(n):
            qtd_corte = (self.run())
            
            if qtd_corte < corte_minimo:
                corte_minimo = qtd_corte
        
        return corte_minimo
    




class Ingenuo:
    def __init__(self, lista_adj: list, lista_aresta: list):
        ''''
        Lista_adj(list): é a lista de adjacência do grafo
        Lista_aresta(list): é uma lista de tuplas que informa quais arestas estão presentes no grafo
        '''
        self.lista_adj = lista_adj
        self.lista_aresta = lista_aresta
    
    def run(self):
        # Criando o corte
        vertices = [i for i in range(1, len(self.lista_adj) + 1)]
        
        grupo_A = []
        for _ in range(len(self.lista_adj)):
            num_aleatorio = randint(1, len(self.lista_adj))
            
            if num_aleatorio not in grupo_A:
                grupo_A.append(num_aleatorio)
                
        grupo_B = [vertice for vertice in vertices if vertice not in grupo_A]
        
        # Criando a duas listas de arestas
        arestas_A = []
        for vertice in grupo_A:    
            for elemento in self.lista_adj[vertice - 1]:
                arestas_A.append((vertice, elemento))

        arestas_B = []
        for vertice in grupo_B:    
            for elemento in self.lista_adj[vertice - 1]:
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