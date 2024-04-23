from gtts import gTTS
import os

def speak(text):
    try:
        tts = gTTS(text=text, lang='ru')
        filename = "response.mp3"
        tts.save(filename)
        os.system(f"afplay {filename}")
        os.remove(filename)  # Удаляем файл после воспроизведения
    except Exception as e:
        print(f"Ошибка при генерации или воспроизведении речи: {e}")
