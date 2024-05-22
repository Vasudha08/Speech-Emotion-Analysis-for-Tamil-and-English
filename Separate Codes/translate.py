from googletrans import Translator

def translate_tamil_to_english(text):
    translator = Translator()
    translation = ""

    # Split the text into smaller chunks (e.g., 200 characters) and translate each chunk
    chunk_size = 200
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunk_translation = translator.translate(chunk, src='ta', dest='en').text
        translation += chunk_translation

    return translation

tamil_text = "ஒவ்வொரு நாளும் நான் சோகமாகவே உணர்கிறேன் எவ்வளவோ முயற்சி செய்தும் என்னால் அந்த சோகத்தில் இருந்து வெளிவர முடியவில்லை ஒரு கனமான சுமையாகவே என்னை எப்பொழுதும் உணருகிறேன் என்னால் இதிலிருந்து தப்பிக்க முடியவில்லை கடைசியாக நான் எதைப் பற்றி சிந்திக்காமல் உண்மையாகவே மகிழ்ச்சியாக அல்லது உற்சாகமாக உணர்ந்ததை என்னால் நினைவில் கொள்ள விரும்பவில்லை பெரும்பாலான நாட்களில் என்னால் படுக்கையிலிருந்து எழும்ப முடியவில்லை எதற்காக வாழ்கிறோம் என்று சிந்திக்கத் தோன்றுகின்றது எப்பொழுதும் வெறுமையாகவும் தொலைந்தது ஆகவும் உணர்க"
english_translation = translate_tamil_to_english(tamil_text)
print("Tamil: ", tamil_text)
print("English Translation: ", english_translation)
