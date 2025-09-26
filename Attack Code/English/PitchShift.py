from pydub import AudioSegment
import numpy as np
from scipy.signal import resample
import tempfile
import os

semitone = [-5, 5]

def change_pitch(audio_path, semitones, output_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_path)
    
    # Convert audio to numpy array
    samples = np.array(audio.get_array_of_samples())
    
    # Calculate the pitch shift factor
    factor = 2 ** (semitones / 12.0)
    
    # Calculate the new number of samples
    new_length = int(len(samples) / factor)
    
    # Resample the audio to the new length
    samples_resampled = resample(samples, new_length)
    
    # Convert resampled audio back to integer type
    samples_resampled_int = np.int16(samples_resampled)
    
    # Create a new AudioSegment with the resampled audio and new frame rate
    new_audio = audio._spawn(samples_resampled_int.tobytes(), overrides={'frame_rate': int(audio.frame_rate * factor)})
    
    # Resample the new audio back to the original frame rate
    new_audio = new_audio.set_frame_rate(int(audio.frame_rate * factor))
    
    
    # Export the modified audio
    new_audio.export(output_path, format="wav")


Name = os.listdir(PATH)

for name in Name:
    change_pitch(NAME, semitone[0], NAME)
