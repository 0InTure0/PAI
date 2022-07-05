import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something! : ")
    audio = r.listen(source)

with open("audio_file2.wav","wb") as file:
  file.write(audio.get_wav_data())

stt_text = r.recognize_google(audio, language='ko-KR')
print(stt_text)