from pydub import AudioSegment
import numpy as np

import os

fs = [1000]

Name = os.listdir(PATH)

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

for name in Name:
    process_audio(NAME, NAME, fs[0])