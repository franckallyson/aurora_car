import json

from .ar_condicionado import ArCondicionado
from .carro import Carro
from .freios import Freios
from .lubrificacao import Lubrificacao
from .gps import GPS
from constantes import CONFIG
from threading import Thread
from assistente_fala import AssistenteFala

class Atuador():
    """
        Essa clase irá controlar a atuação do sistema com base em um comando fornecido.\n
        Ela valida se o comando fornecido se encontra no arquivo de configurações.\n
        Se validado, dispara a atuação para o Objeto referente. 
    """
    def __init__(self):
        """Inicia o atuador, puxando o arquivo de configurações e setando as variáveis principais."""
        try:
            with open(CONFIG, "r", encoding='utf-8') as arquivo:
                self.COMANDOS = json.load(arquivo)
                arquivo.close()
            
            self.comando_validado = False
            self.acao = None
            self.objeto = None
            
            self.cena_validada = False
            self.acoes = []
            self.cena = None
            
            self.assistente_fala = AssistenteFala()
        except Exception as e:
            print(f"erro carregando a configuração: {str(e)}")
            
        self.atuadores_disponiveis = self.__configurar_atuadores()
        
    
    def atuar(self):
        """Atua sobre o comando/cena validado"""
        if self.comando_validado:
            print(f"executando {self.acao} sobre {self.objeto}")

            for atuador in self.atuadores_disponiveis:
                atuacao = Thread(target=atuador["atuacao"], args=[self.acao, self.objeto])
                atuacao.start()
            
            self.comando_validado = False
        elif self.cena_validada:
            print(f"executando {self.acoes} na cena {self.cena}")

            for acao in self.acoes:
                for atuador in self.atuadores_disponiveis:
                    atuacao = Thread(target=atuador["atuacao"], args=[acao["nome"], acao["objeto"]])
                    atuacao.start()
        else:
            self.assistente_fala.desculpe_nao_entendi()
            print("Comando não validado!")
            
            
    def validar_comando(self, comando):
        """
        Valida o comando ou a cena recebida.

        args:
            comando (list): Lista contendo o comando a ser validado.
        """
        self.__validar_comando_unico(comando)
        if not self.comando_validado:
            self.__validar_cena(comando)    
    
    def __validar_comando_unico(self, comando):
        """Valida um comando único, existente na chave 'acoes' do arquivo config"""
        valido, acao, objeto = False, None, None
    
        if len(comando) >= 2:
            acao = comando[0]
            objeto = comando[1]
            
            for acao_prevista in self.COMANDOS["acoes"]:
                if acao == acao_prevista["nome"]:
                    if objeto in acao_prevista["objetos"]:
                        valido = True

                        break

        if valido:
            self.comando_validado = True
            self.acao = acao
            self.objeto = objeto
            
    
    def __validar_cena(self, comando):
        """Valida uma cena, existente na chave 'cenas' do arquivo config"""
        valido, acoes, cena = False, [], None

        if len(comando) == 1:
            cena = comando[0]

            for cena_prevista in self.COMANDOS["cenas"]:
                if cena == cena_prevista["nome"]:
                    valido = True
                    acoes = cena_prevista["acoes"]

                    break

        if valido:
            self.cena_validada = True
            self.acoes = acoes
            self.cena = cena
            
    
    def __configurar_atuadores(self):
        """Define os atuadores ativos no sistema e suas respectivas funções de iniciar e atuar"""
        atuadores_disponiveis = [
            {
                "nome": "carro",
                "inicializacao": Carro().iniciar,
                "atuacao": Carro().atuar
            },
            {
                "nome": "freios",
                "inicializacao": Freios().iniciar,
                "atuacao": Freios().atuar,
            },
            {
                "nome": "lubrificacao",
                "inicializacao": Lubrificacao().iniciar,
                "atuacao": Lubrificacao().atuar,
            },
            {
                "nome": "ar_condicionado",
                "inicializacao": ArCondicionado().iniciar,
                "atuacao": ArCondicionado().atuar,
            },
            {
                "nome": "gps",
                "inicializacao": GPS().iniciar,
                "atuacao": GPS().atuar
            }
        ]

        for atuador in atuadores_disponiveis:
            inicializacao = atuador["inicializacao"]
            inicializacao()
        
        return atuadores_disponiveis
        