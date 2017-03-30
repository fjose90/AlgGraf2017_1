from random import randint, choice

prof_entrada = {}  # hash map (aka 'dicionario')
prof_saida = {}
pai = {}
low = {}
demarcador = {}
articulacoes = set()


def criar_grafo(vertices):
    grafo = {}
    for v in vertices:
        grafo[v] = set()
        low[v] = v
    return grafo

def adicionar_aresta(G, vertice1, vertice2):
    G[vertice1].add(vertice2)
    G[vertice2].add(vertice1)

def busca_prof(G, v):
    prof_entrada[v] = len(prof_entrada) + 1
    for w in G[v]:
        
        if prof_entrada.get(w) is None:
            
            pai[w] = v
            busca_prof(G, w)  # chamada recursiva

            if demarcador[w]:
                articulacoes.add(v)

            if prof_entrada[low[w]] < prof_entrada[low[v]]:
                low[v] = low[w]
            
        else:
            
            if prof_saida.get(w) is None and pai[v] != w:
                if prof_entrada[w] < prof_entrada[low[v]]:
                    low[v] = w
                
    prof_saida[v] = len(prof_saida) + 1
    demarcador[v] = low[v] == v or low[v] == pai.get(v)

             
def encontrar_articulacoes(G):
    n = len(G)
    raiz = choice(list(G.keys()))
    print("raiz = %s" % raiz)
    
    busca_prof(G, raiz)

    cont_filhos_raiz = 0
    for v in range(n):
        if pai.get(v) == raiz:
            cont_filhos_raiz += 1
    if cont_filhos_raiz <= 1:
        articulacoes.remove(raiz)

    print("articulacoes = " + str(articulacoes))
                   
            



## Main

G = criar_grafo(["a", "b", "c", "d", "e", "f"])
adicionar_aresta(G, "a", "b")
adicionar_aresta(G, "a", "d")
adicionar_aresta(G, "b", "c")
adicionar_aresta(G, "b", "d")
adicionar_aresta(G, "d", "e")
adicionar_aresta(G, "d", "f")
adicionar_aresta(G, "e", "f")
encontrar_articulacoes(G)






