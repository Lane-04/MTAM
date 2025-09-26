from pydub import AudioSegment
from pydub.effects import compress_dynamic_range

import os

thresholds = [-50]
ratio = 200
candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']

def apply_compression(audio, threshold, ratio):
    return compress_dynamic_range(audio, threshold=threshold, ratio=ratio)

def process_audio(in_path, out_path, t):
    audio = AudioSegment.from_file(in_path)
    compressed_audio = apply_compression(audio, t, ratio)
    compressed_audio.export(out_path, format="wav")

for c in candidateDirs:
    for t in thresholds:

        current_dir = os.getcwd()
        operating_dir = current_dir + c
        saving_dir = operating_dir + 'compress/'+ str(t)
        os.makedirs(saving_dir, exist_ok=True)

        audioNames = sorted(os.listdir(operating_dir))
        for aud in audioNames:
            if aud.endswith('.mp3'):
                print(operating_dir + ': ' + aud)
                outName = saving_dir + '/' + aud.split('.')[0] + '_t' + str(t) + '.wav'
                process_audio(operating_dir + aud, outName, t)