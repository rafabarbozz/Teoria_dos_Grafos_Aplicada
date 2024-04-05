# Função para ler o arquivo txt e transformar em matriz de adjacência e na lista de arestas do grafo, considerando que os vértice começam de 1
def ler_grafo(caminho):
    # Criando matriz de adjacência
    arq = open(caminho, 'r') # Abrindo arquivo txt
    texto = arq.readlines() # Lendo linhas do arquivo txt
    arq.close()

    # Criando matriz de adjacência
    matriz_adj = []
    for i in range(1, len(texto)): # Vai de 1 até o len de uma linha
        linha_matriz = []
        for j in range(len(texto[i])): # Para cada elemento na linha
            if texto[i][j] == "0" or texto[i][j] == "1": # Se o elemento for 0 ou 1 vai colocar ele na lista "linha" como int
                linha_matriz.append(int(texto[i][j]))

        matriz_adj.append(linha_matriz)


    # Criando lista de aresta
    lista_aresta = []
    for i in range(len(matriz_adj)):
        for j in range(i+1, len(matriz_adj)):
            if matriz_adj[i][j] == 1:
                lista_aresta.append((i+1, j+1))

            
    return matriz_adj, lista_aresta
