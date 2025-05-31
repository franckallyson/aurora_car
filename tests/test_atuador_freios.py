import unittest
from unittest.mock import patch, MagicMock
from atuadores import Freios


class TestFreios(unittest.TestCase):

    @patch('atuadores.freios.AssistenteFala')
    def setUp(self, mock_assistente):
        self.mock_assistente = mock_assistente.return_value
        self.freios = Freios()

    def test_iniciar(self):
        # Apenas verifica se o método executa sem erro
        self.freios.iniciar()

    def test_verificar_freios(self):
        self.freios.verificar("freios")

        # Verifica se comando_executado foi chamado com o áudio correto
        self.mock_assistente.comando_executado.assert_called_once_with("freios.mp3")

    def test_verificar_freio_singular(self):
        self.freios.verificar("freio")

        self.mock_assistente.comando_executado.assert_called_once_with("freios.mp3")

    def test_verificar_objeto_invalido(self):
        self.freios.verificar("porta")

        # Não deve tocar nenhum áudio, pois é objeto inválido
        self.mock_assistente.comando_executado.assert_not_called()

    def test_atuar_acao_existente(self):
        self.freios.atuar("verificar", "freios")

        self.mock_assistente.comando_executado.assert_called_once_with("freios.mp3")

    def test_atuar_acao_nao_existente(self):
        self.freios.atuar("ligar", "freios")

        # Não deve executar nenhum áudio, pois ação não existe
        self.mock_assistente.comando_executado.assert_not_called()


if __name__ == "__main__":
    unittest.main()
