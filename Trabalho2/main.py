from func_ler_grafo import ler_grafo
from buscas import busca_largura, busca_profundidade

for c in range(1, 21):
    # Gerando arquivos GDF's para busca em profundidade para cada grafo de entrada
    lista_adj = ler_grafo(f'Trabalho2/modelos/in/graph_{c}')
    profundidade = busca_profundidade.Busca_profundidade(lista_adj)
    profundidade.run(0)

    # Criando a string que irá no arquivo
    gdf = ""
    gdf+= "nodedef>name VARCHAR,label VARCHAR\n"
    for n in range(1, len(lista_adj) + 1):
        gdf+= f"{n},{n}\n"

    gdf += "edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n"
    for i in range(len(profundidade.lista_adj)):
        for j in range(i + 1, len(profundidade.lista_adj)):
            if profundidade.matriz_cores[i][j] != None:
                gdf += f"{i + 1},{j + 1}," + "false," + f"'{profundidade.matriz_cores[i][j]}'\n"

    # Abrindo o arquivo para escrita
    with open(f"Trabalho2/solucoes_encontradas/profundidade/profundidade_solucao_graph_{c}.gdf", "w") as arquivo:
        arquivo.write(gdf)
    
    
    # Gerando arquivos GDF's para busca em largura para cada grafo de entrada
    lista_adj = ler_grafo(f'Trabalho2/modelos/in/graph_{c}')
    largura = busca_largura.Busca_largura(lista_adj)
    largura.run(0)

    # Criando a string que irá no arquivo
    gdf = ""
    gdf+= "nodedef>name VARCHAR,label VARCHAR\n"
    for n in range(1, len(lista_adj) + 1):
        gdf+= f"{n},{n}\n"

    gdf += "edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n"
    for i in range(len(largura.lista_adj)):
        for j in range(i + 1, len(largura.lista_adj)):
            if largura.matriz_cores[i][j] != None:
                gdf += f"{i + 1},{j + 1}," + "false," + f"'{largura.matriz_cores[i][j]}'\n"

    # Abrindo o arquivo para escrita
    with open(f"Trabalho2/solucoes_encontradas/largura/largura_solucao_graph_{c}.gdf", "w") as arquivo:
        arquivo.write(gdf)
    
    raio, diametro = largura.calc_exentricidade()
    media = largura.calc_media()
    print(f"---- Grafo {c} ----\n"
          f"- Media: {media:.3f}\n"
          f"- Raio: {raio}\n"
          f"- Diametro: {diametro}\n")
    
    
    