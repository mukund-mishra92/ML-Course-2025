import streamlit as st
import speech_recognition as sr
import pyttsx3
from transformers import pipeline

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speech speed

# Load sentiment analysis pipeline
sentiment_model = pipeline("text-classification", model='bert-base-uncased-sentiment-model')

st.title("Voice Sentiment Analysis (Multi-Class)")

# Function to capture audio
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            st.success("Processing audio...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, could not understand your speech.")
            return None
        except sr.RequestError:
            st.error("Speech Recognition service is unavailable.")
            return None

# Button for voice input
if st.button("🎙️ Speak"):
    text_input = recognize_speech()
    if text_input:
        st.write(f"Recognized Text: **{text_input}**")

        # Predict sentiment
        result = sentiment_model(text_input)[0]
        label = result['label']
        score = result['score']
        
        # Display result
        st.success(f"Predicted Sentiment: {label} ({score:.2f})")

        # Speak result
        speak_text = f"The sentiment is {label} with a confidence of {score:.2f}"
        engine.say(speak_text)
        engine.runAndWait()
