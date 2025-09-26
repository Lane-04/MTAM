from pydub import AudioSegment

import os

dbs = [100]
cutoff = 150
candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']

def bass_boost(audio, boost_db, cutoff):
    low_pass = audio.low_pass_filter(cutoff)
    boosted = low_pass + boost_db
    return audio.overlay(boosted)

def process_audio(in_path, out_path, db):
    audio = AudioSegment.from_file(in_path)
    boosted_audio = bass_boost(audio, db, cutoff)
    boosted_audio.export(out_path, format="wav")

for c in candidateDirs:
    for db in dbs:

        current_dir = os.getcwd()
        operating_dir = current_dir + c
        saving_dir = operating_dir + 'bassBoost/'+ str(db)
        os.makedirs(saving_dir, exist_ok=True)

        audioNames = sorted(os.listdir(operating_dir))
        for aud in audioNames:
            if aud.endswith('.mp3'):
                print(operating_dir + ': ' + aud)
                outName = saving_dir + '/' + aud.split('.')[0] + '_db' + str(db) + '.wav'
                process_audio(operating_dir + aud, outName, db)