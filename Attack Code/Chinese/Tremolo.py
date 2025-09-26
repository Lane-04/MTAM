from pydub import AudioSegment
import numpy as np

import os

tremolo_freqs = [300]  # 颤音频率，单位Hz
candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']

def tremolo(audio, tremolo_freq):

    tremolo_depth = 500 # 颤音深度

    # 获取音频数据
    samples = audio.get_array_of_samples()

    # 生成颤音效果
    tremolo_samples = samples * (1 + tremolo_depth * np.sin(2 * np.pi * tremolo_freq * np.arange(len(samples)) / audio.frame_rate))

    # 归一化处理
    tremolo_samples = np.int16(tremolo_samples / np.max(np.abs(tremolo_samples)) * 32767)

    # 创建一个新的音频段
    tremolo_audio = AudioSegment(
        data=tremolo_samples.tobytes(),
        sample_width=audio.sample_width,
        frame_rate=audio.frame_rate,
        channels=audio.channels
    )
    
    return tremolo_audio

def process_audio(in_path, out_path, s):
    audio = AudioSegment.from_file(in_path)
    tremolo_audio = tremolo(audio, s)
    tremolo_audio.export(out_path, format="wav")

for c in candidateDirs:
    for f in tremolo_freqs:

        current_dir = os.getcwd()
        operating_dir = current_dir + c
        saving_dir = operating_dir + 'tremolo/'+ str(f)
        os.makedirs(saving_dir, exist_ok=True)

        audioNames = sorted(os.listdir(operating_dir))
        for aud in audioNames:
            if aud.endswith('.mp3'):
                print(operating_dir + ': ' + aud)
                outName = saving_dir + '/' + aud.split('.')[0] + '_f' + str(f) + '.wav'
                process_audio(operating_dir + aud, outName, f)
