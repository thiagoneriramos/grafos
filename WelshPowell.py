#importa biliotecas
import networkx as nx #biblioteca de criação e manipulação de grafos
import matplotlib.pyplot as pl #biblioteca para a plotagem de grafos
from random import randrange #biblioteca para randomizar valores
def WelshPowell(G=nx.Graph()):

   listaCores = [] #lista de cores rgba com |V| elementos
   listaCoresVertice = {} # lista de cores de 0 a |V| -1
   graus = [] #grau do vertice
   corAleatoria = [255,0,0,1] #primeira cor a ser utilizada

   # preenche lista de todas as cores (|V| cores) rgb que podem ser utilizadas
   #com cores aleatórias geradas em rgb
   for v in G.nodes_iter():

      #enquanto nao achar uma cor que nao está nas cores que podem ser utilizadas
      while (corAleatoria[0],corAleatoria[1],corAleatoria[2],1) in listaCores:

         corAleatoria.clear() #limpa lista que terá o rgba da cor "sorteada"

         for i in range(0,3):
            corAleatoria.append(randrange(0,255))

      #coloca elemento na lista de cores que podem ser utilizadas
      listaCores.append((corAleatoria[0],corAleatoria[1],corAleatoria[2],1))

      listaCoresVertice[v] = [] #inicializa lista de cores de cada vértice
      graus.append((nx.degree(G,v),v)) #armazena o grau do vértice em tupla


   countEl = 0 #contagem de elementos que vao ter no array de cores do vertice v

   #duplica graus, para colocar o numero certo de cores em cada vertice
   bkpGraus = graus[:]

   #coloca lista de cores de cada vértice ordenado por grau decrescentemente
   for i in range(0,G.number_of_nodes()):

      #valor maximo da tupla (grau,vertice) é o maior grau
      indiceMax = max(bkpGraus)[1] #vértice
      valorMax = max(bkpGraus)[0] #grau do vertice
      countEl+=1 #numero de cores no vertice atual

      #preenche cores que podem ser utilizadas
      for i in range(0,countEl):
         listaCoresVertice[indiceMax].append(i)

      #retira tupla utilizada para selecionar o proximo maior grau
      bkpGraus.remove((valorMax,indiceMax))

   particoes = {} #particoes do grafo (cores com seus vertices)

   #Pega a primeira cor da lista de cada vértice e atualiza a lista de cores dos vizinhos
   for i in range(0,G.number_of_nodes()):

      indiceMax = max(graus)[1] #vértice
      valorMax = max(graus)[0] #grau do vertice

      #se for o primeiro elemento da particao
      if listaCoresVertice[indiceMax][0] not in particoes:
         particoes[listaCoresVertice[indiceMax][0]] = []

      #tupla dos tons rgba da cor do primeiro indice do vértice selecionado
      a,b,c,d = listaCores[listaCoresVertice[indiceMax][0]]

      #coloca vertice na particao
      particoes[listaCoresVertice[indiceMax][0]].append(indiceMax)

      #atualiza vizinhos, tirando indice da cor utilizada
      for vizinho in G.neighbors_iter(indiceMax):
         if listaCoresVertice[indiceMax][0] in listaCoresVertice[vizinho]:
            listaCoresVertice[vizinho].remove(listaCoresVertice[indiceMax][0])

      #Caso nao tenha o atributo viz, essas linhas abaixo são necessarias
      G.node[indiceMax]['viz'] = {}
      G.node[indiceMax]['viz']['color'] = {}
      G.node[indiceMax]['viz']['color']['r'] = []
      G.node[indiceMax]['viz']['color']['g'] = []
      G.node[indiceMax]['viz']['color']['b'] = []
      G.node[indiceMax]['viz']['color']['a'] = []

      #atualiza cores para visualização do arquivo em outros programas
      G.node[indiceMax]['viz']['color']['r'] = int(a)
      G.node[indiceMax]['viz']['color']['g'] = int(b)
      G.node[indiceMax]['viz']['color']['b'] = int(c)
      G.node[indiceMax]['viz']['color']['a'] = d

      #remove o vertice selecionado para que possa seguir para o proximo vertice de maior grau
      graus.remove((valorMax,indiceMax))

   return particoes
