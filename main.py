import streamlit as st

# Streamlit App
st.title("Audio File Uploader")

# Upload audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])

# Display hardcoded message after upload
if audio_file:
    st.success("Audio file uploaded successfully!")
    st.audio(audio_file, format="audio/mp3")  # Play the uploaded audio