import ctypes
import ctypes.wintypes
import time

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

print("Tab into Minecraft! You have 5 seconds...")
time.sleep(5)

print("TEST: Moving cursor with SetCursorPos")
for i in range(20):
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    ctypes.windll.user32.SetCursorPos(pt.x + 100, pt.y)
    time.sleep(0.02)

print("Done! Did your Minecraft view move?")
