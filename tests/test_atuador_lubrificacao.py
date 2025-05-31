import unittest
from unittest.mock import patch
from atuadores import Lubrificacao


class TestLubrificacao(unittest.TestCase):

    @patch('atuadores.lubrificacao.AssistenteFala')
    def setUp(self, mock_assistente_fala):
        self.mock_assistente = mock_assistente_fala.return_value
        self.lubrificacao = Lubrificacao()

    def test_iniciar(self):
        self.lubrificacao.iniciar()

    def test_verificar_lubrificacao(self):
        self.lubrificacao.verificar("lubrificação")

        self.mock_assistente.comando_executado.assert_called_once_with("verificacao.mp3")

    def test_verificar_objeto_invalido(self):
        self.lubrificacao.verificar("motor")

        self.mock_assistente.comando_executado.assert_not_called()

    def test_atuar_acao_existente(self):
        self.lubrificacao.atuar("verificar", "lubrificação")

        self.mock_assistente.comando_executado.assert_called_once_with("verificacao.mp3")

    def test_atuar_acao_invalida(self):
        self.lubrificacao.atuar("limpar", "lubrificação")

        self.mock_assistente.comando_executado.assert_not_called()


if __name__ == "__main__":
    unittest.main()
