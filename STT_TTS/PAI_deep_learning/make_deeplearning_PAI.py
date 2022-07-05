import numpy as np
import itertools
import librosa
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential, Model
from keras.layers import Input, Dense
from keras.layers import Conv2D, MaxPool2D, Flatten

midi_file = './PAI_data.wav'
num_note = 191
sec = 2
audio = []
inst = []

for inst_idx, note in itertools.product(range(1), range(num_note)):
  instrunment = 0
  if (note >= 41):
    instrunment = 1
  offset = (note*sec)
  #print('instrunment: {}, note: {}, offset: {}'.format(instrunment, note, offset))
  y, sr = librosa.load(midi_file, sr=None, offset=offset, duration=2.0)
  audio.append(y)
  inst.append(instrunment)

audio_mfcc = []
for y in audio:
  ret = librosa.feature.mfcc(y=y, sr=sr)
  audio_mfcc.append(ret)

mfcc_np = np.array(audio_mfcc, np.float32)
inst_np = np.array(inst, np.int16)

mfcc_np = mfcc_np.reshape((191, 20 * 188))

scaler = MinMaxScaler()
scaler.fit(mfcc_np)

from keras.utils import to_categorical

mfcc_np = np.array(audio_mfcc, np.float32)
mfcc_array = np.expand_dims(mfcc_np, -1)
inst_cat = to_categorical(inst_np)

train_x, test_x, train_y, test_y  = train_test_split(mfcc_array, inst_cat, test_size=0.2)

def model_build():
  model = Sequential()
  input = Input(shape=(20, 188, 1))
  output = Conv2D(128, 3, strides=1, padding='same', activation='relu')(input)
  output = MaxPool2D(pool_size=(2, 2), strides=2, padding='same')(output)
  output = Conv2D(256, 3, strides=1, padding='same', activation='relu')(output)
  output = MaxPool2D(pool_size=(2, 2), strides=2, padding='same')(output)
  output = Conv2D(512, 3, strides=1, padding='same', activation='relu')(output)
  output = MaxPool2D(pool_size=(2, 2), strides=2, padding='same')(output)

  output = Flatten()(output)
  output = Dense(512, activation='relu')(output)
  output = Dense(256, activation='relu')(output)
  output = Dense(128, activation='relu')(output)
  output = Dense(2, activation='sigmoid')(output)
  model = Model(inputs=[input], outputs=output)
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

  return model

model = model_build()
history = model.fit(train_x, train_y, epochs=100, batch_size=128, validation_split=0.2)
model.evaluate(test_x, test_y)