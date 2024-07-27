import gradio as gr
import time
import whisper
from elevenlabs import generate, play, set_api_key
import io
from pydub import AudioSegment
from interpreter import interpreter

# Set up API keys
eleven_labs_api_key = "<your_eleven_labs_api_key>"
set_api_key(eleven_labs_api_key)

# Set up Open Interpreter
interpreter.auto_run = True

# Load Whisper model
model = whisper.load_model("base")

def transcribe(audio):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text

def get_audio_length(audio_bytes):
    byte_io = io.BytesIO(audio_bytes)
    audio = AudioSegment.from_mp3(byte_io)
    length_ms = len(audio)
    return length_ms / 1000.0

def speak(text):
    audio = generate(
        text=text,
        voice="Daniel"
    )
    play(audio, notebook=True)
    audio_length = get_audio_length(audio)
    time.sleep(audio_length)

last_sentence = ""

def add_user_message(audio, history):
    user_message = transcribe(audio)
    return history + [[user_message, None]]

def bot(history):
    global last_sentence

    user_message = history[-1][0]
    history[-1][1] = ""
    active_block_type = ""

    for chunk in interpreter.chat(user_message, stream=True, display=False):
        # Message
        if chunk["type"] == "message" and "content" in chunk:
            if active_block_type != "message":
                active_block_type = "message"
            history[-1][1] += chunk["content"]

            last_sentence += chunk["content"]
            if any([punct in last_sentence for punct in ".?!\n"]):
                yield history
                speak(last_sentence)
                last_sentence = ""
            else:
                yield history

        # Code
        if chunk["type"] == "code" and "content" in chunk:
            if active_block_type != "code":
                active_block_type = "code"
                history[-1][1] += f"\n```{chunk['format']}"
            history[-1][1] += chunk["content"]
            yield history

        # Output
        if chunk["type"] == "execution" and chunk.get("start") == True:
            history[-1][1] += "\n```\n\n```text\n"
            yield history
        if chunk["type"] == "execution" and chunk.get("end") == True:
            history[-1][1] = history[-1][1].strip()
            history[-1][1] += "\n```\n"
            yield history
        if chunk["type"] == "console" and chunk.get("format") == "output":
            if chunk["content"] == "KeyboardInterrupt":
                break
            history[-1][1] += chunk["content"] + "\n"
            yield history

    if last_sentence:
        speak(last_sentence)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    audio_input = gr.inputs.Audio(source="microphone", type="filepath")
    btn = gr.Button("Submit")

    btn.click(add_user_message, [audio_input, chatbot], [chatbot]).then(
        bot, chatbot, chatbot
    )

if __name__ == "__main__":
    demo.launch(debug=True)
