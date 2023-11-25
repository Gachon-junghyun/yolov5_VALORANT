import cv2
from PIL import Image
import numpy as np

def bgr_to_rgb(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_image

def get_rectangle_data(matrix, start_row, start_col, num_rows, num_cols):
    rectangle_data = []
    for i in range(start_row, start_row + num_rows):
        row = []
        for j in range(start_col, start_col + num_cols):
            row.append(matrix[i][j])
        rectangle_data.append(row)
    return rectangle_data

cap = cv2.VideoCapture('input_video3.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2()
index = 0
while True:
    ret, frame = cap.read()

    if frame is None:
        break

    fgmask = fgbg.apply(frame)

    # 전경 객체 검출을 위한 이진화
    ret, fgmask = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    a = -999

    for contour in contours:
        # print(contour)
        (x, y, w, h) = cv2.boundingRect(contour)

        if a < cv2.contourArea(contour) and cv2.contourArea(contour) > 500 and h/w > 1.1:
            a = cv2.contourArea(contour)
            temp = contour


    (x, y, w, h) = cv2.boundingRect(temp)

    # Bounding Box 그리기 및 라벨링
    #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    rectangle_data = frame
    rectangle_data = np.array(rectangle_data)
    rectangle_data = bgr_to_rgb(rectangle_data)
    image = Image.fromarray(rectangle_data)
    index += 1


    image.save('data23/photo' + str(index) + '.jpg')


        #cv2.putText(frame, 'Detected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Frame', frame)

    # 종료 조건 (ESC 키 입력 시 종료)
    if cv2.waitKey(35) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()