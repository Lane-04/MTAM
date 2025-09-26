from pydub import AudioSegment

import os

Name = os.listdir(PATH)

def surround_effect(audio):
    left = audio.pan(-0.5)
    right = audio.pan(0.5)
    return left.overlay(right)

def process_audio(in_path, out_path):
    audio = AudioSegment.from_file(in_path)
    surround_audio = surround_effect(audio)
    surround_audio.export(out_path, format="wav")

for name in Name:
     process_audio(NAME, NAME)