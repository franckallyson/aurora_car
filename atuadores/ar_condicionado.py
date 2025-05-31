
import json
from constantes import CONFIG
from assistente_fala import AssistenteFala

class ArCondicionado():
    
    def __init__(self):
        self.acoes_disponiveis = {
            "ativar": self.ativar,
            "desativar": self.desativar
        }
    
        self.assistente_fala = AssistenteFala()
        
    def iniciar(self):
        """Inicia o ArCondicionado"""
        print(f"[ArCondicionado] Preparando o Ar Condicionado Inteligente!")
    
    
    def atuar(self, acao, objeto):
        if acao in self.acoes_disponiveis:
            return self.acoes_disponiveis[acao](objeto)
        else:
            print(f"[ArCondicionado] Ação '{acao}' não suportada pelo atuador Ar Condicionado.")
    
    
    def ativar(self, objeto):
        if objeto == "ar":
            print("[ArCondicionado] Ar Condicionado ativado com sucesso.")
            self.assistente_fala.comando_executado("ar_condicionado.mp3")
            
        else:
            print(f"[ArCondicionado] Objeto '{objeto}' não reconhecido para a ação 'ligar'.")

    def desativar(self, objeto):
        if objeto == "ar":
            print("[ArCondicionado] Desligando o Ar condicionado...")
        else:
            print(f"[ArCondicionado] Objeto '{objeto}' não reconhecido para a ação 'desligar'.")