import cv2

# 배경 제거 모델 생성
import keyboard
import numpy as np

model = cv2.createBackgroundSubtractorMOG2()

# 비디오 파일 열기
video = cv2.VideoCapture('input_video.mp4')

# 출력 동영상 파일 설정
output_file = 'output_video.avi'
fps = video.get(cv2.CAP_PROP_FPS)
frame_size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

while True:
    # 비디오 프레임 읽기
    ret, frame = video.read()

    if not ret:
        break

    # 배경 제거 적용
    fgmask = model.apply(frame)

    print(np.array(fgmask).shape)
    # 결과 표시
    cv2.imshow('Foreground', fgmask)

    # 출력 동영상에 프레임 추가
    output_video.write(fgmask)

    # 'q' 키를 누르면 종료
    cv2.waitKey(1)

    if keyboard.is_pressed('q'):
        # 리소스 해제
        video.release()
        output_video.release()
        cv2.destroyAllWindows()
        break

video.release()
output_video.release()
cv2.destroyAllWindows()