import keyboard
from ctypes import *

return_list = []
i = 0

print("DD!")
dd_dll = windll.LoadLibrary('c:\DD94687.64.dll')
a = 0


def on_key(event):
    global a
    if a == 1:
        a = 0
        return
    else:
        a = 1
        if 'a' == event.name:
            dd_dll.DD_key(403, 1)
            dd_dll.DD_key(403, 2)
        if 'd' == event.name:
            dd_dll.DD_key(401, 1)
            dd_dll.DD_key(401, 2)
        if 'w' == event.name:
            dd_dll.DD_key(402, 1)
            dd_dll.DD_key(402, 2)
        if 's' == event.name:
            dd_dll.DD_key(302, 1)
            dd_dll.DD_key(302, 2)


#keyboard.on_press(on_key)
keyboard.on_release(on_key)
keyboard.wait()

#daad