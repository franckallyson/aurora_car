import pyaudio

PALAVRA_ATIVACAO = "aurora"
FORMATO = pyaudio.paInt16
AMOSTRAS = 1024
CANAIS = 1
TEMPO_DE_GRAVACAO = 5
CAMINHO_AUDIO_FALA = "C:\\Users\\franc\\OneDrive\\Documentos\\Franck\\Faculdade\\IFBA\\IA\\assistente virtual\\temp"


IDIOMA_CORPUS = "portuguese"
CONFIG = "C:\\Users\\franc\\OneDrive\\Documentos\\Franck\\Faculdade\\IFBA\\IA\\assistente virtual\\config.json"


# Para incialização do modelo (inicializador_modelos.py)
MODELO = "lgris/wav2vec2-large-xlsr-open-brazilian-portuguese-v2"

# Para transcricao (transcritor.py)
TAXA_AMOSTRAGEM = 16_000