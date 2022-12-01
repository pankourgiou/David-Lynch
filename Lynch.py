from gtts import gTTS
import os
text = "Try watching David Lynch movies like Rabbits"
tts = gTTS(text)
tts.save("hi.mp3")
os.system("hi.mp3")
