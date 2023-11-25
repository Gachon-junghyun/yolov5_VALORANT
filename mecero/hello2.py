from ctypes import *
import time

print("DD!")
dd_dll = windll.LoadLibrary('c:\DD94687.64.dll')

#키보드 win
dd_dll.DD_key(601, 1)
dd_dll.DD_key(602, 2)

time.sleep(2)

#절대 좌표
dd_dll.DD_mov(200, 200)

time.sleep(2)

#마우스 우클릭
dd_dll.DD_btn(4)
dd_dll.DD_btn(8)

#상대 좌표
dd_dll.DD_movR(200, 200)