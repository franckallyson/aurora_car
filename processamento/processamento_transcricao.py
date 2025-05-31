from processamento.inicializador_modelos import *
from constantes import *
import torch
from nltk import word_tokenize, corpus


class ProcessadorTranscricao():
    
    def __init__(self):
        dispositivo = "cuda:0" if torch.cuda.is_available() else "cpu"
        
        self.iniciado, self.processador, self.modelo = iniciar_modelo(MODELO, dispositivo)
        self.palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))


    def transcrever_fala(self, fala, dispositivo="cpu"):
        resultado = self.processador(fala, return_tensors="pt", sampling_rate=TAXA_AMOSTRAGEM).input_values.to(dispositivo)
        resultado = self.modelo(resultado).logits

        predicao = torch.argmax(resultado, dim=-1)
        transcricao = self.processador.batch_decode(predicao)[0]

        return transcricao.lower()

    def processar_transcricao(self, transcricao):
        comando = []

        tokens = word_tokenize(transcricao)
        for token in tokens:
            if token not in self.palavras_de_parada:
                comando.append(token)

        return comando
