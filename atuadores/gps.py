
import json
from constantes import CONFIG
from time import sleep
from assistente_fala import AssistenteFala
from escutador import EscutadorComando


class GPS():
    
    def __init__(self):    
        self.acoes_disponiveis = {
            "configurar": self.configurar,
        }
            
        self.assistente_fala = AssistenteFala()
        self.escutador_comando = EscutadorComando()
    def iniciar(self):
        """Inicia a GPS"""
        print(f"[GPS] Preparando o GPS inteligente!")
        
    
    def atuar(self, acao, objeto):
        if acao in self.acoes_disponiveis:
            return self.acoes_disponiveis[acao](objeto)
        else:
            print(f"[GPS] Ação '{acao}' não suportada pelo atuador GPS.")
    
    
    def configurar(self, objeto):
        if objeto == "rota":
            print("[GPS] configurando rota...")
            self.assistente_fala.comando_executado("para_onde_deseja_ir.mp3")
            self.escutador_comando.ouvir_comando(aguardar=7)
            self.assistente_fala.comando_executado("configurando_rota.mp3")
            print("[GPS] GPS verificada! Tudo OK!")
        else:
            print(f"[GPS] Objeto '{objeto}' não reconhecido para a ação 'configurar'.")
