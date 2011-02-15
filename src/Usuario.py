'''
Created on 12/02/2011

@author: Karolyne
'''
from ArmazenaUsuario import ArmazenaUsuario

class Usuario():
    todosUsuarios = []
    
    def __init__(self, nomeGuerra, senha):
        self.nomeGuerra = nomeGuerra
        self.senha = senha
        #ArmazenaUsuario(self)
        self.armazenaUsuarios(self)
        
    def armazenaUsuarios(self, usuario):
        self.todosUsuarios.append(usuario)