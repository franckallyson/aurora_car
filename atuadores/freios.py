
import json
from constantes import CONFIG
from time import sleep
from assistente_fala import AssistenteFala

class Freios():
    
    def __init__(self):    
        self.acoes_disponiveis = {
            "verificar": self.verificar,
        }
            
        self.assistente_fala = AssistenteFala()
    
    def iniciar(self):
        """Inicia os Freios"""
        print(f"[FREIOS] Preparando os freios inteligentes!")
        
    
    def atuar(self, acao, objeto):
        if acao in self.acoes_disponiveis:
            return self.acoes_disponiveis[acao](objeto)
        else:
            print(f"[FREIOS] Ação '{acao}' não suportada pelo atuador Freios.")
    
    
    def verificar(self, objeto):
        if objeto in ["freios", "freio"]:
            print("[FREIOS] Verificando o estado dos freios...")
            self.assistente_fala.comando_executado("freios.mp3")
            print("[FREIOS] Freios verificados! Tudo OK!")
        else:
            print(f"[FREIOS] Objeto '{objeto}' não reconhecido para a ação 'verificar'.")

