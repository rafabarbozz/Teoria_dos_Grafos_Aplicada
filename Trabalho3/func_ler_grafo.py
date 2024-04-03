# Função para ler o arquivo txt e transformar em matriz de adjacência e na lista de arestas do grafo, considerando que os vértice começam de 1
def ler_grafo(caminho):
    # Exemplo de caminho: 'Trabalho3/modelos/in/graph_{i}'
        
   # Criando lista de adjacência
    arq = open(caminho, 'r') # Abrindo arquivo txt
    texto = arq.readlines() # Lendo linhas do arquivo txt
    arq.close()

    lista_adj = []
    for i in range(1, int(len(texto[1]) / 2) + 1): # Vai de 1 até o len de uma linha (14) dividido por 2
        linha_lista = []

        for n, elemento in enumerate(texto[i]):
            if elemento in "1":
                linha_lista.append(int(n/2) + 1)

        lista_adj.append(linha_lista)


    lista_aresta = []
    for n, lista in enumerate(lista_adj):
        for elemento in lista:
            if [n+1, elemento] not in lista_aresta and [elemento, n+1] not in lista_aresta:
                lista_aresta.append([n+1, elemento])

    return lista_adj, lista_aresta