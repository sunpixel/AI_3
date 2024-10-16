#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
from gtts import gTTS  # Import gTTS for text-to-speech
from deep_translator import GoogleTranslator  # Import Deep Translator

# Function to play the generated speech
def talk(words, language='ru'):
    try:
        tts = gTTS(text=words, lang=language)
        tts.save("speech.mp3")
        os.system("start speech.mp3")  # For Windows; use 'afplay' for macOS, 'xdg-open' for Linux
    except Exception as e:
        print(f"Ошибка генерации речи: {e}")

# Function to translate text to the specified language
def translate_text(text, target_language):
    try:
        translation = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translation
    except Exception as e:
        print(f"Ошибка перевода текста: {e}")
        return text  # Return the original text in case of an error

# Main loop
if __name__ == "__main__":
    # Ask the user for language preference
    languages = ['ru', 'en', 'ja', 'es', 'fr', 'nl']

    # Prompt to choose a language
    language_choice = input("Выберите язык (ru/en/ja/es/fr/nl): ").strip().lower()

    # If the choice is not in the list, default to Russian ('ru')
    if language_choice not in languages:
        print("Неверный выбор языка, по умолчанию используется Русский ('ru').")
        language_choice = 'ru'

    # Greet the user in the selected language
    greeting_text = 'Привет, давай поговорим!'
    translated_greeting = translate_text(greeting_text, language_choice)
    talk(translated_greeting, language_choice)

    while True:
        # Accept a line from the user
        text_input = input("Введите текст для озвучивания (или напишите 'стоп' для выхода): ").strip()
        if text_input.lower() == "стоп":
            farewell_text = "Хорошо, до встречи!"  # Original farewell in Russian
            translated_farewell = translate_text(farewell_text, language_choice)  # Translate farewell
            talk(translated_farewell, language_choice)  # Speak the farewell
            break

        # Translate to language
        translated_text = translate_text(text_input, language_choice)

        # Speak the translated text
        talk(translated_text, language_choice)
