from random import seed, sample
        
class Krager:
    def __init__(self, lista_adj: list, lista_aresta: list):
        ''''
        Lista_adj(list): é a lista de adjacência do grafo
        Lista_aresta(list): é uma lista de tuplas que informa quais arestas estão presentes no grafo
        '''
        self.lista_adj = lista_adj
        self.lista_aresta = lista_aresta

    
    def run(self):
        seed(1)
        lista_aresta_copy = self.lista_aresta.copy()
        lista_adj_copy = self.lista_adj.copy()
        
        while lista_adj_copy.count([]) < (len(lista_adj_copy) - 2): # Se só restarem 2 vértices não vazios finaliza o loop
            aresta_escolhida = sample(lista_aresta_copy, 1)[0] # Escolhendo uma aresta aleatoriamente
            
            print(f'Aresta escolhida: {aresta_escolhida}')  
            print(f'Lista_adj antes: {lista_adj_copy}') 
            print(f'Lista_aresta antes: {lista_aresta_copy}\n')
            
            
            for elemento in (lista_adj_copy[aresta_escolhida[1] - 1]):
                # Adicionando na lista de adjacencia do primeiro elemento todos os vertices do segundo elemento
                if elemento not in lista_adj_copy[aresta_escolhida[0] - 1] and elemento != aresta_escolhida[0]:
                    lista_adj_copy[aresta_escolhida[0] - 1].append(elemento)
                
                # Adicionando a lista de aresta todas as arestas do segundo elemento para o primeiro
                if (aresta_escolhida[0], elemento) not in lista_aresta_copy and (elemento, aresta_escolhida[0]) and elemento != aresta_escolhida[0]:
                    lista_aresta_copy.append((aresta_escolhida[0], elemento))
            
             
            # Loop usado para retirar as arestas que o segundo elemento da aresta escolhida possui na lista de arestas
            for aresta in lista_aresta_copy:
                if aresta[0] == aresta_escolhida[1]:
                    lista_aresta_copy.remove(aresta)
                    
                elif aresta[1] == aresta_escolhida[1]:
                    lista_aresta_copy.remove(aresta)
                
                
            # Esvaziando lista adj na segunda posição da aresta escolhida
            lista_adj_copy[aresta_escolhida[1] - 1].clear()
            
            
            print(f'Lista_adj depois: {lista_adj_copy}') 
            print(f'Lista_aresta depois: {lista_aresta_copy}')
            print('\n')
    
        return len(lista_aresta_copy)
