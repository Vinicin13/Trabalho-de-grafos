import statistics as stt
import os
import matplotlib.pyplot as grafico
import psutil
import time

def gerar_Grafico(Graus):
    grafico.xlabel("Vertice")
    grafico.ylabel("Grau")
    grafico.axis(ymin=0, ymax=max(Graus))
    grafico.axis(xmin=0, xmax=len(Graus))
    grafico.plot(Graus)
    grafico.show()

def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

def lista(arq):


    memoryStart = get_process_memory()
    arq.seek(0)
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    Vertices = int(FirstLine[0])
    Arestas = int(FirstLine[1])

    Lista = [[] for x in range(Vertices)]

    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        z = int(Aresta[2])
        Lista[x].append((y, z))
        Lista[y].append((x, z))

    memoryEnd = get_process_memory()
    Memoria = (memoryEnd - memoryStart) / (1024 * 1024)
    print("Lista:\n")
    print(Memoria, "MB")


    return Lista

def matriz(arq):

    memoryStart = get_process_memory()
    arq.seek(0)
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    Vertices = int(FirstLine[0])
    Arestas = int(FirstLine[1])
    Matriz = [[0 for _ in range(Vertices)] for _ in range(Vertices)]

    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        z = int(Aresta[2])
        Matriz[x][y] = z
        Matriz[y][x] = z

    memoryEnd = get_process_memory()
    Memoria = (memoryEnd - memoryStart) / (1024 * 1024)
    print("Matriz:\n")

    print(Memoria, "MB")
    return Matriz

def informacoes(Grafo):

    MaiorG = 0
    MenorG = len(Grafo)

    VerticeMaiorG = 0
    VerticeMenorG = 0

    Graus = []

    for i in range(len(Grafo)):

            cont = len(Grafo[i]) - Grafo[i].count(0)
            Graus.append(cont)
            if MaiorG < cont:
                MaiorG = cont
                VerticeMaiorG = i
            if MenorG > cont:
                MenorG = cont
                VerticeMenorG = i

    print("Maior grau: %d -- vertice: %d \n"
          "Menor grau: %d -- vertice: %d \n"
          "\nGrau medio: %.7f" % (MaiorG, VerticeMaiorG, MenorG, VerticeMenorG, stt.mean(Graus)))
    print("\nFrequencia relativa:")
    #Calcula a frequencia de cada grau
    for i in sorted(set(Graus)):
        Frequencia = Graus.count(i) / len(Graus)
        print("Grau %d: %.7f " % (i, Frequencia))
    return Graus

def busca_in_Largura(Grafo, VInicial,tipo):
    if tipo == 1:
        print("Matriz")
        start = time.time()
        desc = [0 for i in range(len(Grafo))]
        Q = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        nivel = [0 for i in range(len(Grafo))]  # Cria lista de niveis
        nivel[VInicial] = 0  # grava o nivel inicial
        realmenor = []  # auxiliar pra guardar o menor nivel que esta ligado o vertice

        while len(Q) != 0:

            u = Q.pop(0)
            for i in range(len(Grafo[u])):  # percorre a linha u da matriz
                if Grafo[u][i] != 0:
                    if desc[i] == 0:
                        nivel[i] = nivel[u] + 1

            for v in range(len(Grafo)):
                if Grafo[u][v] != 0:
                    if desc[v] == 0:
                        Q.append(v)
                        R.append(v)
                        desc[v] = 1

        for i in range(len(desc)):
            if desc[i] == 0 and i != VInicial:
                for x in range(len(Grafo[i])):
                    if Grafo[i][x] != 0:
                        if x in R:
                            nivel[i] = nivel[x] + 1
                            realmenor.append(nivel[i])
            if len(realmenor) > 1:
                for x in range(len(realmenor) - 1):
                    if realmenor[x] < realmenor[x + 1]:
                        nivel[i] = realmenor[x + 1]

        arquivo = open("saida.txt", "w")
        arquivo.write("#vertice : nivel \n")
        for i in range(len(nivel)):
            if nivel[i] != nivel[VInicial] or i == VInicial:
                arquivo.write("%d : %d \n" % (i, nivel[i]))
        End = time.time()
        print(End - start, "milesegundos")
        return nivel
    elif tipo == 2:
        print("Lista")
        start = time.time()

        desc = [0 for i in range(len(Grafo))]
        Q = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        nivel = [0 for i in range(len(Grafo))]
        nivel[VInicial] = 0

        while len(Q) != 0:

            u = Q.pop(0)

            for i in range(len(Grafo[u])):
                if desc[Grafo[u][i][0]] == 0:
                    nivel[Grafo[u][i][0]] = nivel[u] + 1

            for v in range(len(Grafo[u])):
                if desc[Grafo[u][v][0]] == 0:
                    Q.append(Grafo[u][v][0])
                    R.append(Grafo[u][v][0])
                    desc[Grafo[u][v][0]] = 1

        for i in range(len(desc)):
            if desc[i] == 0 and i != VInicial:
                for x in range(len(Grafo[i])):
                    if Grafo[i][x][0] in R:
                        if len(Grafo[i]) > 1:
                            if nivel[i] == 0:
                                nivel[i] = nivel[Grafo[i][x][0]] + 1
                            elif nivel[i] > nivel[Grafo[i][x][0]] + 1:
                                nivel[i] = nivel[Grafo[i][x][0]] + 1
                        else:
                            nivel[i] = nivel[Grafo[i][x][0]] + 1

        arquivo = open("saida.txt", "w")
        arquivo.write("#vertice : nivel \n")
        for i in range(len(nivel)):
            if nivel[i] != nivel[VInicial] or i == VInicial:
                arquivo.write("%d : %d \n" % (i, nivel[i]))

        End = time.time()
        print(End - start, "milesegundos")
        return nivel



def busca_in_Profundidade(Grafo, VInicial,tipo):
    if tipo == 1:

        print("Matriz")
        desc = [0 for i in range(len(Grafo))]
        S = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1

        while len(S) != 0:
            u = S[-1]
            desempilhar = True

            for v in range(len(Grafo[u])):
                if Grafo[u][v] != 0:
                    if desc[v] == 0:
                        desempilhar = False
                        S.append(v)
                        R.append(v)
                        desc[v] = 1
                        break

            if desempilhar:
                S.pop()


        return R
    elif tipo == 2:

        print("Lista")
        desc = [0 for i in range(len(Grafo))]
        S = [VInicial]
        R = [VInicial]
        desc[VInicial] = 1
        while len(S) != 0:
            u = S[-1]
            desempilhar = True

            for v in Grafo[u]:
                if v != []:
                    if desc[v[0]] == 0:
                        desempilhar = False
                        S.append(v[0])
                        R.append(v[0])
                        desc[v[0]] = 1
                        break
            if desempilhar:
                S.pop()

        return R
    else:
        print("Escolha o Tipo correto!")


def componentes_conexos(Grafo,VInicial = 0):

    Maior = 0
    Menor = len(Grafo)


    desc = [0 for i in range(len(Grafo))]
    Q = [VInicial]
    R = [VInicial]
    desc[VInicial] = 1
    count = 0
    conexo = 0

    while len(Q) != 0:

        u = Q.pop(0)

        for v in range(len(Grafo)):
            if Grafo[u][v] != 0:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1

    if Maior < len(R):
        Maior = len(R)
    if Menor > len(R):
        Menor = len(R)
    vprint = []  ##Guarda as componentes conexas
    vprint.append("-- %d vertices" % (len(R)))
    for v in range(len(desc)):
        if desc[v] == 0:
            count = count + 1
            for x in R:
                if Grafo[x][v] != 0 or Grafo[v][x]:
                    conexo = conexo + 1
                    break
        if count != conexo and desc[v] == 0:  ##Descobre quando a componente não conexa existe
            ##Funçao similiar para conseguir fazer a busca recursiva
            ##Retira dois paramentros e adiciona dois
            ##Passa os descobertos e a lista com os descobertos(String)
            Q = [v]
            R = [v]
            desc[v] = 1
            while len(Q) != 0:

                u = Q.pop(0)

                for v in range(len(Grafo)):
                    if Grafo[u][v] != 0:
                        if desc[v] == 0:
                            Q.append(v)
                            R.append(v)
                            desc[v] = 1
            if Maior < len(R):
                Maior = len(R)
            if Menor > len(R):
                Menor = len(R)
            vprint.append("-- %d vertices" % (len(R)))
    print("%d - Vertices ---- Maior componente conexa \n"
          "%d - Vertices ---- Menor componente conexa \n" % (Maior, Menor))
    print("Componentes conexas: %d" % (len(vprint)))
    for i in vprint:
        print(i)
