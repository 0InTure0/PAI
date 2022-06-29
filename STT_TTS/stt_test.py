#sudo pip3 install playsound && gTTs && speechrecognition
from gtts.tts import gTTS
import playsound


def speak(text):
  tts = gTTS(text=text, lang='ko')
  filename='voice.wav'
  tts.save(filename)  
  playsound.playsound(filename)

speak("안녕하세요 인공지능 펫봇 파이입니다~334, 100")