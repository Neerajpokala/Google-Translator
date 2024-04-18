import streamlit as st
from googletrans import Translator, LANGUAGES

def translate_text():
    translator = Translator()
    input_text = st.text_area("Enter the text to be translated:")

    detection = translator.detect(input_text)
    source_lang = detection.lang if input_text else None

    target_lang = st.selectbox("Select the target language:", [LANGUAGES[lang] for lang in LANGUAGES])
    target_lang_key = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_lang)]

    if st.button("Translate") and input_text and source_lang:
        translated_text = translator.translate(input_text, src=source_lang, dest=target_lang_key)
        st.success(f"Translated text ({target_lang}): {translated_text.text}")

def main():
    st.set_page_config(page_title="Text Translator", page_icon="🌎")
    st.title("Text Translator Supports 107 languages")
    translate_text()

if __name__ == "__main__":
    main()
