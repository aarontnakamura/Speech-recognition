##Japanese speech recognition
import speech_recognition as sr

r = sr.Recognizer()
#replace with the file name you want to use
with sr.AudioFile('abcdefg.wav') as source:
    audio = r.record(source)
print(r.recognize_google(audio, language='ja-JP'))

sub = (r.recognize_google(audio, language='ja-JP'))
