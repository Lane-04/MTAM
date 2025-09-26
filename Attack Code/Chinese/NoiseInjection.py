import librosa
import numpy as np
import os
import soundfile as sf

candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']


def add_noise(data):
    wn = np.random.normal(0,2,len(data))
    data_noise = np.where(data != 0.0, data.astype('float64') + 0.02 * wn, 0.0).astype(np.float32)
    return data_noise

for c in candidateDirs:

    current_dir = os.getcwd()
    operating_dir = current_dir + c
    saving_dir = operating_dir + 'noise'
    os.makedirs(saving_dir, exist_ok=True)

    audioNames = sorted(os.listdir(operating_dir))
    for aud in audioNames:
        if aud.endswith('.mp3'):
            print(operating_dir + ': ' + aud)
            data, fs = librosa.core.load(operating_dir + aud)
            data_noise = add_noise(data)
            outName = saving_dir + '/' + aud.split('.')[0] + '_noise' + '.wav'
            sf.write(outName, data_noise, fs)