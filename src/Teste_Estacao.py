'''
Created on 16/02/2011

@author: Karolyne
'''
from should_dsl.dsl import should
from should_dsl.matchers import equal_to
import unittest
from Estacao import Estacao


class Teste_Estacao(unittest.TestCase):
    
    def testeAdicionaUmaEstacao(self):
        self.estacao = Estacao("001", "Estacao SUN", 1000, 8, "Sala 101")
        self.estacao.localizacao |should| equal_to("Sala 101")
        self.estacao.codPatrimonio |should| equal_to("001")
        self.estacao.descricao |should| equal_to("Estacao SUN")
        self.estacao.hd |should| equal_to(1000)
        self.estacao.memoria |should| equal_to(8)
        self.estacao.todasEstacoes[0].localizacao |should| equal_to("Sala 101")
        
