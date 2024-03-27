# Função para ler o arquivo txt e transformar em lista de adjacência os vértice começam de 1
def ler_grafo(caminho):
    # Exemplo de caminho: 'Trabalho2/modelos/in/graph_{i}'
    # Criando lista de adjacência
    
    arq = open(caminho, 'r') # Abrindo arquivo txt
    texto = arq.readlines() # Lendo linhas do arquivo txt
    arq.close()

    lista_adj = []

    for i in range(1, int(len(texto[1]) / 2) + 1): # Vai de 1 até o len de uma linha (14) dividido por 2
        linha_lista = []

        for n, elemento in enumerate(texto[i]):
            if elemento in "1":
                linha_lista.append(int(n/2))

        lista_adj.append(linha_lista)
    
    return lista_adj


