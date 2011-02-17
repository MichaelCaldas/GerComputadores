'''
Created on 15/02/2011

@author: Michael
'''
from Impressora import Impressora
from should_dsl.dsl import should
from should_dsl.matchers import equal_to
import unittest

class Teste_Impressora(unittest.TestCase):
    
    def testeAdicionaUmaImpressora(self):
        self.impressora = Impressora("001", "HP 2300", 500, "IBM Server")
        self.impressora.codPatrimonio |should| equal_to("001")
        self.impressora.descricao |should| equal_to("HP 2300")
        self.impressora.velocidade |should| equal_to(500)
        self.impressora.todasImpressoras[0].codPatrimonio |should| equal_to("001")