from indicnlp import common
from indicnlp import loader
from indicnlp.tokenize import indic_tokenize
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Set the default encoding to UTF-8
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# Load Indic NLP resources
loader.load()

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
            chunk_text = recognizer.recognize_google(chunk_audio_data, language='ta-IN')
            text += chunk_text + " "
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

    return text

# Example usage
audio_file_path = "D:\\Hema\\Sem 6\\IP Lab\\Datasets\\ta_in_female\\taf_00008_00072928033.wav"  # Replace with the actual file path
text_result = convert_audio_to_text(audio_file_path)

# Tokenize the text using Indic NLP
#tokens = indic_tokenize.trivial_tokenize(text_result)
print("Text:", text_result)
