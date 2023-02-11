##Japanese speech recognition
import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('/Users/aarontnakamura/Desktop/export/4_resting_state_long_1_2022_Sep_20_1925_wav/mic_alt-1663669655.877.wav') as source:
    audio = r.record(source)
print(r.recognize_google(audio, language='ja-JP'))

sub = (r.recognize_google(audio, language='ja-JP'))
