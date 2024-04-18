import streamlit as st
from googletrans import Translator, LANGUAGES

def translate_text(input_text, target_lang_key):
    try:
        translator = Translator()
        translated_text = translator.translate(input_text, dest=target_lang_key)
        return translated_text.text
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.set_page_config(page_title="Text Translator", page_icon="🌎")
    st.title("Text Translator Supports 107 languages")

    input_text = st.text_area("Enter the text to be translated:")

    # Always show the selectbox and translate button
    target_lang = st.selectbox("Select the target language:", [LANGUAGES[lang] for lang in LANGUAGES])
    target_lang_key = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_lang)]
    translate_button = st.button("Translate")

    if translate_button and input_text:
        translated_text = translate_text(input_text, target_lang_key)
        st.success(f"Translated text ({target_lang}): {translated_text}")

if __name__ == "__main__":
    main()
