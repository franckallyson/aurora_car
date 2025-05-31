
# 🚗 Assistente de Carro Autônomo — **Aurora Car**

Um projeto de assistente virtual para veículos autônomos, capaz de reconhecer comandos de voz e executar tarefas. O assistente pode ser executado tanto via terminal quanto através de uma interface web.

---

## ✅ Pré-requisitos

* Python 3.9 ou superior
* Ambiente virtual configurado

---

## 🚀 Instalação e Configuração

1️⃣ Crie e ative o ambiente virtual:

* **Windows:**

```bash
python3 -m venv env
env\Scripts\activate
```

* **Linux/Mac:**

```bash
python3 -m venv env
source env/bin/activate
```

2️⃣ Instale as dependências:

```bash
pip3 install -r requirements.txt
```

3️⃣ Baixe os recursos necessários (modelos ou dados):

```bash
python3 download.py
```

4️⃣ Configure os caminhos no arquivo `constantes.py`:

* Ajuste:

```python
CAMINHO_AUDIO_FALA = 'caminho/para/temp'
CONFIG = 'caminho/para/config.json'
```

* Recomenda-se apontar:

  * **CAMINHO\_AUDIO\_FALA** → para a pasta `/temp` do projeto.
  * **CONFIG** → para o arquivo `config.json` no diretório raiz do projeto.

---

## 🧪 Executando os Testes

Execute todos os testes unitários com:

```bash
python3 -m unittest discover -s tests
```

---

## 🏁 Executando o Assistente

Para iniciar o assistente, execute:

```bash
python3 assistente.py
```

* Por padrão, a **interface web estará ativada**.
* Se desejar rodar apenas pelo **terminal**, altere no arquivo `assistente.py` a constante:

```python
ATIVAR_INTERFACE_WEB = False
```

---

## 🔧 Estrutura de Diretórios

```
AuroraCar/
├── assistente.py
├── assistente_fala.py
├── constantes.py
├── download.py
├── requirements.txt
├── config.json
├── temp/
├── tests/
├── processamento/
├── audios_respostas/
├── atuadores/
└── public/
```

---

## 💡 Observações

* Verifique se os caminhos configurados estão corretos para seu sistema operacional.
* A pasta `/temp` deve existir e ser acessível para armazenar os áudios temporários.

---

## 📜 Licença

Projeto desenvolvido para fins acadêmicos e de pesquisa. Consulte os termos antes de utilização comercial.

---

