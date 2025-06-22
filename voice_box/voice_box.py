import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import sys
import os
from dotenv import load_dotenv
import requests
import base64
from Sarvam_telugu.sarvam_telugu import transcribe_audio

load_dotenv()
SARVAM_API_KEY = os.getenv('SARVAM_API_KEY')

# SarvamAI STT
STT_URL = 'https://api.sarvam.ai/speech-to-text'
# SarvamAI TTS
TTS_URL = 'https://api.sarvam.ai/text-to-speech'

AUDIO_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Sarvam_Audio_IO')
os.makedirs(AUDIO_DIR, exist_ok=True)

def record_audio(filename='output.wav', duration=15, fs=16000):
    filepath = os.path.join(AUDIO_DIR, filename)
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filepath, fs, audio)
    print(f"Saved recording to {filepath}")
    return filepath

def play_audio(filename='output.wav'):
    filepath = os.path.join(AUDIO_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist.")
        return
    fs, data = wav.read(filepath)
    print(f"Playing {filepath}...")
    sd.play(data, fs)
    sd.wait()
    print("Playback finished.")

def tts_to_audio(text, language_code='te-IN', output_filename='tts_output.wav', model='bulbul:v2'):
    headers = {"api-subscription-key": SARVAM_API_KEY, "Content-Type": "application/json"}
    payload = {"text": text, "target_language_code": language_code, "model": model}
    response = requests.post(TTS_URL, json=payload, headers=headers)
    if response.status_code == 200:
        audio_b64 = response.json()["audios"][0]
        audio_bytes = base64.b64decode(audio_b64)
        output_path = os.path.join(AUDIO_DIR, output_filename)
        with open(output_path, "wb") as f:
            f.write(audio_bytes)
        print(f"TTS audio saved to {output_path}")
        return output_path
    else:
        print("TTS Error:", response.text)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python voice_box.py [record|play|stt|tts] [filename|text] [duration]")
        sys.exit(1)
    command = sys.argv[1]
    if command == 'record':
        filename = sys.argv[2] if len(sys.argv) > 2 else 'output.wav'
        duration = int(sys.argv[3]) if len(sys.argv) > 3 else 15
        record_audio(filename, duration)
    elif command == 'play':
        filename = sys.argv[2] if len(sys.argv) > 2 else 'output.wav'
        play_audio(filename)
    elif command == 'stt':
        filename = sys.argv[2] if len(sys.argv) > 2 else 'output.wav'
        transcript = transcribe_audio(filename)
        print(f"Transcript: {transcript}")
    elif command == 'tts':
        text = sys.argv[2] if len(sys.argv) > 2 else 'హలో, ఇది టెస్ట్ సందేశం.'
        output_filename = 'tts_output.wav'
        tts_to_audio(text, output_filename=output_filename)
        play_audio(output_filename)
    else:
        print("Unknown command. Use 'record', 'play', 'stt', or 'tts'.") 