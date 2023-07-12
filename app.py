import streamlit as st
import os
import openai
from secret_key import openapi_key

os.environ['OPENAI_API_KEY'] = openapi_key

# Define the list of available languages
languages = [
    "English",
    "Hindi",
    "French",
    "Telugu",
    "Albanian",
    "Bengali",
    "Bhojpuri",
    "Brazilian Portuguese",
    "Chinese",
    "Dutch",
    "Georgian",
    "German",
    "Greek",
    "Gujarati",
    "Haryanvi",
    "Hungarian",
    "Indonesian",
    "Irish",
    "Italian",
    "Japanese",
    "Kannada",
    "Korean",
    "Maithili",
    "Mandarin Chinese",
    "Marathi",
    "Marwari",
    "Nepali",
    "Norwegian",
    "Oriya",
    "Portuguese",
    "Punjabi",
    "Romanian",
    "Russian",
    "Sanskrit",
    "Serbian",
    "Ukrainian",
    "Urdu"
]

def translate_text(text, source_language, target_language):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=f"Translate the following text from {source_language} to {target_language}:\n{text}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    translation = response.choices[0].text.strip().split("\n")[0]
    return translation

# Streamlit web app
def main():
    st.title("Translate My Text")

    # Input text
    text = st.text_area("Enter the text to translate")

    # Source language dropdown
    source_language = st.selectbox("Select source language", languages)

    # Target language dropdown
    target_language = st.selectbox("Select target language", languages)

    # Translate button
    if st.button("Translate"):
        translation = translate_text(text, source_language, target_language)
        st.markdown(f'<p style="color: blue; font-size: 25px;"> {translation}</p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
