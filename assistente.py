

from atuadores import Atuador
from constantes import *

from flask import Flask, send_from_directory, request, jsonify
from processamento.inicializador_modelos import *
from nltk import corpus
from processamento.processamento_transcricao import *
from processamento.processamento_fala import *
from escutador import *


import json
import os
import pyaudio
import queue
import time


# linha de comando
def ativar_assistente():
    fila_ativacao = queue.Queue()

    escutador_ativacao = EscutadorAtivacao(fila_ativacao)
    escutador_ativacao.start()

    escutador_comando = EscutadorComando()
    atuador = Atuador()

    try:
        while True:
            if not fila_ativacao.empty():

                comando = escutador_comando.ouvir_comando()

                if comando:
                    atuador.validar_comando(comando)
                    validado = False
                    if atuador.cena_validada or atuador.comando_validado:
                        validado = True
                    atuador.atuar()
                    
                    # Faço isso pois quando o atuador atua, ele reseta a validação pra não afetar o próximo comando.
                    # Antes de atuar, eu só testo se validou e guardo na flag, pra não voltar pra ativação antes de atuar.
                    if validado:
                        fila_ativacao.get()
                        print("🔁 Retornando para modo de ativação...")
                

            time.sleep(1)

    except KeyboardInterrupt:
        print("🛑 Encerrando assistente...")
        escutador_ativacao.parar()
        escutador_ativacao.join()

        

# 2. através de uma aplicação web acessível por browsers
servico = Flask("assistente", static_folder="public")

@servico.get("/")
def get_pagina():
    return send_from_directory("public", "index.html")

@servico.get("/<path:path>")
def get_caminho_estatico(path):
    return send_from_directory("public", path)

@servico.post("/reconhecer_comando")
def reconhecer_comando():
    if "audio" not in request.files:
        return jsonify({"erro": "nenhum foi enviado"}), 400
    
    arquivo = request.files["audio"]
    
    caminho_arquivo = os.path.join(CAMINHO_AUDIO_FALA, f"{secrets.token_hex(32).lower()}.wav")
    arquivo.save(caminho_arquivo)

    try:
        processador_fala = ProcessadorFala()
        processador_transcricao = ProcessadorTranscricao()
        
        audio = processador_fala.carregar_fala(caminho_arquivo)
        transcricao = processador_transcricao.transcrever_fala(audio, servico.config["dispositivo"])
        comando = processador_transcricao.processar_transcricao(transcricao)
        print(f"📝 Capturado: {comando}")

        if servico.config["palavra_ativacao"] in comando:
            assistente_fala = AssistenteFala()
            assistente_fala.em_que_posso_ajudar()
            servico.config["status"] = True
            return jsonify({"status": "ativo", "transcricao": comando}), 201
        
        if servico.config["status"] and comando:
            
            servico.config["atuador"].validar_comando(comando)
            status = "ativo"
            if servico.config["atuador"].cena_validada or servico.config["atuador"].comando_validado:
                servico.config["status"] = False
                status = "desativado"
            servico.config["atuador"].atuar()
            
            return jsonify({"status": status, "transcricao": transcricao})
            
        
        return jsonify({"status": "desativado", "transcricao": transcricao}), 201
    except Exception as e:
        print(f"erro validando comando: {str(e)}")

        return jsonify({"erro": "erro validando comando"}), 500
    finally:
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

def ativar_interface_web():

    servico.config["atuador"] = Atuador()
    servico.config["status"] = False
    servico.config["palavra_ativacao"] = PALAVRA_ATIVACAO
    servico.config["dispositivo"] = "cuda:0" if torch.cuda.is_available() else "cpu"
    servico.run(host="0.0.0.0", debug=True)

ATIVAR_INTERFACE_WEB = False

if __name__ == "__main__":
    if ATIVAR_INTERFACE_WEB:
        ativar_interface_web()
    else:
        ativar_assistente()