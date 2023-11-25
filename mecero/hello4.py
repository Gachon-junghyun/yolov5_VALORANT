from ctypes import *
import time

mouseleftdown = 1
mouseleftup = 2
mouserightdown = 4
mouserightup = 8
mousewheeldown = 16
mousewheelup = 32

print("DD!")
dd_dll = windll.LoadLibrary('c:\DD94687.64.dll')

#키보드 win
#dd_dll.DD_key(601, 1)
#dd_dll.DD_key(602, 2)

time.sleep(2)

#절대 좌표
dd_dll.DD_mov(200, 200)

#time.sleep(2)

#마우스 우클릭
#dd_dll.DD_btn(4)
#dd_dll.DD_btn(8)

#상대 좌표
dd_dll.DD_btn(mouseleftdown)

dd_dll.DD_movR(1, 1)
time.sleep(1)
print("단계 1")
dd_dll.DD_movR(10, 10)
time.sleep(1)
print("단계 2")

dd_dll.DD_movR(230, 200)
time.sleep(1)
print("단계 3")

dd_dll.DD_btn(mouseleftup)