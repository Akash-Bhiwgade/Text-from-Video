import os
import speech_recognition as sr

command = "ffmpeg -i Bolna.mp4 Bolna.mp3"
os.system(command)

commandwav = "ffmpeg -i Bolna.mp3 Bolna.wav"
os.system(commandwav)

AUDIO_FILE = "Bolna.wav"

r = sr.Recognizer()
Bolna = sr.AudioFile(AUDIO_FILE)

with Bolna as source:
   audio = r.record(source, duration=100)

print(type(audio))
print(r.recognize_google(audio))
