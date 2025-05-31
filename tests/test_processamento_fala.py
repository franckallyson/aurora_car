import unittest
from unittest.mock import patch, MagicMock, mock_open
import torch
import os

from processamento import ProcessadorFala

class TestProcessadorFala(unittest.TestCase):
    
    @patch('torchaudio.load')
    @patch('torchaudio.transforms.Resample')
    def test_carregar_fala(self, mock_resample, mock_load):
        # Simula o áudio carregado
        mock_load.return_value = (torch.rand(2, 16000), 44100)

        # Mock do resample
        mock_resample.return_value = MagicMock(side_effect=lambda x: x)

        processador = ProcessadorFala()
        resultado = processador.carregar_fala('teste.wav')

        # Verifica se retorna um tensor unidimensional
        self.assertTrue(isinstance(resultado, torch.Tensor))
        self.assertEqual(len(resultado.shape), 1)

        # Verifica se o resample foi chamado
        mock_resample.assert_called_once_with(44100, 16000)

    @patch('pyaudio.PyAudio.open')
    def test_capturar_fala(self, mock_open):
        # Mocka o stream de áudio
        stream_mock = MagicMock()
        stream_mock.read.return_value = b'audio'

        mock_open.return_value = stream_mock

        processador = ProcessadorFala()
        resultado = processador.capturar_fala(tempo=1)  # 1 segundo para simplificar

        # Verifica se a captura retornou uma lista de bytes
        self.assertIsInstance(resultado, list)
        self.assertTrue(all(isinstance(chunk, bytes) for chunk in resultado))

        stream_mock.read.assert_called()

    @patch('wave.open')
    @patch('pyaudio.PyAudio.get_sample_size')
    def test_gravar_fala(self, mock_sample_size, mock_wave_open):
        mock_sample_size.return_value = 2  # tamanho qualquer
        wave_mock = MagicMock()
        mock_wave_open.return_value = wave_mock

        processador = ProcessadorFala()
        fala = [b'audio1', b'audio2']

        gravado, arquivo = processador.gravar_fala(fala)

        self.assertTrue(gravado)
        self.assertTrue(arquivo.endswith('.wav'))

        wave_mock.setnchannels.assert_called()
        wave_mock.setsampwidth.assert_called()
        wave_mock.setframerate.assert_called()
        wave_mock.writeframes.assert_called_with(b''.join(fala))
        wave_mock.close.assert_called()

if __name__ == '__main__':
    unittest.main()
