'''
Created on 16/02/2011

@author: Karolyne
'''

class Impressao():
    todasImpressoes = []
    
    def __init__(self, arquivo, usuario, impressora, numeroCopias):
        self.arquivo = arquivo
        self.usuario = usuario
        self.impressora = impressora
        self.numeroCopias = numeroCopias
        self.armazenaImpressoes(self)
        
    def armazenaImpressoes(self, impressao):
        self.todasImpressoes.append(impressao)