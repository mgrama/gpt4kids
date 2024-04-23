import speech_recognition as sr
import numpy as np
import sounddevice as sd

def listen(duration=5, fs=44100):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # ждем завершения записи
    print("Finished recording")

    # Использование speech_recognition для преобразования аудио в текст
    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(np.asarray(recording).tobytes(), fs, 2)  # Создаем AudioData

    try:
        # Используем recognizer для преобразования аудио данных в текст
        text = recognizer.recognize_google(audio_data, language='ru-RU')
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
