from pydub import AudioSegment

import os

delay = [1000]
candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']

def add_echo_effect(in_path, out_path, delay_ms=500, decay=0.5):
    # Load the audio file
    audio = AudioSegment.from_file(in_path)
    
    # Create a silent segment for delay
    delayed_audio = audio[:delay_ms]
    
    # Reduce the volume and create the echo effect
    echoed_audio = audio.overlay(delayed_audio, loop = True)
    
    # Export the modified audio
    echoed_audio.export(out_path, format="wav")

for c in candidateDirs:
    for d in delay:

        current_dir = os.getcwd()
        operating_dir = current_dir + c
        saving_dir = operating_dir + 'Echo/'+ str(d)
        os.makedirs(saving_dir, exist_ok=True)

        audioNames = sorted(os.listdir(operating_dir))
        for aud in audioNames:
            if aud.endswith('.mp3'):
                print(operating_dir + ': ' + aud)
                outName = saving_dir + '/' + aud.split('.')[0] + '_e' + str(d) + '.wav'
                add_echo_effect(operating_dir + aud, outName, d)