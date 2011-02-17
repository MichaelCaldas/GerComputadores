'''
Created on 16/02/2011

@author: Karolyne
'''
from Micro import Micro

class Estacao(Micro):
    todasEstacoes = []
    def __init__(self, codPatrimonio, descricao, hd, memoria, localizacao):
        Micro.__init__(self, codPatrimonio, descricao, hd, memoria)
        self.localizacao = localizacao
        self.armazenaEstacoes(self)
        
    def armazenaEstacoes(self, estacao):
        self.todasEstacoes.append(estacao)