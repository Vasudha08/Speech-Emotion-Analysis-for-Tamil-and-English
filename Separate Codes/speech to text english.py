import nltk
from nltk.tokenize import word_tokenize

import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

def convert_audio_to_text(audio_file_path):
    # Load audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Split audio on silence
    chunks = split_on_silence(audio, silence_thresh=-40)

    # Use SpeechRecognition to convert audio chunks to text
    recognizer = sr.Recognizer()
    text = ""

    for chunk in chunks:
        # Convert Pydub AudioSegment to bytes
        chunk_bytes = chunk.raw_data

        # Convert bytes to AudioData using SpeechRecognition's AudioData class
        chunk_audio_data = sr.AudioData(chunk_bytes, chunk.frame_rate, 2)

        try:
            chunk_text = recognizer.recognize_google(chunk_audio_data, language='en')
            text += chunk_text + " "
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

    return text

# Example usage
audio_file_path = "D:\Hema\Sem 6\IP Lab\Datasets\MELD\chatgpt.mp3"  # Replace with the actual file path
text_result = convert_audio_to_text(audio_file_path)

# Tokenize the English text using NLTK
#english_tokens = word_tokenize(text_result)
print("Text (English):", text_result)
