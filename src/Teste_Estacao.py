'''
Created on 16/02/2011

@author: Karol
'''
from should_dsl.dsl import should
from should_dsl.matchers import equal_to
import unittest
from Estacao import Estacao


class Teste_Estacao(unittest.TestCase):
    
    def testeAdicionaUmaEstacao(self):
        self.estacao = Estacao("Sala 101")
        self.estacao.localizacao |should| equal_to("Sala 101")
        self.estacao.todasEstacoes[0].localizacao |should| equal_to("Sala 101")
        self.estacao.codPatrimonio |should| equal_to("002")
        
