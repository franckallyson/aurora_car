import threading
import queue
import time
import os
import torch
from processamento.processamento_fala import *
from processamento.processamento_transcricao import *
from assistente_fala import AssistenteFala
import pygame

class EscutadorAtivacao(threading.Thread):
    def __init__(self, fila_ativacao):
        super().__init__()
        self.fila_ativacao = fila_ativacao
        self.processador_fala = ProcessadorFala()
        self.processador_transcricao = ProcessadorTranscricao()
        self.dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.executando = True
        self.palavra_ativacao = "aurora"
        self.assistente_fala = AssistenteFala()

        
    def run(self):
        print("👂 Escutando palavra de ativação...")

        while self.executando:
            try:
                if self.fila_ativacao.empty():
                    fala = self.processador_fala.capturar_fala(tempo=2)  # gravações curtas
                    gravado, arquivo = self.processador_fala.gravar_fala(fala)

                    if gravado:
                        audio = self.processador_fala.carregar_fala(arquivo)
                        transcricao = self.processador_transcricao.transcrever_fala(audio, self.dispositivo)
                        os.remove(arquivo)

                        print(f"📝 Capturado: {transcricao}")

                        if self.palavra_ativacao.lower() in transcricao:
                            print("🚗 Palavra de ativação detectada!")
                            self.assistente_fala.em_que_posso_ajudar()
                            self.fila_ativacao.put(True)

                time.sleep(0.5)  # pequena pausa para não sobrecarregar

            except Exception as e:
                print(f"❌ Erro na escuta de ativação: {e}")

    def parar(self):
        self.executando = False


class EscutadorComando:
    def __init__(self):
        self.processador_fala = ProcessadorFala()
        self.processador_transcricao = ProcessadorTranscricao()
        self.dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"
        

    def ouvir_comando(self, aguardar=5):
        tempo = aguardar
        print("🎙️ Ouvindo comando...")
        fala = self.processador_fala.capturar_fala(tempo=tempo)  # tempo maior para o comando
        gravado, arquivo = self.processador_fala.gravar_fala(fala)

        if gravado:
            audio = self.processador_fala.carregar_fala(arquivo)
            transcricao = self.processador_transcricao.transcrever_fala(audio, self.dispositivo)
            os.remove(arquivo)

            comando = self.processador_transcricao.processar_transcricao(transcricao)
            
            print(f"🗣️ Comando detectado: {comando}")
            return comando
        return None
