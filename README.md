# Speech-Emotion-Analysis-for-Tamil-and-English

### System Overview
The system analyzes and interprets the emotional content of audio messages from patients. It starts with the **Audio to Text Processing module**, which converts speech data into text for further analysis. This text is then processed by **Text to Emotion Analysis modules** for both Tamil and English. Additionally, an **Audio to Emotion Analysis module** focuses on English audio, utilizing a combined approach of direct audio analysis and text-based emotion inference. This comprehensive assessment provides valuable insights into patients' emotional well-being for healthcare providers.

### Audio to Text Processing Module
**Audio Input:** Users provide voice messages detailing their concerns.   
**Speech Recognition:** Advanced algorithms analyze the audio to identify spoken words and phrases.  
**Language Processing:** Recognized text undergoes further processing to handle grammar, syntax, and semantics.  
**Text Output:** The processed audio is converted into text for subsequent analysis.  

### Tamil Text Translation to English Module
**Tamil Text Input:** Users provide text in Tamil.  
**Tokenization with INDIC NLP:** Tamil text is broken down into individual tokens.  
**Translation with Google Translate API:** Tokenized text is translated into English.  
**Text Output:** The translated English text is returned to the user. 

### Text to Emotion Analysis (English) Module
**Text Input:** Users provide text in English.  
**Tokenization with NLTK:** Text is broken down into tokens for detailed analysis.  
**Emotion Analysis with EmoRoBERTa:** Tokenized text is analyzed to detect emotional nuances.  
**Emotion Inference:** EmoRoBERTa assigns emotional labels or scores to the text.  
**Output:** A detailed assessment of the emotional content is provided.  

### Audio to Emotion Analysis (English) Module
**Audio Input:** Users provide audio messages.  
**Feature Extraction:** Acoustic features like pitch and intensity are extracted.  
**Speech Emotion Recognition with HUBERT:** HUBERT analyzes these features to predict the speaker's emotional state.  
**Emotion Output:** Predicted emotional states are labeled or scored.  
**Integration with Text Emotion Analysis:** Results are combined with text-based analysis for a comprehensive emotion assessment. 

### User Interface
The "Med Vitals" app features a simple, user-friendly interface. Users can upload audio files, submit them for analysis, and view detailed reports. This streamlined interface ensures a smooth user experience, facilitating mental health support and intervention.

### Architecture

![image](https://github.com/Vasudha08/Speech-Emotion-Analysis-for-Tamil-and-English/assets/105427446/2c575c9c-fb2e-456a-8f91-71ecf2da4c85)

