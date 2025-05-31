import unittest
from unittest.mock import patch
from atuadores import ArCondicionado


class TestArCondicionado(unittest.TestCase):

    @patch('atuadores.ar_condicionado.AssistenteFala')
    def setUp(self, mock_assistente_fala):
        self.mock_assistente = mock_assistente_fala.return_value
        self.ar = ArCondicionado()

    def test_iniciar(self):
        self.ar.iniciar()

    def test_ativar_objeto_correto(self):
        self.ar.ativar("ar")
        self.mock_assistente.comando_executado.assert_called_once_with("ar_condicionado.mp3")

    def test_ativar_objeto_errado(self):
        self.ar.ativar("ventilador")
        self.mock_assistente.comando_executado.assert_not_called()

    def test_desativar_objeto_correto(self):
        self.ar.desativar("ar")
        # Nenhum comando de áudio para desativar no seu código, então só confere a saída (visual)

    def test_desativar_objeto_errado(self):
        self.ar.desativar("ventilador")

    def test_atuar_acao_existente(self):
        self.ar.atuar("ativar", "ar")
        self.mock_assistente.comando_executado.assert_called_with("ar_condicionado.mp3")

    def test_atuar_acao_invalida(self):
        self.ar.atuar("ligar", "ar")
        self.mock_assistente.comando_executado.assert_not_called()


if __name__ == "__main__":
    unittest.main()
