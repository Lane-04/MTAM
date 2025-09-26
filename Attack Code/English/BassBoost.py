from pydub import AudioSegment

import os

dbs = [200]
cutoff = 150


def bass_boost(audio, boost_db, cutoff):
    low_pass = audio.low_pass_filter(cutoff)
    boosted = low_pass + boost_db
    return audio.overlay(boosted)

def process_audio(in_path, out_path, db):
    audio = AudioSegment.from_file(in_path)
    boosted_audio = bass_boost(audio, db, cutoff)
    boosted_audio.export(out_path, format="wav")

Name = os.listdir(PATH)

for name in Name:
    process_audio(NAME, NAME, dbs[0])