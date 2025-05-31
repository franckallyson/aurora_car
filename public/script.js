const statusDisplay = document.getElementById('status');
const transcriptionDisplay = document.getElementById('transcription');
const statusAssistenteDisplay = document.getElementById('status_assistente');
let audioContext;
let processor;
let input;
let recorder;
let stream;
let isRecording = false;

const silenceThreshold = 0.01; // Sensibilidade (ajustável)
const silenceDelay = 1000; // ms após o silêncio para parar

let silenceTimer = null;

async function startVAD() {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    audioContext = new (window.AudioContext || window.webkitAudioContext)();
    input = audioContext.createMediaStreamSource(stream);

    processor = audioContext.createScriptProcessor(2048, 1, 1);
    input.connect(processor);
    processor.connect(audioContext.destination);

    processor.onaudioprocess = detectVoice;

    statusDisplay.textContent = 'Aguardando voz...';
}

function detectVoice(event) {
    const inputData = event.inputBuffer.getChannelData(0);
    let total = 0;

    for (let i = 0; i < inputData.length; i++) {
        total += Math.abs(inputData[i]);
    }

    const rms = total / inputData.length;

    if (rms > silenceThreshold) {
        if (!isRecording) {
            startRecording();
        }

        clearTimeout(silenceTimer);

        silenceTimer = setTimeout(() => {
            if (isRecording) {
                stopRecording();
            }
        }, silenceDelay);

    }
}

function startRecording() {
    console.log('🎙️ Detecção de voz: Iniciando gravação...');
    isRecording = true;
    recorder = RecordRTC(stream, {
        type: 'audio',
        mimeType: 'audio/wav',
        recorderType: RecordRTC.StereoAudioRecorder,
        numberOfAudioChannels: 1,
        desiredSampRate: 16000
    });

    recorder.startRecording();
    statusDisplay.textContent = 'Gravando...';
}

function stopRecording() {
    console.log('⏹️ Silêncio detectado: Parando gravação...');
    isRecording = false;
    recorder.stopRecording(async () => {
        const blob = recorder.getBlob();

        statusDisplay.textContent = 'Enviando...';

        const formData = new FormData();
        formData.append('audio', blob, 'audio.wav');

        try {
            const response = await fetch('reconhecer_comando', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            const texto = result.transcricao || "Erro na transcrição";
            transcriptionDisplay.textContent = `${texto}`;
            statusAssistenteDisplay.textContent = `${result.status.toUpperCase()}`
            console.log('Transcrição:', texto);
        } catch (error) {
            console.error("Erro:", error);
            transcriptionDisplay.textContent = "\n❌ Erro na comunicação";
        }

        recorder.destroy();
        recorder = null;

        statusDisplay.textContent = 'Aguardando voz...';
    });
}

function stopVAD() {
    if (processor) processor.disconnect();
    if (input) input.disconnect();
    if (audioContext) audioContext.close();
    if (stream) stream.getTracks().forEach(track => track.stop());

    isRecording = false;
    statusDisplay.textContent = 'Parado';
}


function atualizarCorStatus() {
    const statusDiv = document.getElementById('status_assistente');
    const statusTexto = statusDiv.textContent.trim().toUpperCase();

    if (statusTexto === 'ATIVO') {
        statusDiv.style.color = 'white';
        statusDiv.style.backgroundColor = 'green';
    } else if (statusTexto === 'DESATIVADO') {
        statusDiv.style.color = 'white';
        statusDiv.style.backgroundColor = 'red';
    } else {
        // Caso queira uma cor padrão para outros status
        statusDiv.style.color = 'black';
        statusDiv.style.backgroundColor = 'gray';
    }
}

// Executa ao carregar a página
atualizarCorStatus();

// Se quiser atualizar sempre que mudar o texto, pode observar:
const observer = new MutationObserver(atualizarCorStatus);
observer.observe(document.getElementById('status_assistente'), { childList: true });