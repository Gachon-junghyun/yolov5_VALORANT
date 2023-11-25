import time
import pyautogui
import torch
import matplotlib.pyplot as plt
import numpy as np
import mss
import mss.tools
import asyncio
import cv2
from PIL import Image

changing = 0

async def async_function(x, y):
    cx = x / 30
    cx = y / 30
    await asyncio.sleep(0.03)

    global changing
    changing = 0

def async_function1(rectangle_data, x, y, h, w):

    #rectangle_data = np.array(rectangle_data)

    #display = denormalize_image(rectangle_data).astype(np.uint8).copy()
    #rectangle_data = rectangle_data[..., :3]
    s1 = int((x + h) / 2)
    s2 = int((w + y) / 2)
    diff = int( (y - w) / 5 )
    cv2.circle(rectangle_data, ( s1, s2 + diff * 1) , 5, (0, 255, 0), -1)
    while(pyautogui.position() > (x + h)/2 - 10 and pyautogui.position() < (x + h)/2 + 10 and pyautogui.position() > (y + w)/2 - 10 and pyautogui.position() < (y + w)/2 + 10):
        pass
    #cv2.imshow('Frame', rectangle_data)
    #cv2.waitKey(350)

    #cv2.rectangle(rectangle_data.copy(), (x, y), (h, w), (0, 255, 0), 2)


    image = Image.fromarray(rectangle_data)
    image.save('image/breach.jpg')



# Loading in yolov5s - you can switch to larger models such as yolov5m or yolov5l, or smaller such as yolov5n
model = torch.hub.load('ultralytics/yolov5','custom' ,'best.pt')

# 화면 스크린샷 찍기
with mss.mss() as sct:
    monitor = sct.monitors[1]  # 스크린 번호 설정 (0부터 시작하며, 현재 모니터의 번호에 따라 조정)
    before = 1
    while(1):
        screenshot = sct.grab(monitor)

        #image_np = np.array(screenshot)

        results = model('breach1053.jpg')
        #f = results.pandas().xyxy[0]['xmin']
        #print(len(results.pandas().xyxy[0].index))
        x = results.pandas().xyxy[0]

        image = cv2.imread('breach1053.jpg')

        if len(x.index) == 0:
            if before == 0:
                before = 0
                pass
            else:
                print("not detect")
                before = 0
        else:

            #print( ( x['xmin'] + x['xmax'] ) / 2)
            #print((x['ymin'] + x['ymax']) / 2)

            #change_x =  1720 - ((x['xmin'] + x['xmax']) / 2 )
            #change_y = 720 - ((x['ymin'] + x['ymax']) / 2)
            #print(x.iloc[0]['xmin'])
            async_function1(image, int(x.iloc[0]['xmin']), int(x.iloc[0]['ymin']), int(x.iloc[0]['xmax']), int(x.iloc[0]['ymax']))

            changing = 1
            if changing != 1:
                pass
                #asyncio.run(async_function(change_x, change_y))

            before = 1
