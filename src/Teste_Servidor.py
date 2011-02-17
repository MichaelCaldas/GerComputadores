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
        self.servidor = Servidor(200, 10)
        self.servidor.tamanhoBuffer |should| equal_to(200)
        self.servidor.quantidadeBuffer |should| equal_to(10)
        self.servidor.todosServidores[0].tamanhoBuffer |should| equal_to(200)