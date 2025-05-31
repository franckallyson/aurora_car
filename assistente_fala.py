import pygame
import time

class AssistenteFala:
    def __init__(self):
        pygame.mixer.init()
        self.caminho_audios = 'audios_respostas/'
    
    def reproduzir_audio(self, nome_arquivo):
        caminho = self.caminho_audios + nome_arquivo
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    # Métodos específicos
    def em_que_posso_ajudar(self):
        self.reproduzir_audio('em_que_posso_ajudar.mp3')
    
    def desculpe_nao_entendi(self):
        self.reproduzir_audio('desculpe_nao_entendi.mp3')

    def comando_executado(self, arquivo):
        self.reproduzir_audio(arquivo)