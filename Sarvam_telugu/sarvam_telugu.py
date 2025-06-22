import os
import requests
from dotenv import load_dotenv

AUDIO_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Sarvam_Audio_IO')
load_dotenv()
SARVAM_API_KEY = os.getenv('SARVAM_API_KEY')
STT_URL = 'https://api.sarvam.ai/speech-to-text'

def transcribe_audio(filename, model='saarika:v2.5'):
    """Transcribes audio, prioritizing Telugu and English, and returns the transcript and detected language."""
    filepath = os.path.join(AUDIO_DIR, filename)
    headers = {"api-subscription-key": SARVAM_API_KEY}
    files = {"file": (os.path.basename(filepath), open(filepath, "rb"), "audio/wav")}
    
    # Prioritize Telugu and English to guide the auto-detection
    payload = {
        "model": model,
        "language_codes": "te-IN,en-IN"  # Hinting the model
    }
    
    response = requests.post(STT_URL, data=payload, files=files, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        transcript = data.get("transcript", "")
        detected_lang = data.get("language_code", "en-IN")
        return transcript, detected_lang
    else:
        print("STT Error:", response.text)
        return "", "en-IN" 