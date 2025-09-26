from pydub import AudioSegment

import os

delay = [2000]
candidateDirs = []

def add_echo_effect(in_path, out_path, delay_ms=500, decay=0.5):
    # Load the audio file
    audio = AudioSegment.from_file(in_path)
    
    # Create a silent segment for delay
    delayed_audio = audio[:delay_ms]
    
    # Reduce the volume and create the echo effect
    echoed_audio = audio.overlay(delayed_audio, loop = True)
    
    # Export the modified audio
    echoed_audio.export(out_path, format="wav")

Name = os.listdir(PATH)

for name in Name:
    add_echo_effect(NAME, NAME, delay[0])