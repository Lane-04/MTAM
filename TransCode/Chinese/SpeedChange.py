from audiostretchy.stretch import AudioStretch
from audiostretchy.stretch import stretch_audio

import os

velocity = [0.6,1.45]
candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']

def change_speed(inPath, outPath, R):
    stretch_audio(inPath, outPath, ratio = R)

for c in candidateDirs:
    for v in velocity:
        stretchR = 1.0/v

        current_dir = os.getcwd()
        operating_dir = current_dir + c
        saving_dir = operating_dir + 'Tempo/'+ str(v)
        os.makedirs(saving_dir, exist_ok=True)

        audioNames = sorted(os.listdir(operating_dir))
        for aud in audioNames:
            if aud.endswith('.mp3'):
                print(operating_dir + ': ' + aud)
                outName = saving_dir + '/' + aud.split('.')[0] + '_' + str(v) + '.wav'
                change_speed(operating_dir + aud, outName, stretchR)