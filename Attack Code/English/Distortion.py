import os
import numpy as np
import soundfile as sf

def distort_audio(input_file, output_file):

    data, samplerate = sf.read(input_file) 
        
    noise_std_dev = 0.1

    white_noise = np.random.uniform(-1, 1, data.shape)

    distorted_data = data + white_noise * noise_std_dev

    distorted_data = np.clip(distorted_data, -1, 1)

    sf.write(output_file, distorted_data, samplerate)

Name = os.listdir(PATH)

for name in Name:
    distort_audio(NAME, NAME)