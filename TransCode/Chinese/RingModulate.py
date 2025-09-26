from pydub import AudioSegment
import numpy as np

import os

fs = [400]
candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']

def ring_modulate(audio, frequency):
    samples = np.array(audio.get_array_of_samples())
    sample_rate = audio.frame_rate

    # Create a modulation signal
    t = np.arange(len(samples)) / sample_rate
    modulation = np.sin(2 * np.pi * frequency * t)

    # Apply ring modulation
    modulated_samples = samples * modulation
    modulated_audio = audio._spawn(modulated_samples.astype(np.int16).tobytes())
    
    return modulated_audio

def process_audio(in_path, out_path, f):
    audio = AudioSegment.from_file(in_path)
    ringed_audio = ring_modulate(audio, f)
    ringed_audio.export(out_path, format="wav")

for c in candidateDirs:
    for f in fs:

        current_dir = os.getcwd()
        operating_dir = current_dir + c
        saving_dir = operating_dir + 'ringModulate/'+ str(f)
        os.makedirs(saving_dir, exist_ok=True)

        audioNames = sorted(os.listdir(operating_dir))
        for aud in audioNames:
            if aud.endswith('.mp3'):
                print(operating_dir + ': ' + aud)
                outName = saving_dir + '/' + aud.split('.')[0] + '_f' + str(f) + '.wav'
                process_audio(operating_dir + aud, outName, f)