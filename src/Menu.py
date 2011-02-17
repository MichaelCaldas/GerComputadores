'''
Created on 15/02/2011

@author: Michael&karolyne
'''
from Estacao import Estacao
from Micro import Micro
from Servidor import Servidor
from Usuario import Usuario
from Impressora import Impressora

class Menu():
    def __init__(self):
        self.iniciaMenu()
        
    def iniciaMenu(self):      
        opcao = 0

        while opcao != 10:
            print "1 - Cadastrar Usuario"
            print "2 - Cadastrar Estacao"
            print "3 - Cadastrar Servidor"
            print "4 - Cadastrar Impressora"
            print "5 - Listar Usuarios"
            print "6 - Listar Estacoes"
            print "7 - Listar Servidores"
            print "8 - Listar Impressoras"
            print "9 - Associar Impressoras a um Servidor"
            print "10 - Sair"
            opcao = input("O que deseja fazer: ")
    
            if opcao == 1:
                print "Nome: "
                nomeGuerra = raw_input()
                print "Senha: "
                senha = input()
                usuario = Usuario(nomeGuerra, senha)
               
            if opcao == 2:
                codPatrimonio = raw_input("Codigo do Patrimonio: ")
                descricao = raw_input("Descricao: ")
                hd = input("HD: ")
                memoria = input("Memoria: ")
                localizacao = raw_input("Localizacao: ")
                estacao = Estacao(codPatrimonio, descricao, hd, memoria, localizacao)
                
            if opcao == 3:
                codPatrimonio = raw_input("Codigo do Patrimonio: ")
                descricao = raw_input("Descricao: ")
                hd = input("HD: ")
                memoria = input("Memoria: ")
                tamanhoBuffer = input("Tamanho do Buffer: ")
                quantidadeBuffer = input("Quantidade de Buffer: ")
                servidor = Servidor(codPatrimonio, descricao, hd, memoria, tamanhoBuffer, quantidadeBuffer)
                
                
            if opcao == 4:
                codPatrimonio = raw_input("Codigo do Patrimonio: ")
                descricao = raw_input("Descricao: ")
                velocidade = input("Velocidade: ")
                servidorAux = raw_input("Servidor: ")
                for i in range(len(servidor.todosServidores)):
                    if servidorAux == servidor.todosServidores[i].codPatrimonio:
                        achou = True
                        impressora = Impressora(codPatrimonio, descricao, velocidade, servidorAux)
                        break
                    else:
                        achou = False
                if achou == True:
                    "Impressoa cadastrada com sucesso! \n"
                else:
                    "Nao foi possivel cadastrar a impressora, verifique se o servidor foi informado corretamente \n!"

            if opcao == 5:
                for i in range(len(usuario.todosUsuarios)):
                    print usuario.todosUsuarios[i].nomeGuerra
                    print usuario.todosUsuarios[i].senha       

            if opcao == 6:
                for i in range(len(estacao.todasEstacoes)):
                    print "Codigo: " + estacao.todasEstacoes[i].codPatrimonio
                    print "Descricao: " + estacao.todasEstacoes[i].descricao
                    print "HD: ", estacao.todasEstacoes[i].hd
                    print "Memoria: ", estacao.todasEstacoes[i].memoria
                    print "Localizacao: " + estacao.todasEstacoes[i].localizacao
                    print "\n"
                    
            if opcao == 7:
                for i in range(len(servidor.todosServidores)):
                    print "Listando Servidores"
                    print "Codigo: " + servidor.todosServidores[i].codPatrimonio
                    print "Descricao: " + servidor.todosServidores[i].descricao
                    print "HD: ", servidor.todosServidores[i].hd
                    print "Memoria: ", servidor.todosServidores[i].memoria
                    print "Tamanho do Buffer: ", servidor.todosServidores[i].tamanhoBuffer
                    print "Quantidade de Buffer: ", servidor.todosServidores[i].quantidadeBuffer
                    print "Impressoras conectadas: ", servidor.todosServidores[i].recuperaImpressorasConectadas()
                        
                    print "\n"
            
            if opcao == 8:
                for i in range(len(impressora.todasImpressoras)):
                    print "Codigo: " + impressora.todasImpressoras[i].codPatrimonio
                    print "Descricao: " + impressora.todasImpressoras[i].descricao
                    print "Velocidade: ", impressora.todasImpressoras[i].velocidade
                    print "Conectada ao Servidor: " + impressora.todasImpressoras[i].servidor
                    
            if opcao == 9:
                cadastrar = raw_input("Deseja cadastrar alguma impressora(s/n): ")
                
                if cadastrar == "s":
                    codImpressora = input("Infome a impressora que deseja cadastrar: ")
                    for i in range(len(impressora.todasImpressoras)):
                        if codImpressora == impressora.todasImpressoras[i].codPatrimonio:
                            achou = True
                            break
                        else:
                            achou = False
                        if achou == True:
                            servidorAux = raw_input("Em qual servidor deseja cadastrar a impressora: ")
                            for i in range(len(servidor.todosServidores)):
                                if servidorAux == servidor.todosServidores[i].codPatrimonio:
                                    achou = True
                                    break
                                else:
                                    achou = False
                                if achou == True:
                                    servidor.todosServidores[i].armazenaImpressorasConectadas(codImpressora)
                                    print "Impressora associada com sucesso ao servidor!"
                                else:
                                    print "Nao foi possivel associar a impressora ao servidor desejado!"
                        else:
                            print "A impressora nao foi localizada!"
                                      
                                
menu = Menu()
