from voice_box.voice_box import record_audio, play_audio, tts_to_audio
from Sarvam_telugu.sarvam_telugu import transcribe_audio
from langchain.langchain_module import process_text
from Mistral_7b.static_query_handler import handle_static_query

AUDIO_FILENAME = 'user_query.wav'
RESPONSE_AUDIO_FILENAME = 'llm_response.wav'

# 1. Record user audio
print("Please speak your query in English or Telugu...")
record_audio(AUDIO_FILENAME, duration=10)

# 2. Transcribe audio to text and get the detected language
transcript, detected_lang = transcribe_audio(AUDIO_FILENAME)
print(f"Transcript: {transcript} (Language: {detected_lang})")

# 3. Classify intent
intent = process_text(transcript)
print(f"Intent detected: {intent['type']}")

# 4. Handle the query
if intent['type'] in ['greeting', 'query']:
    llm_response = handle_static_query(transcript)
    print(f"LLM Response: {llm_response}")

    # 5. Convert response to speech using the detected language
    tts_to_audio(llm_response, output_filename=RESPONSE_AUDIO_FILENAME, language_code=detected_lang)
    play_audio(RESPONSE_AUDIO_FILENAME)
else:
    print("Intent not recognized as static query or greeting.") 