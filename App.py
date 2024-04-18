import streamlit as st
from googletrans import Translator, LANGUAGES

def translate_text(input_text):
    translator = Translator()
    detection = translator.detect(input_text)
    source_lang = detection.lang if input_text else None

    if source_lang:
        target_lang = st.selectbox("Select the target language:", [LANGUAGES[lang] for lang in LANGUAGES])
        target_lang_key = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_lang)]

        if st.button("Translate"):
            try:
                translated_text = translator.translate(input_text, src=source_lang, dest=target_lang_key)
                st.success(f"Translated text ({target_lang}): {translated_text.text}")
            except Exception as e:
                st.error(f"An error occurred during translation: {str(e)}")
    else:
        st.warning("Please provide text in a known language.")

def main():
    st.set_page_config(page_title="Text Translator", page_icon="🌎")
    st.title("Text Translator Supports 107 languages")
    input_text = st.text_area("Enter the text to be translated:")
    translate_text(input_text)

if __name__ == "__main__":
    main()
