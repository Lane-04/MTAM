from pydub import AudioSegment
from pydub.effects import compress_dynamic_range

import os

thresholds = [-50]
ratio = 200
candidateDirs = []

def apply_compression(audio, threshold, ratio):
    return compress_dynamic_range(audio, threshold=threshold, ratio=ratio)

def process_audio(in_path, out_path, t):
    audio = AudioSegment.from_file(in_path)
    compressed_audio = apply_compression(audio, t, ratio)
    compressed_audio.export(out_path, format="wav")

Name = os.listdir(PATH)

for name in Name:
    process_audio(NAME, NAME, thresholds[0])