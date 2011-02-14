'''
Created on 12/02/2011

@author: Karolyne
'''
class Usuario():
    def __init__(self, nomeGuerra, senha):
      self.nomeGuerra = nomeGuerra
      self.senha = senha  
        
    def setNomeGuerra(self, nomeGuerra):
        self.nomeGuerra = nomeGuerra
        
    def getNomeGuerra(self):
        return self.nomeGuerra
    
    def setSenha(self, senha):
        self.senha = senha
        
    def getSenha(self):
        return self.senha
