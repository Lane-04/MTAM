import librosa
import numpy as np
import os
import soundfile as sf

Name = os.listdir(PATH)

def add_noise(data):
    wn = np.random.normal(0,2,len(data))
    data_noise = np.where(data != 0.0, data.astype('float64') + 0.02 * wn, 0.0).astype(np.float32)
    return data_noise


for name in Name:
    path = PATH
    data, fs = librosa.core.load(path + name)
    data_noise = add_noise(data)
    sf.write(NAME, data_noise, fs)