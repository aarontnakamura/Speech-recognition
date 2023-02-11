from os import path
from pydub import AudioSegment
# files replace with the file name need to be converted from mp3 to wav
src = "abcdefg.mp3"
dst = "abcdefg.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
