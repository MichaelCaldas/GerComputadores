'''
Created on 12/02/2011

@author: Karolyne
'''

from Usuario import Usuario
from should_dsl.dsl import should
from should_dsl.matchers import be, equal_to
import unittest

class Teste_Usuario(unittest.TestCase):

    def setUp(self):
        self.usuario = Usuario("Michael", 123456)
        self.usuario.nomeGuerra |should| equal_to("Michael")
        self.usuario.senha |should| equal_to(123456)
               
    def teste_get_nome_guerra(self):
        self.usuario.setNomeGuerra("Michael")
        self.usuario.getNomeGuerra() |should| be("Michael")
        
    def teste_get_senha(self):
        self.usuario.setSenha(123456)
        self.usuario.getSenha() |should| be(123456)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()