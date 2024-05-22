from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline
import tensorflow as tf

## Load tokenizer and model
tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

# Example usage
audio_file_path = r"D:\Hema\Sem 6\IP Lab\Datasets\MELD\test_shruti.mp3" # Replace with the actual file path

# Convert audio to text
text_result = " No news about other pictures"

# Tokenize text
inputs = tokenizer(text_result, return_tensors="tf")

# Get raw model output
outputs = model(**inputs)

# Fetch the emotion labels from the model config
emotion_labels = model.config.id2label

# Interpret the output probabilities for each emotion label
raw_output = tf.nn.softmax(outputs.logits, axis=-1).numpy()[0]
emotion_probabilities = list(zip(emotion_labels.values(), raw_output))

# Sort emotions based on probabilities in descending order
sorted_emotions = sorted(emotion_probabilities, key=lambda x: x[1], reverse=True)

# Display all emotion probabilities
for emotion, probability in sorted_emotions:
    print(f"{emotion}: {probability:.4f}")
