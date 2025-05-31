import unittest
from processamento import ProcessadorTranscricao, ProcessadorFala

class TestReconhecimentoComandos(unittest.TestCase):
    
    def setUp(self):
        self.transcritor = ProcessadorTranscricao()
        self.processador_fala = ProcessadorFala()
        
    def test_aurora(self):
        caminho_arquivo = 'tests/archives/aurora.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "aurora")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")
    
    
    def test_ligar_carro(self):
        caminho_arquivo = 'tests/archives/ligar_carro.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "ligar carro")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")
    
    def test_desligar_carro(self):
        caminho_arquivo = 'tests/archives/desligar_carro.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "desligar carro")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")
    
    def test_verificar_freios(self):
        caminho_arquivo = 'tests/archives/verificar_freios.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "verificar freios")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")
        
    def test_verificar_lubrificacao(self):
        caminho_arquivo = 'tests/archives/verificar_lubrificacao.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "verificar lubrificação")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")
        
    def test_ativar_ar_condicionado(self):
        caminho_arquivo = 'tests/archives/ativar_ar_condicionado.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "ativar ar condicionado")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")
        
    def test_desativar_ar_condicionado(self):
        caminho_arquivo = 'tests/archives/desativar_ar_condicionado.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "desativar ar condicionado")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")
        
    def test_configurar_rota(self):
        caminho_arquivo = 'tests/archives/configurar_rota.wav'

        fala = self.processador_fala.carregar_fala(caminho_arquivo)
        transcricao = self.transcritor.transcrever_fala(fala)

        self.assertIsInstance(transcricao, str)
        self.assertEqual(transcricao, "configurar rota")
        self.assertGreater(len(transcricao), 0, "A transcrição deveria ter conteúdo")
    