import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()

def sound_recoding():
  #recoding variable
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

while True:
  sound_recoding()
