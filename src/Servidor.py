'''
Created on 15/02/2011

@author: Michael
'''
class Servidor():
    todosServidores = []
    
    def __init__(self, tamanhoBuffer, quantidadeBuffer):
        self.tamanhoBuffer = tamanhoBuffer
        self.quantidadeBuffer = quantidadeBuffer
        self.armazenaServidores(self)
        
    def armazenaServidores(self, servidor):
        self.todosServidores.append(servidor)