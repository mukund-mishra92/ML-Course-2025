import numpy as py
import pandas as pd
import streamlit as st

from transformers import pipeline
st.title("fine tuning BERT for twitter tweet for multi class sentient classification")

sentiment_model = pipeline("text-classification", model='bert-base-uncased-sentiment-model')
text = st.text_area("Enter some text")
if st.button("predict"):
    result = sentiment_model(text)
    st.write(result)

# import streamlit as st
# import speech_recognition as sr
# import pyttsx3
# from transformers import pipeline

# # Load sentiment analysis model
# @st.cache_resource
# def load_model():
#     return pipeline("text-classification", model='bert-base-uncased-sentiment-model')

# sentiment_model = load_model()

# # Initialize TTS engine
# @st.cache_resource
# def init_tts():
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     return engine

# tts_engine = init_tts()

# # Title
# st.title("🎤 Voice-Powered Sentiment Classifier")

# # Instructions
# st.markdown("Click the button to speak into your mic. The app will transcribe your speech, classify the sentiment, display the result, and read it aloud.")

# # Function to recognize speech
# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("🎙 Listening... Please speak now.")
#         audio = recognizer.listen(source, phrase_time_limit=5)
#         try:
#             with st.spinner("🧠 Transcribing..."):
#                 text = recognizer.recognize_google(audio)
#             return text
#         except sr.UnknownValueError:
#             st.error("❌ Could not understand the audio.")
#             return None
#         except sr.RequestError:
#             st.error("❌ Could not request results from the speech service.")
#             return None

# # Voice Input Button
# if st.button("🎤 Speak Now"):
#     transcribed_text = recognize_speech()

#     if transcribed_text:
#         st.success(f"📝 You said: `{transcribed_text}`")

#         # Sentiment prediction
#         with st.spinner("🔍 Analyzing sentiment..."):
#             result = sentiment_model(transcribed_text)[0]
#             label = result['label']
#             score = result['score']

#         st.markdown(f"### 🔮 Sentiment: `{label}`")
#         st.markdown(f"**Confidence:** {score:.2f}")

#         # Text-to-Speech
#         tts_message = f"The sentiment is {label} with {score:.2f} confidence."
#         tts_engine.say(tts_message)
#         tts_engine.runAndWait()
