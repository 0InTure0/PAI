import numpy as np
import librosa
from keras.models import load_model

midi_file = 'audio_file2.wav'
model = load_model('./PAI_Model(0.0021, 1).h5')

y, sr = librosa.load(midi_file, sr=None, duration=2.0)
audio = [y]

ret = librosa.feature.mfcc(y=y, sr=sr)
audio_mfcc = [ret]

mfcc_np = np.array(audio_mfcc, np.float32)
mfcc_array = np.expand_dims(mfcc_np, -1)

xhat = mfcc_array[[0]]
y_prob = model.predict(xhat, verbose=0) 
predicted = y_prob.argmax(axis=-1)
print('Predict : ' + str(predicted[0]))