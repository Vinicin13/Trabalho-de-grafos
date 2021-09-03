import Funções

def menu():


     print("Menu principal:\n Escolha de 1 a 4 entre:\n 1- Arquivo de Teste 'example.txt'\n"
          " 2- Arquivo de Colaborações em pesquisa 'collaboration_graph.txt'\n 3- Arquivo de Coxexões da web 'as_graph.txt'\n"
          " 4 -Sair")
     opção = int(input("Opção:"))

     if opção == 1:
         return(menu_ArquivoTeste(opção))

     if opção == 2:
         return(menu_ArquivoColaboração(opção))
     if opção == 3:
         return(menu_ArquivoConexões(opção))
     if opção == 4:
         return(0)



def menu_ArquivoTeste(percurso):

    while percurso != 8:
        print("Arquivo de Teste 'example.txt':\n Escolha de 0 a 7 entre:\n 0- Gerar grafico \n 1- Representar em forma de Lista\n"
          " 2- Representar em forma de Matriz\n 3- Informações desse grafo\n 4- Gerar arquivo de saida de uma Busca em Largura\n"
              " 5- Gerar arquivo de saida de uma Busca em Profundidade\n 6- Componentes Conexas\n 7- Voltar ao Menu Principal\n 8- Sair")
        opção1 = int(input("Opção:"))

        if opção1 == 0:
            arquivo = open("example.txt","r")
            ma = Funções.matriz(arquivo)
            grau = Funções.informacoes(ma)
            Funções.gerar_Grafico(grau)
            return(menu_ArquivoTeste(opção1))

        if opção1 == 1:
            arquivo = open("example.txt","r")
            li = Funções.lista(arquivo)
            print(li)
            return(menu_ArquivoTeste(opção1))

        if opção1 == 2:
            arquivo = open("example.txt", "r")
            ma = Funções.matriz(arquivo)
            print(ma)
            return (menu_ArquivoTeste(opção1))

        if opção1 == 3:
            arquivo = open("example.txt", "r")
            ma = Funções.matriz(arquivo)
            Funções.informacoes(ma)
            return (menu_ArquivoTeste(opção1))

        if opção1 == 4:
            arquivo = open("example.txt", "r")
            ma = Funções.matriz(arquivo)
            VerticeI = int(input("Qual o vertice inical da busca?"))
            Funções.busca_in_Largura(ma,VerticeI,1)
            return (menu_ArquivoTeste(opção1))

        if opção1 == 5:
            arquivo = open("example.txt", "r")
            ma = Funções.matriz(arquivo)
            VerticeI = int(input("Qual o vertice inical da busca?"))
            Funções.busca_in_Profundidade(ma,VerticeI,1)
            return (menu_ArquivoTeste(opção1))

        if opção1 == 6:
            arquivo = open("example.txt", "r")
            ma = Funções.matriz(arquivo)
            Funções.componentes_conexos(ma,0)

            return (menu_ArquivoTeste(opção1))

        if opção1 == 7:
            return(menu())

        if opção1 == 8:
            return((menu_ArquivoTeste(opção1)))

def menu_ArquivoColaboração(percurso):

    while percurso != 8:
        print("Arquivo de Colaborações em pesquisa 'collaboration_graph.txt':\n Escolha de 0 a 7 entre:\n 0- Gerar grafico\n 1- Representar em forma de Lista\n"
          " 2- Representar em forma de Matriz\n 3- Informações desse grafo\n 4- Gerar arquivo de saida de uma Busca em Largura\n"
              " 5- Gerar arquivo de saida de uma Busca em Profundidade\n 6- Componentes Conexas\n 7- Voltar ao Menu Principal\n 8- Sair")
        opção2 = int(input("Opção:"))

        if opção2 == 0:
            arquivo = open("collaboration_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            grau = Funções.informacoes(ma)
            Funções.gerar_Grafico(grau)
            return (menu_ArquivoColaboração(opção2))

        if opção2 == 1:
            arquivo = open("collaboration_graph.txt","r")
            li = Funções.lista(arquivo)
            print(li)

            return(menu_ArquivoColaboração(opção2))

        if opção2 == 2:
            arquivo = open("collaboration_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            print(ma)
            return (menu_ArquivoColaboração(opção2))

        if opção2 == 3:
            arquivo = open("collaboration_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            Funções.informacoes(ma)
            return (menu_ArquivoColaboração(opção2))

        if opção2 == 4:
            arquivo = open("collaboration_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            li = Funções.lista(arquivo)
            VerticeI = int(input("Qual o vertice inical da busca?"))
            tipo = int(input("Deseja operar usando Lista:Digite 2\nDeseja operar usando Matriz:Digite 1"))
            if tipo == 1:
               Funções.busca_in_Largura(ma, VerticeI, tipo)
               return (menu_ArquivoColaboração(opção2))

            if tipo == 2:
                Funções.busca_in_Largura(li, VerticeI, tipo)
                return (menu_ArquivoColaboração(opção2))

        if opção2 == 5:
            arquivo = open("collaboration_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            li = Funções.lista(arquivo)
            VerticeI = int(input("Qual o vertice inical da busca?"))
            tipo = int(input("Deseja operar usando Lista:Digite 2\nDeseja operar usando Matriz:Digite 1"))
            if tipo == 1:
                Funções.busca_in_Profundidade(ma, VerticeI, tipo)
                return (menu_ArquivoColaboração(opção2))

            if tipo == 2:
                Funções.busca_in_Profundidade(li, VerticeI, tipo)
                return (menu_ArquivoColaboração(opção2))

        if opção2 == 6:
            arquivo = open("collaboration_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            Funções.componentes_conexos(ma,0)
            return (menu_ArquivoColaboração(opção2))

        if opção2 == 7:
            return(menu())

        if opção2 == 8:
            return((menu_ArquivoColaboração(opção2)))

def menu_ArquivoConexões(percurso):

    while percurso != 8:
        print("Arquivo de Coxexões da web 'as graph.txt':\n Escolha de 0 a 7 entre:\n 0- Gerar Grafico\n 1- Representar em forma de Lista\n"
          " 2- Representar em forma de Matriz\n 3- Informações desse grafo\n 4- Gerar arquivo de saida de uma Busca em Largura\n"
              " 5- Gerar arquivo de saida de uma Busca em Profundidade\n 6- Componentes Conexas\n 7- Voltar ao Menu Principal\n 8- Sair")
        opção3 = int(input("Opção:"))

        if opção3 == 0:
            arquivo = open("as_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            grau = Funções.informacoes(ma)
            Funções.gerar_Grafico(grau)

            return (menu_ArquivoConexões(opção3))
        if opção3 == 1:
            arquivo = open("as_graph.txt","r")
            li = Funções.lista(arquivo)
            print(li)
            return(menu_ArquivoConexões(opção3))

        if opção3 == 2:
            arquivo = open("as_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            print(ma)

            return (menu_ArquivoConexões(opção3))

        if opção3 == 3:
            arquivo = open("as_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            Funções.informacoes(ma)
            return (menu_ArquivoConexões(opção3))

        if opção3 == 4:
            arquivo = open("as_graph.txt", "r")

            li = Funções.lista(arquivo)
            VerticeI = int(input("Qual o vertice inical da busca?"))

            Funções.busca_in_Largura(li,VerticeI,2)
            return (menu_ArquivoConexões(opção3))

        if opção3 == 5:
            arquivo = open("as_graph.txt", "r")

            li = Funções.lista(arquivo)
            VerticeI = int(input("Qual o vertice inical da busca?"))

            Funções.busca_in_Profundidade(li,VerticeI,2)
            return (menu_ArquivoConexões(opção3))

        if opção3 == 6:
            arquivo = open("as_graph.txt", "r")
            ma = Funções.matriz(arquivo)
            Funções.componentes_conexos(ma,0)
            return (menu_ArquivoConexões(opção3))

        if opção3 == 7:
            return(menu())

        if opção3 == 8:
            return((menu_ArquivoConexões(opção3)))
