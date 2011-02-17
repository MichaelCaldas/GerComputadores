'''
Created on 16/02/2011

@author: Karol
'''
from Micro import Micro

class Estacao(Micro):
    todasEstacoes = []
    def __init__(self, micro, localizacao):
        self.micro = micro
        self.localizacao = localizacao
        self.armazenaEstacoes(self)
        
    def armazenaEstacoes(self, estacao):
        self.todasEstacoes.append(estacao)