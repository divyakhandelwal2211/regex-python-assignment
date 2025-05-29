import pygame as py
from gtts import gTTS

py.init()


def paytm(amount):
    txt = f"paytm par {amount}rs prapt huye, Thank you!!!"
    msg = gTTS(txt)
    msg.save("audio.mp3")
    song = py.mixer.Sound("audio.mp3")
    song.play()


paytm(20000000)
