import os
import numpy as np
from pydub import AudioSegment

def tremolo_audio(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="wav")

    samples = audio.get_array_of_samples()

    tremolo_freq = 500
    tremolo_depth = 500

    tremolo_samples = samples * (1 + tremolo_depth * np.sin(2 * np.pi * tremolo_freq * np.arange(len(samples)) / audio.frame_rate))

    tremolo_samples = np.int16(tremolo_samples / np.max(np.abs(tremolo_samples)) * 32767)

    tremolo_audio = AudioSegment(
        data=tremolo_samples.tobytes(),
        sample_width=audio.sample_width,
        frame_rate=audio.frame_rate,
        channels=audio.channels
    )

    tremolo_audio.export(output_file, format="wav")


Name = os.listdir(PATH)

for name in Name:
    tremolo_audio(NAME, NAME)