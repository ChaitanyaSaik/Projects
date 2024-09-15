from gtts import gTTS
import os
f=open('sample.txt')
x=f.read()
language='en'
audio=gTTS(text=x,slow=False)
audio.save("audio.wav")
os.system("audio.wav")

