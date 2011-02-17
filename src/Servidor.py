'''
Created on 15/02/2011

@author: Michael
'''
from Micro import Micro
class Servidor(Micro):
    todosServidores = []
    impressoras = []
    def __init__(self, codPatrimonio, descricao, hd, memoria, tamanhoBuffer, quantidadeBuffer):
        Micro.__init__(self, codPatrimonio, descricao, hd, memoria)
        self.tamanhoBuffer = tamanhoBuffer
        self.quantidadeBuffer = quantidadeBuffer
        self.armazenaServidores(self)
        
    def armazenaServidores(self, servidor):
        self.todosServidores.append(servidor)
        
    def armazenaImpressorasConectadas(self, codImpressora):
        if len(self.impressoras) <= 2:
            self.impressoras.append(codImpressora)
        else:
            print "Para este servidor ja existem 3 impressoras cadastradas!"
    
    def recuperaImpressorasConectadas(self):
        return self.impressoras
        