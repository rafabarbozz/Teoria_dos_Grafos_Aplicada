from random import sample, seed
        
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
        lista_adj_copy = [adj_lista.copy() for adj_lista in self.lista_adj]  # Criando uma cópia profunda da lista de adjacência

        while len([lst for lst in lista_adj_copy if lst]) > 2: # Se só restarem 2 vértices não vazios finaliza o loop
            aresta_escolhida = sample(lista_aresta_copy, 1)[0] # Escolhendo uma aresta aleatoriamente

            for elemento in (lista_adj_copy[aresta_escolhida[1] - 1]):
                # Adicionando na lista de adjacencia do primeiro elemento todos os vertices do segundo elemento tirando ele mesmo
                if elemento not in lista_adj_copy[aresta_escolhida[0] - 1] and elemento != aresta_escolhida[0]:
                    lista_adj_copy[aresta_escolhida[0] - 1].append(elemento)
                
                # Adicionando na lista de aresta todas as arestas do segundo elemento para o primeiro
                if (aresta_escolhida[0], elemento) not in lista_aresta_copy and (elemento, aresta_escolhida[0]) and elemento != aresta_escolhida[0]:
                    lista_aresta_copy.append((aresta_escolhida[0], elemento))
            
            
            # Loop usado para retirar as arestas que o segundo elemento da aresta escolhida possui na lista de arestas, se usar o remove pode dar problema com 
            # elementos sendo pulados
            lista_aresta_copy = [aresta for aresta in lista_aresta_copy if aresta_escolhida[1] not in aresta]
    
                 
            # Esvaziando lista adj na posição do segundo elemento da aresta escolhida
            lista_adj_copy[aresta_escolhida[1] - 1].clear()
        
        return len(lista_aresta_copy)
    

    def executar_n(self, n):
        corte_minimo = float('inf')
        for _ in range(n):
            qtd_corte, lista_adj = (self.run())
            if qtd_corte < corte_minimo:
                corte_minimo = qtd_corte
        
        return corte_minimo
    
    