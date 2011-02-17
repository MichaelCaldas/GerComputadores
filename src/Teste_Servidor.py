'''
Created on 15/02/2011

@author: Michael
'''
from should_dsl.dsl import should
from should_dsl.matchers import equal_to
import unittest
from Servidor import Servidor
class Teste_Servidor(unittest.TestCase):
    
    def testeAdicionaUmServidor(self):
        self.servidor = Servidor("001", "Servidor Unix", 500, 4, 200, 10)
        self.servidor.codPatrimonio |should| equal_to("001")
        self.servidor.descricao |should| equal_to("Servidor Unix")
        self.servidor.hd |should| equal_to(500)
        self.servidor.memoria |should| equal_to(4)
        self.servidor.tamanhoBuffer |should| equal_to(200)
        self.servidor.quantidadeBuffer |should| equal_to(10)
        self.servidor.todosServidores[0].tamanhoBuffer |should| equal_to(200)
        self.servidor.armazenaImpressorasConectadas("001")
        self.servidor.recuperaImpressorasConectadas()[0] |should| equal_to("001")
    
#    def testeRecuperaImpressorasConectadas(self):
#        self.servidor.armazenaImpressorasConectadas("001")
#        self.servidor.recuperaImpressorasConectadas() |should| equal_to("002")

