import pyaudio
import wave
import numpy as np
import librosa
from keras.models import load_model

#recoding variable
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()

#PAI_AI valiable
model = load_model('PAI_Model_V2(0.052, 0.976).h5')

def sound_recoding():
  print("recoding start")
  p = pyaudio.PyAudio()
  stream = p.open(format=FORMAT, channels=CHANNELS,rate=RATE, input=True, frames_per_buffer=CHUNK)
  frames = []
  for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
      data = stream.read(CHUNK)
      frames.append(data)
  print("recoding save")
  stream.stop_stream()
  stream.close()
  p.terminate()
  wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(b''.join(frames))
  wf.close()

def PAI_AI():
  y, sr = librosa.load(WAVE_OUTPUT_FILENAME, sr=None, duration=2.0)
  ret = librosa.feature.mfcc(y=y, sr=sr)
  audio_mfcc = [ret]
  mfcc_np = np.array(audio_mfcc, np.float32)
  mfcc_array = np.expand_dims(mfcc_np, -1)
  xhat = mfcc_array[[0]]
  y_prob = model.predict(xhat, verbose=0) 
  predicted = y_prob.argmax(axis=-1)
  PAI_value = str(predicted[0])
  print('Predict : ' + PAI_value)
  return PAI_value


while True:
  sound_recoding()
  PAI_value = PAI_AI()
  print(PAI_value)
  if(PAI_value == "0"):
    input("말씀하세요 주인님:")
  else:
    pass
