
import json
from constantes import CONFIG
from time import sleep
from assistente_fala import AssistenteFala

class Lubrificacao():
    
    def __init__(self):    
        self.acoes_disponiveis = {
            "verificar": self.verificar,
        }
            
        self.assistente_fala = AssistenteFala()
    
    def iniciar(self):
        """Inicia a Lubrificação"""
        print(f"[LUBRIFICAÇÃO] Preparando a lubrificação inteligente!")
        
    
    def atuar(self, acao, objeto):
        if acao in self.acoes_disponiveis:
            return self.acoes_disponiveis[acao](objeto)
        else:
            print(f"[LUBRIFICAÇÃO] Ação '{acao}' não suportada pelo atuador Lubrificacao.")
    
    
    def verificar(self, objeto):
        if objeto == "lubrificação":
            print("[LUBRIFICAÇÃO] Verificando a lubrificação do veículo...")
            self.assistente_fala.comando_executado("verificacao.mp3")
            print("[LUBRIFICAÇÃO] Lubrificação verificada! Tudo OK!")
        else:
            print(f"[LUBRIFICAÇÃO] Objeto '{objeto}' não reconhecido para a ação 'verificar'.")
