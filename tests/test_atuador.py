import unittest
from atuadores import Atuador  # Ajuste o import conforme seu projeto
import json
from constantes import CONFIG

class TestAtuador(unittest.TestCase):

    def setUp(self):
        # Aqui instanciamos normalmente, usando o arquivo CONFIG real
        self.atuador = Atuador()
        
    def test_arquivo_config_carregado(self):
        # Verifica se o atributo COMANDOS existe e não é None
        self.assertIsNotNone(self.atuador.COMANDOS)

        # Verifica se as chaves principais existem
        self.assertIn("acoes", self.atuador.COMANDOS)
        self.assertIn("cenas", self.atuador.COMANDOS)

        # Além disso, verifica se o conteúdo está igual ao do arquivo JSON
        with open(CONFIG, "r", encoding="utf-8") as f:
            config_arquivo = json.load(f)

        self.assertEqual(self.atuador.COMANDOS, config_arquivo)
        
    def test_validar_comando_valido(self):
        comando = ["ligar", "carro"]
        self.atuador.validar_comando(comando)
        self.assertTrue(self.atuador.comando_validado)
        self.assertEqual(self.atuador.acao, "ligar")
        self.assertEqual(self.atuador.objeto, "carro")

    def test_validar_comando_invalido(self):
        comando = ["acender", "luz"]
        self.atuador.validar_comando(comando)
        self.assertFalse(self.atuador.comando_validado)
        self.assertFalse(self.atuador.cena_validada)

    def test_validar_cena_valida(self):
        comando = ["revisão"]
        self.atuador.validar_comando(comando)
        self.assertTrue(self.atuador.cena_validada)
        self.assertEqual(self.atuador.cena, "revisão")
        self.assertEqual(len(self.atuador.acoes), 2)

if __name__ == "__main__":
    unittest.main()
