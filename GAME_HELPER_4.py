import cv2
import pyautogui
import numpy as np
import sounddevice as sd
import asyncio
import keyboard
import time
y = 0

# 화면 크기 설정
screen_width, screen_height = pyautogui.size()

# 녹화할 파일명과 확장자 설정
output_file = "screen_record_audio.avi"

# 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# CUDA 가속을 사용하여 VideoWriter 생성
out = cv2.VideoWriter(output_file, fourcc, 24.0, (screen_width, screen_height), True)

# 오디오 녹음 설정
sample_rate = 44100
duration = 1.0
audio_frames = []

def audio_callback(indata, frames, time, status):
    audio_frames.append(indata.copy())

# 비동기적으로 키 입력을 처리하는 함수
async def key_listener():
    while True:
        if keyboard.is_pressed("q"):
            break
        await asyncio.sleep(0.1)  # 잠시 대기하여 CPU 부하를 줄임

# 비동기 루프 생성
async def main():
    loop = asyncio.get_event_loop()
    task = loop.create_task(key_listener())
    await asyncio.gather(task)


# 오디오 녹음 시작
stream = sd.InputStream(callback=audio_callback, channels=2, samplerate=sample_rate)
stream.start()

# 비동기 루프 실행
#qasyncio.run(main())

while True:
    # 현재 화면 이미지 가져오기
    img = pyautogui.screenshot()
    print('hello')
    # 이미지를 OpenCV 형식으로 변환
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # 프레임을 동영상 파일에 저장
    out.write(frame)

    # 화면에 표시 (optional)
    cv2.imshow("Screen Recording", frame)


# 'q' 키를 누르면 녹화 종료
if y == 100:
    print("========================")
    # 동영상 파일과 OpenCV 창 닫기
    out.release()
    cv2.destroyAllWindows()

    # 오디오 녹음 중지 및 저장
    stream.stop()
    audio_data = np.concatenate(audio_frames, axis=0)
    audio_file = "audio.wav"
    sd.write(audio_file, audio_data, sample_rate)
