import unittest
from unittest.mock import MagicMock, patch
from atuadores import Carro


class TestCarro(unittest.TestCase):
    
    @patch('atuadores.carro.AssistenteFala')
    def setUp(self, mock_assistente):
        self.carro = Carro()
        self.mock_assistente = mock_assistente.return_value

    def test_inicial_estado_desligado(self):
        self.assertFalse(self.carro.ligado)

    def test_ligar_carro(self):
        self.carro.atuar("ligar", "carro")
        self.assertTrue(self.carro.ligado)
        self.mock_assistente.comando_executado.assert_called_once_with("ligar_carro.mp3")

    def test_ligar_carro_ja_ligado(self):
        self.carro.ligado = True
        self.carro.atuar("ligar", "carro")
        self.assertTrue(self.carro.ligado)
        # Mesmo que já esteja ligado, não executa novamente o comando de áudio
        self.mock_assistente.comando_executado.assert_not_called()

    def test_desligar_carro(self):
        self.carro.ligado = True
        self.carro.atuar("desligar", "carro")
        self.assertFalse(self.carro.ligado)
        self.mock_assistente.comando_executado.assert_called_once_with("desligar_carro.mp3")

    def test_desligar_carro_ja_desligado(self):
        self.carro.ligado = False
        self.carro.atuar("desligar", "carro")
        self.assertFalse(self.carro.ligado)
        self.mock_assistente.comando_executado.assert_not_called()

    def test_acao_nao_suportada(self):
        resultado = self.carro.atuar("voar", "carro")
        self.assertIsNone(resultado)

    def test_objeto_invalido(self):
        self.carro.atuar("ligar", "avião")
        self.assertFalse(self.carro.ligado)
        self.mock_assistente.comando_executado.assert_not_called()


if __name__ == '__main__':
    unittest.main()
