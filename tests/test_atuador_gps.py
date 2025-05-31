import unittest
from unittest.mock import patch, MagicMock
from atuadores import GPS


class TestGPS(unittest.TestCase):

    @patch('atuadores.gps.EscutadorComando')
    @patch('atuadores.gps.AssistenteFala')
    def setUp(self, mock_assistente_fala, mock_escutador):
        self.mock_assistente = mock_assistente_fala.return_value
        self.mock_escutador = mock_escutador.return_value
        self.gps = GPS()

    def test_iniciar(self):
        self.gps.iniciar()

    def test_configurar_rota(self):
        self.gps.configurar("rota")

        # Verifica se chamou os áudios na ordem correta
        self.mock_assistente.comando_executado.assert_any_call("para_onde_deseja_ir.mp3")
        self.mock_assistente.comando_executado.assert_any_call("configurando_rota.mp3")

        # Verifica se o escutador foi chamado
        self.mock_escutador.ouvir_comando.assert_called_once_with(aguardar=7)

    def test_configurar_objeto_invalido(self):
        self.gps.configurar("porta")

        # Não deve tocar nenhum áudio nem ouvir comando
        self.mock_assistente.comando_executado.assert_not_called()
        self.mock_escutador.ouvir_comando.assert_not_called()

    def test_atuar_acao_existente(self):
        self.gps.atuar("configurar", "rota")

        self.mock_assistente.comando_executado.assert_any_call("para_onde_deseja_ir.mp3")
        self.mock_assistente.comando_executado.assert_any_call("configurando_rota.mp3")
        self.mock_escutador.ouvir_comando.assert_called_once_with(aguardar=7)

    def test_atuar_acao_nao_existente(self):
        self.gps.atuar("ligar", "rota")

        # Nenhum áudio ou escuta deve acontecer
        self.mock_assistente.comando_executado.assert_not_called()
        self.mock_escutador.ouvir_comando.assert_not_called()


if __name__ == "__main__":
    unittest.main()
