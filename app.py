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
        os.system("start speech.mp3")
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


if __name__ == "__main__":
    # Ask the user for language preference
    languages = ['ru', 'en', 'ja', 'es', 'fr', 'nl']
    language_choice = input("Выберите язык (ru/en/ja/es/fr/nl): ").strip().lower()

    # If not in the list, set to ru
    if language_choice not in languages:
        print("Неверный выбор языка, по умолчанию используется Русский ('ru').")
        language_choice = 'ru'

    greeting_text = 'Привет, давай поговорим!'
    translated_greeting = translate_text(greeting_text, language_choice)
    talk(translated_greeting, language_choice)

    while True:

        text_input = input("Введите текст для озвучивания (или напишите 'стоп' для выхода): ").strip()
        if text_input.lower() == "стоп":
            farewell_text = "Хорошо, до встречи!"
            translated_farewell = translate_text(farewell_text, language_choice)
            talk(translated_farewell, language_choice)
            break

        # Translate to language and speak
        translated_text = translate_text(text_input, language_choice)
        talk(translated_text, language_choice)
