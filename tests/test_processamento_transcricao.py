import unittest
import torch
from processamento import ProcessadorTranscricao, ProcessadorFala


class TestProcessadorTranscricaoReal(unittest.TestCase):
    
    def setUp(self):
        self.transcritor = ProcessadorTranscricao()
        self.processador_fala = ProcessadorFala()

    def test_modelo_iniciado(self):
        self.assertTrue(self.transcritor.iniciado)
        
    def test_carregamento_palavras_de_parada(self):
        self.assertIsNotNone(self.transcritor.palavras_de_parada)
        
    def test_transcrever_fala_de_arquivo(self):
        caminho_arquivo = 'tests/archives/teste.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "teste")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")

    def test_processar_transcricao(self):
        transcricao = "ligar o carro agora"
        resultado = self.transcritor.processar_transcricao(transcricao)

        self.assertIn('ligar', resultado)
        self.assertIn('carro', resultado)
        self.assertNotIn('o', resultado)  # Verifica se a palavra de parada foi removida


if __name__ == '__main__':
    unittest.main()
