import whisper
from pydub import AudioSegment
import audiostretchy
import os

def transcribe_audio_with_whisper(audio_path):
    # Load Whisper model and transcribe the audio
    model = whisper.load_model("base")  # You can choose a different model if needed
    result = model.transcribe(audio_path, word_timestamps=True)
    return result

def find_keyword_times(transcript, keyword):
    keyword_times = []
    for segment in transcript['segments']:
        for word_info in segment['words']:
            if keyword.lower() in word_info['word'].lower():
                start_time = word_info['start']
                end_time = word_info.get('end', start_time + 1)  # Use end time if available, otherwise estimate
                keyword_times.append((start_time, end_time))
    return keyword_times

def extract_and_stretch_segment(audio, start_time, end_time, stretch_factor=1.5):
    start_ms = start_time * 1000
    end_ms = end_time * 1000
    segment = audio[start_ms:end_ms]
    # Stretch the segment
    stretched_segment = segment._spawn(segment.raw_data, overrides={"frame_rate": int(segment.frame_rate / stretch_factor)})
    stretched_segment = stretched_segment.set_frame_rate(segment.frame_rate)
    return stretched_segment

def insert_segment_into_audio(original_audio, segment, start_time, end_time):
    start_ms = start_time * 1000
    end_ms = end_time * 1000
    # Split original audio into parts: before, and after the segment
    before_segment = original_audio[:start_ms]
    after_segment = original_audio[end_ms:]
    # Combine the parts with the stretched segment
    combined_audio = before_segment + segment + after_segment
    return combined_audio

def save_audio(audio, path):
    audio.export(path, format="wav")
    print(f"Audio saved to {path}")

# Directory paths
Name = os.listdir(PATH)

for name in Name:
    print(name)

    # Main process
    audio_path = ""
    keyword_list = []
    
    original_audio = AudioSegment.from_wav(audio_path)

    # Save the modified audio
    export_path = ""
    save_audio(original_audio, export_path)