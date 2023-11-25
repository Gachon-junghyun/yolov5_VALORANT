import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav


def record_audio(duration, filename):
    fs = 44100  # 샘플링 속도 (Hz)

    print("녹음 시작")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # 녹음 완료 대기

    print("녹음 완료")
    wav.write(filename, fs, recording)  # 오디오 파일 저장

    print("파일 저장 완료")


# 녹음 시간과 저장할 파일명을 지정하세요.
duration = 5  # 녹음 시간 (초)
filename = "recorded_audio.wav"  # 저장할 파일명

record_audio(duration, filename)