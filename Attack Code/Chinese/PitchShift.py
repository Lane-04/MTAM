from pydub import AudioSegment
import numpy as np
from scipy.signal import resample
import tempfile
import os

semitone = [-3, 3]
candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']

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
    new_audio = new_audio.set_frame_rate(audio.frame_rate)
    
    # Export the modified audio
    new_audio.export(output_path, format="wav")

for c in candidateDirs:
    for s in semitone:
        current_dir = os.getcwd()
        operating_dir = current_dir + c
        saving_dir = operating_dir + 'Pitch/'+ str(s)
        os.makedirs(saving_dir, exist_ok=True)

        audioNames = sorted(os.listdir(operating_dir))
        for aud in audioNames:
            if aud.endswith('.mp3'):
                print(operating_dir + ': ' + aud)
                outName = saving_dir + '/' + aud.split('.')[0] + '_p'+ str(s) + '.wav'
                change_pitch(operating_dir + aud, s, outName)