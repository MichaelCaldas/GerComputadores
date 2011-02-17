'''
Created on 15/02/2011

@author: Michael
'''
from Micro import Micro
class Servidor(Micro):
    todosServidores = []
    
    def __init__(self, codPatrimonio, descricao, hd, memoria, tamanhoBuffer, quantidadeBuffer):
        Micro.__init__(self, codPatrimonio, descricao, hd, memoria)
        self.tamanhoBuffer = tamanhoBuffer
        self.quantidadeBuffer = quantidadeBuffer
        self.armazenaServidores(self)
        
    def armazenaServidores(self, servidor):
        self.todosServidores.append(servidor)