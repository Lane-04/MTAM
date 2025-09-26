import os
import numpy as np
from pydub import AudioSegment

def reverb_audio(input_file, output_file):

    audio = AudioSegment.from_file(input_file, format="wav")

    samples = audio.get_array_of_samples()

    strength = 700
    duration = 0.4

    reverb_samples = np.convolve(samples, np.random.randn(strength) * duration, mode='same').astype(np.int16)

    reverb_audio = AudioSegment(
        data=reverb_samples.tobytes(),
        sample_width=audio.sample_width,
        frame_rate=audio.frame_rate,
        channels=audio.channels
    )

    reverb_audio.export(output_file, format="wav")


Name = os.listdir("PATH")

for name in Name:
    reverb_audio(FILENAME, FILENAME)
