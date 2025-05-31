from constantes import *
import secrets
import wave 
from nltk import word_tokenize, corpus
import pyaudio
import torchaudio
import torch


class ProcessadorFala():
    
    def __init__(self):
        self.gravador = pyaudio.PyAudio()
    
    def carregar_fala(self, caminho_audio):
        
        audio, amostragem = torchaudio.load(caminho_audio)
        
        if audio.shape[0] > 1:
            audio = torch.mean(audio, dim=0, keepdim=True)

        adaptador_amostragem = torchaudio.transforms.Resample(amostragem, TAXA_AMOSTRAGEM)
        audio = adaptador_amostragem(audio)

        return audio.squeeze()

    def capturar_fala(self, tempo=None):
        tempo_gravacao = tempo if tempo else TEMPO_DE_GRAVACAO
        gravacao = self.gravador.open(format=FORMATO, channels=CANAIS, rate=TAXA_AMOSTRAGEM, input=True, frames_per_buffer=AMOSTRAS)

        print("fale alguma coisa")

        fala = []
        for _ in range(0, int(TAXA_AMOSTRAGEM / AMOSTRAS * tempo_gravacao)):
            fala.append(gravacao.read(AMOSTRAS))

        gravacao.stop_stream()
        gravacao.close()

        return fala

    def gravar_fala(self, fala):
        gravada, arquivo = False, f"{CAMINHO_AUDIO_FALA}/{secrets.token_hex(32)}.wav"

        try:
            wav = wave.open(arquivo, "wb")
            wav.setnchannels(CANAIS)
            wav.setsampwidth(self.gravador.get_sample_size(FORMATO))
            wav.setframerate(TAXA_AMOSTRAGEM)
            wav.writeframes(b"".join(fala))
            wav.close()

            gravada = True
        except Exception as e:
            print(f"ocorreu um erro gravando fala: {str(e)}")

        return gravada, arquivo

"""
def processar_transcricao(transcricao, palavras_de_parada):
    comando = []

    tokens = word_tokenize(transcricao)
    for token in tokens:
        if token not in palavras_de_parada:
            comando.append(token)

    return comando"""