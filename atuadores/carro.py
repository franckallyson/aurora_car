
import json
from constantes import CONFIG
from assistente_fala import AssistenteFala

class Carro():
    
    def __init__(self):
        self.acoes_disponiveis = {
            "ligar": self.ligar,
            "desligar": self.desligar
        }

        self.ligado = False
        self.assistente_fala = AssistenteFala()
    def iniciar(self):
        """Inicia o carro"""
        print(f"[CARRO] Girando a chave e aguardando incialização do carro!")
        
    
    
    def atuar(self, acao, objeto):
        if acao in self.acoes_disponiveis:
            return self.acoes_disponiveis[acao](objeto)
        else:
            print(f"[CARRO] Ação '{acao}' não suportada pelo atuador Carro.")
    
    
    def ligar(self, objeto):
        if objeto == "carro":
            if self.ligado:
                print("[CARRO] Carro já está ligado.")
            else:
                print("[CARRO] Carro ligado com sucesso.")
                self.assistente_fala.comando_executado("ligar_carro.mp3")
                self.ligado = True
        else:
            print(f"[CARRO] Objeto '{objeto}' não reconhecido para a ação 'ligar'.")

    def desligar(self, objeto):
        if objeto == "carro":
            if not self.ligado:
                print("[CARRO] Carro já está desligado!")
            else:
                print("[CARRO] Desligando o carro...")
                self.assistente_fala.comando_executado("desligar_carro.mp3")
                self.ligado = False
        else:
            print(f"[CARRO] Objeto '{objeto}' não reconhecido para a ação 'desligar'.")