from pydub import AudioSegment
import numpy as np

import os

strengths = [350]
candidateDirs = ['/baidu/InsultAudio/', '/baidu/PornAudio/', '/baidu/SpamAudio/', 
                 '/nextdata/InsultAudio/', '/nextdata/PornAudio/', '/nextdata/SpamAudio/',
                 '/tencent/PornAudio/', '/tencent/SpamAudio/']

def reverb(audio, strength):

    duration = 0.4

    # 获取音频数据
    samples = audio.get_array_of_samples()

    # 模拟混响效果
    reverb_samples = np.convolve(samples, np.random.randn(strength) * duration, mode='same').astype(np.int16)

    # 创建一个新的音频段
    reverb_audio = AudioSegment(
        data=reverb_samples.tobytes(),
        sample_width=audio.sample_width,
        frame_rate=audio.frame_rate,
        channels=audio.channels
    )
    
    return reverb_audio

def process_audio(in_path, out_path, s):
    audio = AudioSegment.from_file(in_path)
    reverbed_audio = reverb(audio, s)
    reverbed_audio.export(out_path, format="wav")

for c in candidateDirs:
    for s in strengths:

        current_dir = os.getcwd()
        operating_dir = current_dir + c
        saving_dir = operating_dir + 'reverb/'+ str(s)
        os.makedirs(saving_dir, exist_ok=True)

        audioNames = sorted(os.listdir(operating_dir))
        for aud in audioNames:
            if aud.endswith('.mp3'):
                print(operating_dir + ': ' + aud)
                outName = saving_dir + '/' + aud.split('.')[0] + '_s' + str(s) + '.wav'
                process_audio(operating_dir + aud, outName, s)